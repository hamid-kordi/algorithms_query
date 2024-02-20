"""
a1z26 

    amir => [1,13,9,26]


"""


def encode(plain):
    "code your string"
    return [ord(elem) for elem in plain]


def decode(plain):
    "decode your num to str"

    return "".join([chr(elem) for elem in plain])


print(decode([97, 109, 107]))
