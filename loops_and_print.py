def enumerate_list(list):
    result = []
    for i, s in enumerate(strings):
        if s:
            result.append(f"{i}. {s}")
    return result

colors = ["Red", "Green", "", "White", "Black"]
print(enumerate_list(colors))


def enumerate_backwards(list):
    result = []
    for i, s in enumerate(strings):
        if s:
            result.append(f"{len(strings) - i - 1}. {s[::-1]}")
    return result

colors = ["Red", "Green", "", "White", "Black"]
print(enumerate_list(colors))
