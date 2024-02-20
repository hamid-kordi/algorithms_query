"""
a1z26 

    amir => [1,13,9,26]


"""


def encode(plain):
    return [ord(i) for i in plain]


print(encode("salam"))
