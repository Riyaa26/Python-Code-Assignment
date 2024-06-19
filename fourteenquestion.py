 def read_and_print_lines():
    lines = []
    print("Enter multiple lines of text (press Enter on an empty line to stop):")
    
    while True:
        line = input()
        if line == "":
            break
        lines.append(line)
    
    print("\nYou entered:")
    for line in lines:
        print(line)

read_and_print_lines()
