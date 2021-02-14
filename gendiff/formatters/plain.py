def format_data(diff_data, parent=''):
    out = ''

    for item in sorted(diff_data, key=lambda x: x['name']):
        if item['type'] == 'removed':
            out += '\n' + ('Property ' + brackets(f"{parent}{item['name']}") + ' was removed')
        if item['type'] == 'added':
            out += '\n' + ('Property ' + brackets(f"{parent}{item['name']}") + ' was added with value: ' + value_format(item['value']))
        if item['type'] == 'updated':
            out += '\n' + ('Property ' + brackets(f"{parent}{item['name']}") + ' was updated with value: ' + value_format(item['old_value']) + ' to value ' + value_format(item['old_value']))
        if item['type'] == 'stand':
            if 'children' in item:
                out += format_data(item['children'], parent + item['name'] + '.')

    out = out.replace('\n\n', '\n')
    return out


def value_format(value):
    if isinstance(value, dict):
        return '[complex value]'
    return brackets(value)


def brackets(name):
    return f'\'{name}\''

