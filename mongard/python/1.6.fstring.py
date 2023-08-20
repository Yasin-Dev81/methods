x = "yasin"
y = "khos manesh"

a = f"... {x} {y} ..."
b = "... {xxx} ...".format(
    xxx=x
)
c = "... {} {} ...".format(x, y)
d = "...{1} {0} ...".format(y, x)
e = "... %s ... %s ..." % (x, y)

print(a, b, c, d, e)
