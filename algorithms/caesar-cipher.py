"""
Caesar encryption algorithm is in this order that it takes each letter and returns 3 letters after it.
This algorithm is very old
"""

from string import ascii_letters

print(type(ascii_letters))
print(ascii_letters[1])


def cipher(phrase):
    lst = list(phrase)
    lst_main = list(ascii_letters)
    result = []
    for i in lst:
        if i == "x":
            result.append("a")
        elif i == "y":
            result.append("b")
        elif i == "z":
            result.append("c")
        else:
            temp = lst_main.index(i) + 3
            result.append(lst_main[temp])
    result = "".join(result)
    return result


print(cipher("oiahnocliuehrsvig hjsemopvghsls"))
