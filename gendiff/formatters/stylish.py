INDENT = '    '
REMOVED = '  - '
ADDED = '  + '
STAND = INDENT

TYPE_TO_STR = {
    'removed':
        lambda x, deep, indent=INDENT:
        f"\n{deep * indent}{REMOVED}{x['name']}: {value_format(x['value'], deep + 1)}",
    'added':
        lambda x, deep, indent=INDENT:
        f"\n{deep * indent}{ADDED}{x['name']}: {value_format(x['value'], deep + 1)}",
    'updated':
        lambda x, deep, indent=INDENT:
        f"\n{deep * indent}{REMOVED}{x['name']}: {value_format(x['old_value'], deep + 1)}"
        f"\n{deep * indent}{ADDED}{x['name']}: {value_format(x['new_value'], deep + 1)}",
    'stand':
        lambda x, deep, indent=INDENT:
        f"\n{deep * indent}{STAND}{x['name']}: "
        f"{format_diff(x['children'], deep + 1)}"
        if ('children' in x) else
        f"\n{deep * indent}{STAND}{x['name']}: {value_format(x['value'],deep + 1)}"
}


def format_diff(diff, deep=0, indent=INDENT):
    out = ''
    for item in diff:
        try:
            out += TYPE_TO_STR[item['type']](item, deep)
        except KeyError:
            raise ValueError(f"'{item['type']}' is no such node type")
    return f"{{{out}\n{deep * indent}}}\n".replace('\n\n', '\n')


def value_format(value, deep, indent=INDENT):
    if isinstance(value, dict):
        out = '{'
        for key in value:
            out += f"\n{(deep + 1) * indent}{key}: "
            out += value_format(value[key], deep + 1)
        return out + f'\n{deep * indent}}}'
    if isinstance(value, bool):
        return f'{str(value).lower()}'
    if value is None:
        return 'null'
    return f'{value}'
