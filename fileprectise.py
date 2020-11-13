with open('workfile','a+') as f:
    print(f.read())
    f.writelines("i am happy!")
    f.writelines("ssss")
    print(f.tell())

 