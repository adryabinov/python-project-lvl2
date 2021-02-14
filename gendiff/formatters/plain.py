TYPE_TO_STR = {
    'removed':
        lambda x, parent:
        f"\nProperty \'{parent}{x['name']}\' was removed.",
    'added':
        lambda x, parent:
        f"\nProperty \'{parent}{x['name']}\' was added with value: {value_format(x['value'])}.",
    'updated':
        lambda x, parent:
        f"\nProperty \'{parent}{x['name']}\' was updated with value: {value_format(x['old_value'])}"
        f" to value: {value_format(x['new_value'])}.",
    'stand':
        lambda x, parent:
        format_diff(x['children'], f"{parent}{x['name']}.") if ('children' in x) else ''
}


def value_format(value):
    return '[complex value]' if isinstance(value, dict) else f'\'{value}\''


def format_diff(diff, parent=''):
    out = ''
    for item in diff:
        out += TYPE_TO_STR[item['type']](item, parent)
    return out.replace('\n\n', '\n')
