def outer():
    print("I am outer")
    global a
    a=100
    def inner():
        print("I am inner")
        a=99
        print(a)
    inner()
    print(a)

outer()