def make_diff(data1, data2):
    diff = []
    for key in sorted(data1.keys() | data2.keys()):
        if key not in data2.keys():
            diff.append({
                'name': key,
                'value': data1[key],
                'type': 'removed',
            })
            continue
        if key not in data1.keys():
            diff.append({
                'name': key,
                'value': data2[key],
                'type': 'added',
            })
            continue
        if (isinstance(data1[key], dict)
                & isinstance(data2[key], dict)):
            diff.append({
                'name': key,
                'children': make_diff(data1[key], data2[key]),
                'type': 'nested',
            })
            continue
        if data1[key] == data2[key]:
            diff.append({
                'name': key,
                'value': data1[key],
                'type': 'unchanged',
            })
            continue
        if data1[key] != data2[key]:
            diff.append({
                'name': key,
                'old_value': data1[key],
                'new_value': data2[key],
                'type': 'updated',
            })
    return diff
