TYPE_TO_STR = {
    'removed':
        lambda item, parent:
        f"Property \'{parent}{item['name']}\' was removed\n",
    'added':
        lambda item, parent:
        f"Property \'{parent}{item['name']}\'"
        f" was added with value: {format_value(item['value'])}\n",
    'updated':
        lambda item, parent:
        f"Property \'{parent}{item['name']}\'"
        f" was updated. From {format_value(item['old_value'])}"
        f" to {format_value(item['new_value'])}\n",
    'nested':
        lambda item, parent:
        format_tree(
            item['children'],
            f"{parent}{item['name']}."
        ) + '\n',
    'unchanged': lambda item, parent: '',
}

supported_types = list(TYPE_TO_STR.keys())


def format_value(value):
    return '[complex value]' if isinstance(value, dict) \
        else str(value).lower() if isinstance(value, bool) \
        else 'null' if (value is None) \
        else value if isinstance(value, int) \
        else f'\'{value}\''


def format_tree(tree, parent=''):
    out = ''
    for item in tree:
        if item['type'] not in supported_types:
            raise ValueError('diff or formatter is broken')
        out += TYPE_TO_STR[item['type']](item, parent)
    return out.rstrip("\n")
