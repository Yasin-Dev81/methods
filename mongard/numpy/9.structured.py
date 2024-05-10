"""
- structured array
    - وقتی که میخوایم اطلاعات مختلفی رو داخل یه آرایه ذخیره کنیم استفاده میشه

https://numpy.org/doc/stable/user/basics.rec.html

- record-arrays
    - structured array with attribute
    - بجای ایندکس از اتربیوت استفاده میکنه
https://numpy.org/doc/stable/user/basics.rec.html#record-arrays

"""
import numpy as np

# method 1
esm_sen = np.zeros(
    3,
    dtype={
        "names": ("esm", "sen"),
        "formats": (
            "U10", # str limit 10 letter
            "i4" # int 32 bit
        )
    }
)

print(esm_sen)

esm = np.array(["amir", "yasin", "rezaaaaaaaaaaaaaaaaaaaaaaaaaaaa"])
sen = np.array([12, 15, 31])

esm_sen["esm"] = esm
esm_sen["sen"] = sen

print(esm_sen)
print(esm_sen[0]["esm"])
print(esm_sen[esm_sen["sen"] > 18])
