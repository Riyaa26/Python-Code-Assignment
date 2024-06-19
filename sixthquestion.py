def q6(filename):
    try:
        file = open(filename, 'r')
        print("content in the file is \n{}".format(file.read()))
    except FileNotFoundError:
        print(f"The file {filename} was not found.")
    except IOError:
        print(f"An error occurred while reading the file {filename}.")

filename = 'C:/Users/muska/OneDrive/Desktop/demo.txt'  
