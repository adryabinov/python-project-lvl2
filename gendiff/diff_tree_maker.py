def make_diff(data1, data2):
    diff = []
    for key in data1.keys() | data2.keys():

        removed = data1.keys() - data2.keys()
        added = data2.keys() - data1.keys()
        unchanged = data2.keys() & data1.keys()

        if key in removed:
            diff.append({
                'name': key,
                'value': data1[key],
                'type': 'removed',
            })

        if key in added:
            diff.append({
                'name': key,
                'value': data2[key],
                'type': 'added',
            })

        if key in unchanged:
            if isinstance(data1[key], dict) & isinstance(data2[key], dict):
                diff.append({
                    'name': key,
                    'children': make_diff(data1[key], data2[key]),
                    'type': 'stand',
                })
            else:
                if data1[key] == data2[key]:
                    diff.append({
                        'name': key,
                        'value': data1[key],
                        'type': 'stand',
                    })
                if data1[key] != data2[key]:
                    diff.append({
                        'name': key,
                        'old_value': data1[key],
                        'new_value': data2[key],
                        'type': 'updated',
                    })
    return sorted(diff, key=lambda x: x['name'])
