INDENT = '    '
REMOVED = '  - '
ADDED = '  + '
STAND = INDENT

TYPE_TO_STR = {
    'removed':
        lambda item, deep, indent=INDENT:
        f"\n{deep * indent}{REMOVED}{item['name']}: "
        f"{format_value(item['value'], deep + 1)}",
    'added':
        lambda item, deep, indent=INDENT:
        f"\n{deep * indent}{ADDED}{item['name']}: "
        f"{format_value(item['value'], deep + 1)}",
    'updated':
        lambda item, deep, indent=INDENT:
        f"\n{deep * indent}{REMOVED}{item['name']}: "
        f"{format_value(item['old_value'], deep + 1)}"
        f"\n{deep * indent}{ADDED}{item['name']}: "
        f"{format_value(item['new_value'], deep + 1)}",
    'stand':
        lambda item, deep, indent=INDENT:
        f"\n{deep * indent}{STAND}{item['name']}: "
        f"{format_diff(item['children'], deep + 1)}"
        if ('children' in item) else
        f"\n{deep * indent}{STAND}{item['name']}: "
        f"{format_value(item['value'], deep + 1)}"
}

supported_types = list(TYPE_TO_STR.keys())


def format_diff(diff, deep=0, indent=INDENT):
    out = "{"
    for item in diff:
        if item['type'] not in supported_types:
            raise ValueError('diff or formatter is broken')
        out += TYPE_TO_STR[item['type']](item, deep)
    return f"{out}\n{deep * indent}}}"


def format_value(value, deep, indent=INDENT):
    if isinstance(value, dict):
        out = '{'
        for key in value:
            out += f"\n{(deep + 1) * indent}{key}: "
            out += (format_value(value[key], deep + 1))
        return f"{out}\n{deep * indent}}}"
    if isinstance(value, bool):
        return str(value).lower()
    if value is None:
        return 'null'
    return str(value)
