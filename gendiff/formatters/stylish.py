INDENT = '    '
REMOVED = '  - '
ADDED = '  + '
STAND = '    '

supported_types = {
    'removed',
    'added',
    'updated',
    'nested',
    'unchanged'
}


def format_tree(tree):
    def walk(in_tree, depth=0):
        out = []
        for item in in_tree:
            if item['type'] not in supported_types:
                raise ValueError('diff or formatter is broken')
            if item['type'] == 'removed':
                out += f"\n{make_indent(depth)}{REMOVED}{item['name']}: "
                out += f"{format_value(item['value'], depth + 1)}"
            if item['type'] == 'added':
                out += f"\n{make_indent(depth)}{ADDED}{item['name']}: "
                out += f"{format_value(item['value'], depth + 1)}"
            if item['type'] == 'updated':
                out += f"\n{make_indent(depth)}{REMOVED}{item['name']}: "
                out += f"{format_value(item['old_value'], depth + 1)}"
                out += f"\n{make_indent(depth)}{ADDED}{item['name']}: "
                out += f"{format_value(item['new_value'], depth + 1)}"
            if item['type'] == 'nested':
                out += f"\n{make_indent(depth)}{STAND}{item['name']}: "
                out += f"{walk(item['children'], depth + 1)}"
            if item['type'] == 'unchanged':
                out += f"\n{make_indent(depth)}{STAND}{item['name']}: "
                out += f"{format_value(item['value'], depth + 1)}"
        return f"{{{''.join(out)}\n{make_indent(depth)}}}"
    return walk(tree)


def format_value(value, depth):
    if isinstance(value, dict):
        out = []
        for key in value:
            out += f"\n{make_indent(depth + 1)}{key}: "
            out += f"{format_value(value[key], depth + 1)}"
        return f"{{{''.join(out)}\n{make_indent(depth)}}}"
    if isinstance(value, bool):
        return str(value).lower()
    if value is None:
        return 'null'
    return str(value)


def make_indent(depth):
    return depth * INDENT
