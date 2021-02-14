def format_data(diff_data, deep=0):
    out = ''

    for item in sorted(diff_data, key=lambda x: x['name']):
        if item['type'] == 'removed':
            out += '\n' + (deep*'   ' + '-' + str(item['name']) + ': ' + str(value_format(item['value'], (deep + 1))))
        if item['type'] == 'added':
            out += '\n' + (deep*'   ' + '+' + str(item['name']) + ': ' + str(value_format(item['value'], (deep + 1))))
        if item['type'] == 'updated':
            out += '\n' + (deep*'   ' + '-' + str(item['name']) + ': ' + str(value_format(item['old_value'], (deep + 1))))
            out += '\n' + (deep*'   ' + '+' + str(item['name']) + ': ' + str(value_format(item['new_value'], (deep + 1))))
        if item['type'] == 'stand':
            if 'children' in item:
                out += '\n' + (deep*'   ' + ' ' + str(item['name']) + ':')
                out += format_data(item['children'], deep + 1)
            if 'value' in item:
                out += '\n' + (deep*'   ' + ' ' + str(item['name']) + ': ' + str(value_format(item['value'], (deep + 1))))
    out = out.replace('\n\n', '\n')
    return out

def dict2strings(dicto, deep):
    strings = []
    def deep_dict2tree(dicto, deep):
        for key in dicto:

            if isinstance(dicto[key], dict):
                strings.append((deep, key + ':'))
                deep_dict2tree(dicto[key], deep + 1)
            else:
                strings.append((deep, key + ': ' + str(dicto[key])))
    deep_dict2tree(dicto, deep)
    return strings

def strings2out(strings):
    out = ''
    for item in strings:
        out = out + (item[0]*'   ' + item[1]) + '\n'

    return out

def value_format(value, deep):
    if isinstance(value, dict):
        return '\n' + strings2out(dict2strings(value, deep))
    return value
