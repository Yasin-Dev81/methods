

# w : write -> قبلی ها را پاک می کند
# r : read -> قبلی ها را می خواند
# a : append -> به قبلی ها اضافه می کند

# ./ : در همین فایل
# ../ : فایل عقب تر

with open("file.txt", "r") as f :
    print (f.read())
    print (f.read()) # اجرا نمی شود

with open("file.txt", "r") as f :
    for line in f :
        print ("---", line, end="")

with open("file.txt", "r") as f :
    print (f.readlines())
    print (f.readlines()) # اجرا نمی شود

with open("file2.txt", "w") as f :# خالی کردن فایل -> انجام دستورات
    f.write("mohammad\nyasin\nali\n")
    f.writelines(["younes\n", "yousef\n"])

with open("file2.txt", "a") as f :
    f.write("X\nY\n")
    f.writelines(["Younes\n", "Yousef\n"])

# open 2 files
with open("file.txt", "r") as f, open("file2.txt", "a") as g :
    pass
