def characters_in_range(char1: str, char2: str) -> str:

    start = ord(char1)
    end = ord(char2)


    result = [chr(i) for i in range(start + 1, end)]

    return " ".join(result)


print(characters_in_range('a', 'd'))
print(characters_in_range('#', ':'))
print(characters_in_range('C', 'E'))