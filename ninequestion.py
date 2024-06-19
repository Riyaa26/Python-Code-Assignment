def q9():
    string = str(input("enter a string : "))
    substring = str(input("enter a substring : "))
    if(substring in string):
        print("{} is present in {}".format(substring,string))
    else:
        print("{} is not present in {}".format(substring,string))
