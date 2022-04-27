# String: "fox The quick brown fox jumps over the lazy dog"
# Sub-string: "fox"

# take a string of characters and look that string inside of a second string
# 	1. check length of find string is shorter than than the search string
# 	2. look for

def find_string(sub_string: str, search_string: str) -> list[int]:
    result: list[int] = []
    if len(sub_string) > len(search_string):
        return result
    if len(sub_string) == 0:
        return result
    if len(search_string) == 0:
        return result
    for i in range(len(search_string)-(len(sub_string)-1)):
        if search_string[i:i+len(sub_string)] == sub_string:
            result.append(i)
    return result
    # return search_string.index(sub_string)


print(find_string("fox",
                  "fox The quick brown fox jumps over the lazy dog foxy fox"))

"""
Test Case #1
String: The quick brown fox jumps over the lazy dog
Sub-string: fox

Test Case #2:
String: fox
Sub-string: The quick brown fox jumps over the lazy dog
returns None

Test Case #3
FOX != fox if case matters

Test Case #4
String: The quick brown fox jumps over the lazy dog
Sub-string: Cow
return None

test case #5
check for empty string not throwing an error


"""
# fox
# ' fox '
# fox,
