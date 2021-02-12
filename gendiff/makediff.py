from gendiff.parser import parse_file


def generate_diff(path1, path2):
    data1 = parse_file(path1)
    data2 = parse_file(path2)
    return make_diff(data1, data2)


def make_diff(data1, data2):
    diff = []
    for key in data1.keys() - data2.keys():
        diff.append({
            'removed': {
                'name': key,
                'value': data1[key]
            }
        })

    for key in data2.keys() - data1.keys():
        diff.append({
            'added': {
                'name': key,
                'value': data2[key]
            }
        })

    for key in data2.keys() & data1.keys():
        if isinstance(data1[key], dict) & isinstance(data2[key], dict):
            diff.append({
                'stand': {
                    'name': key,
                    'children': make_diff(data1[key], data2[key])
                }
            })
        else:
            if data1[key] == data2[key]:
                diff.append({
                    'stand': {
                        'name': key,
                        'value': data1[key]
                    }
                })
            else:
                diff.append({
                    'changed': {
                        'name': key,
                        'value': (data1[key], data2[key])
                    }
                })
    return diff



