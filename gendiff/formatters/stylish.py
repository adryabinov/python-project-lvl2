def format(diff_data):
    return "todo"

def dict2tree(dicto, deep):
    strings = []
    def deep_dict2tree(dicto, deep):
        for key in dicto:

            if isinstance(dicto[key], dict):
                strings.append((deep, key))
                deep_dict2tree(dicto[key], deep + 1)
            else:
                strings.append((deep, key, str(dicto[key])))

    deep_dict2tree(dicto, deep)

    return strings

