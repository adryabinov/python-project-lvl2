supported_types = ['removed', 'added', 'updated', 'nested', 'unchanged']


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


def format_tree(unformat_tree):
    def walk(tree, path=''):
        out = ''
        for item in tree:
            if item['type'] not in supported_types:
                raise ValueError('diff or formatter is broken')
            if item['type'] == 'removed':
                out += f"Property \'{path}{item['name']}\' was removed\n"
            if item['type'] == 'added':
                out += f"Property \'{path}{item['name']}\'"\
                       f" was added with value: {stringify(item['value'])}\n"
            if item['type'] == 'updated':
                out += f"Property \'{path}{item['name']}\'"\
                       f" was updated. From {stringify(item['old_value'])}"\
                       f" to {stringify(item['new_value'])}\n"
            if item['type'] == 'nested':
                out += walk(item['children'], f"{path}{item['name']}.") + '\n'
            if item['type'] == 'unchanged':
                out += ''
        return out.rstrip("\n")
    return walk(unformat_tree, '')
