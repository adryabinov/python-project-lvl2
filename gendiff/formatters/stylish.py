INDENT = '    '
REMOVED = '  - '
ADDED = '  + '
STAND = INDENT

TYPE_TO_STR = {
    'removed':
        lambda item, deep, indent=INDENT:
        '\n' + (deep * indent) + REMOVED + item['name'] + ': ' + value_format(item['value'], deep + 1),
    'added':
        lambda item, deep, indent=INDENT:
        '\n' + (deep * indent) + ADDED + item['name'] + ': ' + value_format(item['value'], deep + 1),
    'updated':
        lambda item, deep, indent=INDENT:
        '\n' + (deep * indent) + REMOVED + item['name'] + ': ' + value_format(item['old_value'], deep + 1) +
        '\n' + (deep * indent) + ADDED + item['name'] + ': ' + value_format(item['new_value'], deep + 1),
    'stand':
        lambda item, deep, indent=INDENT:
        '\n' + (deep * indent) + STAND + item['name'] + ": " + format_diff(item['children'], deep + 1)
        if ('children' in item) else
        '\n' + (deep * indent) + STAND + item['name'] + ": " + value_format(item['value'], deep + 1)
}


def format_diff(diff, deep=0, indent=INDENT):
    out = "{"
    for item in diff:
            out = out + (TYPE_TO_STR[item['type']](item, deep))
    return out + '\n' + (deep * indent) + "}"


def value_format(value, deep, indent=INDENT):
    if isinstance(value, dict):
        out = '{'
        for key in value:
            out += ("\n" + ((deep + 1) * indent) + str(key) + ": ")
            out += (value_format(value[key], deep + 1))
        return out + '\n' + (deep * indent) + "}"
    if isinstance(value, bool):
        return str(value).lower()
    if value is None:
        return 'null'
    return str(value)
