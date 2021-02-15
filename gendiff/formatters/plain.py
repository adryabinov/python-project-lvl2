TYPE_TO_STR = {
    'removed':
        lambda item, parent:
        f"\nProperty \'{parent}{item['name']}\' was removed",
    'added':
        lambda item, parent:
        f"\nProperty \'{parent}{item['name']}\'"
        f" was added with value: {format_value(item['value'])}",
    'updated':
        lambda item, parent:
        f"\nProperty \'{parent}{item['name']}\'"
        f" was updated. From value: {format_value(item['old_value'])}"
        f" to {format_value(item['new_value'])}",
    'stand':
        lambda item, parent:
        format_diff(
            item['children'],
            f"{parent}{item['name']}."
        ) if ('children' in item) else ''
}


def format_value(value):
    return '[complex value]' if isinstance(value, dict) \
        else str(value).lower() if isinstance(value, bool) \
        else 'null' if (value is None) \
        else f'\'{value}\''


def format_diff(diff, parent=''):
    out = ''
    for item in diff:
        try:
            out += TYPE_TO_STR[item['type']](item, parent)
        except KeyError:
            raise ValueError(f"'{item['type']}' is no such node type")
    return f"{out}".replace('\n\n', '\n')
