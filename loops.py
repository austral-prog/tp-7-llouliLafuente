def index_of_by_index(string, strings, start):
    index = strings.index(string, start) if string in strings[start:] else -1
    return index + start if index >= 0 else -1


def index_of_empty(strings):
    index = strings.index("") if "" in strings else -1
    return index


def index_of(string, strings):
    index = strings.index(string) if string in strings else -1
    return index


def put(string, strings):
    index = next((i for i, s in enumerate(strings) if s == ""), len(strings))
    if index < len(strings):
        strings[index] = string
        return index
    return -1


def remove(string, strings):
    strings = [s if s != string else "" for s in strings]
    count = sum(1 for s in strings if s == "")
    return count
