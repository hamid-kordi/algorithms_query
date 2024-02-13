"""
Caesar encryption algorithm is in this order that it takes each letter and returns 3 letters after it.
This algorithm is very old
"""

from string import ascii_letters



def cipher(phrase, n):
    lst = list(phrase)
    lst_main = list(ascii_letters)
    result = []
    for i in lst:
        temp = lst_main.index(i) + n
        if temp < len(lst_main):
            result.append(lst_main[temp])
        else:
            tempo = n - (len(lst_main) - lst_main.index(i))
            result.append(lst_main[tempo])
    result = "".join(result)
    return result

def decipher(phrase,n):
    print(">> decipher this phrase : ",phrase)
    lst = list(phrase)
    lst_main = list(ascii_letters)

    return phrase
print(cipher("asdXYZ", 5))
