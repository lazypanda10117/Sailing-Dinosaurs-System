import datetime
import json


def filterDict(dict_items, invalid):
    return {key: val for key, val in dict_items if key not in invalid}


def serializeJSONListData(tags, data):
    to_serialize = tags
    for json_obj_ref in to_serialize:
        if json_obj_ref in data:
            data[json_obj_ref] = json.dumps(data[json_obj_ref])
    return data


def grabValueAsList(dictionary):
    return list(dictionary.values())


def grabLinkValueFromChoices(choices, key):
    choice_data = {choice_id: choice_val for choice_id, choice_val in choices}
    return choice_data.get(key)


def noneCatcher(key, data):
    return data.get(key)


def jsonLoadCatch(text):
    try:
        return json.loads(text)
    except:
        return {}


def getTimeNow():
    return datetime.datetime.now()


def modAdd(base, add, mod):
    return ((base + add) % mod) + 1


def getViewJSON(action, element_id):
    return {"action": action, "id": element_id}


def updateDict(dictionary, new_dictionary):
    d = dictionary
    d.update(new_dictionary)
    return d


def getModelName(model):
    return model.__name__


def fallback(a, b):
    return b if a is None else a


def simpleEqtFormatter(equation, replace_dict):
    result = equation
    for key, replace_val in replace_dict.items():
        result = result.replace(key, str(replace_val))
    return result


def truncateText(text, length=150):
    return text if len(text) < length else text[:length] + "..."


def truncateDisplayScore(score):
    try:
        return float('%.3f' % score)
    except:
        return "N/A"


def findMaxInStrArr(arr):
    m = None
    for a in arr:
        try:
            b = int(a)
            if m is None:
                m = b
            if b > m:
                m = b
        except ValueError:
            continue
    return m


def getAlphabet(idx):
    alphabet_arr = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
                    'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    if idx > 25 or idx < 0:
        raise IndexError("Out of Alphabetical Range")
    return alphabet_arr[idx]


# For use within a lambda expression or as a wrapper for raise
def lraise(e):
    raise e


# Try to convert an object to a specfic type
def canConvertTo(type, obj):
    try:
        type(obj)
        return True
    except ValueError:
        return False
