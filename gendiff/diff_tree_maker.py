def make_diff(data1, data2):

    diff = []
    all_contain = data1.keys() | data2.keys()
    first_contain_only = data1.keys() - data2.keys()
    second_contain_only = data2.keys() - data1.keys()

    for key in sorted(all_contain):
        if key in first_contain_only:
            diff.append({
                'name': key,
                'value': data1[key],
                'type': 'removed',
            })
            continue
        if key in second_contain_only:
            diff.append({
                'name': key,
                'value': data2[key],
                'type': 'added',
            })
            continue
        if isinstance(data1[key], dict) & isinstance(data2[key], dict):
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
            continue
    return diff
