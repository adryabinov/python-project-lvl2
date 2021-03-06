supported_types = {
    'removed',
    'added',
    'updated',
    'nested',
    'unchanged'
}


def stringify(value):
    if isinstance(value, dict):
        return '[complex value]'
    if isinstance(value, bool):
        return str(value).lower()
    if value is None:
        return 'null'
    if isinstance(value, str):
        return f'\'{value}\''
    return value


def format_tree(tree):
    def walk(nodes, path=''):
        result = []
        for node in nodes:
            if node['type'] not in supported_types:
                raise ValueError(
                    f"diff is broken: node type {node} "
                    f"not in supported types: "
                    f"{' '.join(supported_types)}")
            if node['type'] == 'removed':
                result.append(
                    f"Property \'{path}{node['name']}\' was removed\n")
            if node['type'] == 'added':
                result.append(
                    f"Property \'{path}{node['name']}\'"
                    ' was added with value: '
                    f"{stringify(node['value'])}\n")
            if node['type'] == 'updated':
                result.append(
                    f"Property \'{path}{node['name']}\'"
                    f" was updated. From {stringify(node['old_value'])}"
                    f" to {stringify(node['new_value'])}\n")
            if node['type'] == 'nested':
                result.append(walk(
                    node['children'],
                    f"{path}{node['name']}.") + '\n')
        return ''.join(result).rstrip("\n")
    return walk(tree)
