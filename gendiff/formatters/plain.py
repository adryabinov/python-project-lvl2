TYPE_TO_STR = {
    'removed':
        lambda item, path:
        f"Property \'{path}{item['name']}\' was removed\n",
    'added':
        lambda item, path:
        f"Property \'{path}{item['name']}\'"
        f" was added with value: {format_value(item['value'])}\n",
    'updated':
        lambda item, path:
        f"Property \'{path}{item['name']}\'"
        f" was updated. From {format_value(item['old_value'])}"
        f" to {format_value(item['new_value'])}\n",
    'nested':
        lambda item, path:
        format_tree(
            item['children'],
            f"{path}{item['name']}."
        ) + '\n',
    'unchanged': lambda item, path: '',
}

supported_types = list(TYPE_TO_STR.keys())


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


def format_tree(tree, path=''):
    out = []
    for item in tree:
        if item['type'] not in supported_types:
            raise ValueError('diff or formatter is broken')
        out += TYPE_TO_STR[item['type']](item, path)
    return ''.join(out).rstrip("\n")