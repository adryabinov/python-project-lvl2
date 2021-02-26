INDENT_TYPE = ' '
INDENT_SIZE = 4

supported_types = {
    'removed',
    'added',
    'updated',
    'nested',
    'unchanged'
}


def make_indent(
        depth,
        indent=INDENT_TYPE,
        size=INDENT_SIZE):
    return depth * size * indent


def stringify(value, depth):
    if isinstance(value, dict):
        lines = []
        for key in value:
            lines.append(
                f"\n{make_indent(depth + 1)}    {key}: "
                f"{stringify(value[key], depth + 1)}")
        return f"{{{''.join(lines)}\n{make_indent(depth + 1)}}}"
    if isinstance(value, bool):
        return str(value).lower()
    if value is None:
        return 'null'
    return str(value)


def format_tree(tree):
    def walk(nodes, depth=0):
        result = []
        for node in nodes:
            if node['type'] not in supported_types:
                raise ValueError(
                    f"diff is broken: node type '{node}' "
                    f"not in supported types: "
                    f"{' '.join(supported_types)}")
            if node['type'] == 'removed':
                result.append(
                    f"\n{make_indent(depth)}  - {node['name']}: "
                    f"{stringify(node['value'], depth)}")
            if node['type'] == 'added':
                result.append(
                    f"\n{make_indent(depth)}  + {node['name']}: "
                    f"{stringify(node['value'], depth)}")
            if node['type'] == 'updated':
                result.append(
                    f"\n{make_indent(depth)}  - {node['name']}: "
                    f"{stringify(node['old_value'], depth)}"
                    f"\n{make_indent(depth)}  + {node['name']}: "
                    f"{stringify(node['new_value'], depth)}")
            if node['type'] == 'nested':
                result.append(
                    f"\n{make_indent(depth)}    {node['name']}: "
                    f"{{{walk(node['children'], depth + 1)}}}")
            if node['type'] == 'unchanged':
                result.append(
                    f"\n{make_indent(depth)}    {node['name']}: "
                    f"{stringify(node['value'], depth)}")
        return f"{''.join(result)}\n{make_indent(depth)}"
    return f"{{{walk(tree).rstrip(' ')}}}"
