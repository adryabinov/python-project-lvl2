supported_types = {
    'removed',
    'added',
    'updated',
    'nested',
    'unchanged'
}


def format_value(value):
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
    def walk(in_tree, path=''):
        out = []
        for item in in_tree:
            if item['type'] not in supported_types:
                raise ValueError('diff or formatter is broken')
            if item['type'] == 'removed':
                out += f"Property \'{path}{item['name']}\' was removed\n"
            if item['type'] == 'added':
                out += f"Property \'{path}{item['name']}\'"
                out += ' was added with value: '
                out += f"{format_value(item['value'])}\n"
            if item['type'] == 'updated':
                out += f"Property \'{path}{item['name']}\'"
                out += f" was updated. From {format_value(item['old_value'])}"
                out += f" to {format_value(item['new_value'])}\n"
            if item['type'] == 'nested':
                out += (walk(
                    item['children'],
                    f"{path}{item['name']}.") + '\n')
        return ''.join(out).rstrip("\n")
    return walk(tree)
