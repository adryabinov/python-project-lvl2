from gendiff.load import load_file
from gendiff.format import format_diff


def generate_diff(path1, path2, formatter='stylish'):
    return format_diff(make_diff(
        load_file(path1),
        load_file(path2)
    ), formatter)


def make_diff(data1, data2):
    diff = []
    for key in data1.keys() - data2.keys():
        diff.append({
            'name': key,
            'value': data1[key],
            'type': 'removed',
        })

    for key in data2.keys() - data1.keys():
        diff.append({
            'name': key,
            'value': data2[key],
            'type': 'added',
        })

    for key in data2.keys() & data1.keys():
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
            else:
                diff.append({
                    'name': key,
                    'old_value': data1[key],
                    'new_value': data2[key],
                    'type': 'updated',
                })
    return sorted(diff, key=lambda x: x['name'])
