"""
- onetimepad
    * یک استرینگ را گرفته و عدد یونیکد آن را با یک عدد تصادفی در یک عملیات ریاضی استفاده میکند
    * به ازای هر حرف استرینگ یک عدد تصادفی جداگانه استفاده میکند

"""
import random

class OneTime:
    def encrypt(self, text):
        plain = [ord(i) for i in text]
        key = []
        cipher = []
        for i in plain:
            k = random.randint(1, 300)
            c = (i + k) * k
            cipher.append(c)
            key.append(k)
        return cipher, key

    def decrypt(self, cipher, key):
        plain = []
        for i in range(len(key)):
            p = int((cipher[i]/key[i])-key[i])
            plain.append(chr(p))
        return "".join(i for i in plain)


c, k = OneTime().encrypt(text='amir')
print(c, k)
print(OneTime().decrypt(c, k))
