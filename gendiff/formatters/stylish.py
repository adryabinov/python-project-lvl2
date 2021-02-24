INDENT = '    '
REMOVED = '  - '
ADDED = '  + '
STAND = '    '

TYPE_TO_STR = {
    'removed':
        lambda item, depth, indent=INDENT:
        f"\n{make_indent(depth)}{REMOVED}{item['name']}: "
        f"{format_value(item['value'], depth + 1)}",
    'added':
        lambda item, depth, indent=INDENT:
        f"\n{make_indent(depth)}{ADDED}{item['name']}: "
        f"{format_value(item['value'], depth + 1)}",
    'updated':
        lambda item, depth, indent=INDENT:
        f"\n{make_indent(depth)}{REMOVED}{item['name']}: "
        f"{format_value(item['old_value'], depth + 1)}"
        f"\n{make_indent(depth)}{ADDED}{item['name']}: "
        f"{format_value(item['new_value'], depth + 1)}",
    'nested':
        lambda item, depth, indent=INDENT:
        f"\n{make_indent(depth)}{STAND}{item['name']}: "
        f"{format_tree(item['children'], depth + 1)}",
    'unchanged':
        lambda item, depth:
        f"\n{make_indent(depth)}{STAND}{item['name']}: "
        f"{format_value(item['value'], depth + 1)}",
}

supported_types = list(TYPE_TO_STR.keys())


def format_tree(tree, depth=0):
    out = []
    for item in tree:
        if item['type'] not in supported_types:
            raise ValueError('diff or formatter is broken')
        out += TYPE_TO_STR[item['type']](item, depth)
    return f"{{{''.join(out)}\n{make_indent(depth)}}}"


def format_value(value, depth):
    if isinstance(value, dict):
        out = []
        for key in value:
            out.append(f"\n{make_indent(depth + 1)}{key}: " 
                       f"{format_value(value[key], depth + 1)}")
        return f"{{{''.join(out)}\n{make_indent(depth)}}}"
    if isinstance(value, bool):
        return str(value).lower()
    if value is None:
        return 'null'
    return str(value)


def make_indent(depth):
    return depth * INDENT
