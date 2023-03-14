# function will receive a function and an iterable and return a dictionary where the key is the
# result of the function


def group_by(function, iterable):
    result = {}
    for item in iterable:
        key = function(item)

        if key not in result.keys():
            result[key] = [item]
        else:
            result[key].append(item)
    return result

print(group_by(len, ["hi", "bye", "yo", "try"]))

