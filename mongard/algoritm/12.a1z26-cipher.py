"""
- a1z26
    * یه الگوریتم رمزنگاری
    * هر حرف را با معادل یونیکد عددی خود جایگزین میکند

"""


def a1z26_encode(plain):
    return [ord(i) for i in plain]

print(en := a1z26_encode('amir koocheh'))

def decode(encode):
    return "".join([chr(i) for i in encode])

print(decode(en))
