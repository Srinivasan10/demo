def about_me(your_name):
    print("The wise {} loves Python.".format(your_name))            

def HW():
    print("Hello World!")

def Both():
    HW()
    about_me("Ab")

Both()

Mydict = {"a" : 1,"b" :12, "c" : {"d":15}} 
print(Mydict["c"]["d"])