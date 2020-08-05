def custom_split(string, separators=None):
    if separators is None:
        separators = [" "]

    result = []
    word = ""
    for elem in string:
        if elem not in separators:
            word += elem
        else:
            if word != "":
                result.append(word)
                word = ""
    if word != "":
        result.append(word)
    return result


print(custom_split("helo, world and you  ! how are things?", [" ", "!"]))


def custom_split_test():
    assert custom_split("hello world") == ["hello", "world"]


custom_split_test()