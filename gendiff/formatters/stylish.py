INDENT = '   '

TYPE_TO_STR = {
    'removed':
        lambda x, deep, indent=INDENT:
        f"\n{deep * indent}-{x['name']}: {value_format(x['value'], deep)}",
    'added':
        lambda x, deep, indent=INDENT:
        f"\n{deep * indent}+{x['name']}: {value_format(x['value'], deep)}",
    'updated':
        lambda x, deep, indent=INDENT:
        f"\n{deep * indent}-{x['name']}: {value_format(x['old_value'], deep)}"
        f"\n{deep * indent}+{x['name']}: {value_format(x['new_value'], deep)}",
    'stand':
        lambda x, deep, indent=INDENT:
        f"\n{deep * indent} {x['name']}:"
        f"{format_diff(x['children'], deep + 1)}"
        if ('children' in x) else
        f"\n{deep * indent} {x['name']}: {value_format(x['value'], deep)}"
}


def format_diff(diff, deep=0):
    out = ''
    for item in diff:
        out += TYPE_TO_STR[item['type']](item, deep)
    return out.replace('\n\n', '\n')


def dict2strings(dicto, deep):
    strings = []
    for key in dicto:
        if isinstance(dicto[key], dict):
            strings.append((deep, key + ':'))
            dict2strings(dicto[key], deep + 1)
        else:
            strings.append((deep, key + ': ' + str(dicto[key])))
    return strings


def strings2out(strings):
    out = ''
    for item in strings:
        out += f"{item[0] * INDENT}{item[1]}\n"

    return out


def value_format(value, deep):
    if isinstance(value, dict):
        return f"\n{strings2out(dict2strings(value, deep + 1))}"
    return f'{value}'
