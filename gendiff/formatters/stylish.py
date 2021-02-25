INDENT_TYPE = ' '
INDENT_SIZE = 4
FIX_SIZE = 4
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


def make_indent(depth,
                fix=None,
                indent_size=INDENT_SIZE,
                indent_type=INDENT_TYPE,
                fix_size=FIX_SIZE):
    dynamic_part = (depth - 1) * indent_size * indent_type
    fix_part = fix if fix else fix_size * indent_type
    return f"{dynamic_part}{fix_part}"


def format_tree(tree):
    def walk(in_tree, depth=1):
        out = []
        for item in in_tree:
            if item['type'] not in supported_types:
                raise ValueError('diff or formatter is broken')
            if item['type'] == 'removed':
                out += f"\n{make_indent(depth, REMOVED)}{item['name']}: "
                out += f"{stringify(item['value'], depth)}"
            if item['type'] == 'added':
                out += f"\n{make_indent(depth, ADDED)}{item['name']}: "
                out += f"{stringify(item['value'], depth)}"
            if item['type'] == 'updated':
                out += f"\n{make_indent(depth, REMOVED)}{item['name']}: "
                out += f"{stringify(item['old_value'], depth)}"
                out += f"\n{make_indent(depth, ADDED)}{item['name']}: "
                out += f"{stringify(item['new_value'], depth)}"
            if item['type'] == 'nested':
                out += f"\n{make_indent(depth, STAND)}{item['name']}: "
                out += f"{{{walk(item['children'], depth + 1)}}}"
            if item['type'] == 'unchanged':
                out += f"\n{make_indent(depth, STAND)}{item['name']}: "
                out += f"{stringify(item['value'], depth)}"
        return f"{''.join(out)}\n{make_indent(depth-1)}"
    return f"{{{walk(tree).rstrip(' ')}}}"


def stringify(value, depth):
    if isinstance(value, dict):
        out = []
        for key in value:
            out += f"\n{make_indent(depth + 1, STAND)}{key}: "
            out += f"{stringify(value[key], depth + 1)}"
        return f"{{{''.join(out)}\n{make_indent(depth)}}}"
    if isinstance(value, bool):
        return str(value).lower()
    if value is None:
        return 'null'
    return str(value)
