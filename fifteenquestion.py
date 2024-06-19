import csv
def q15(filename):
    # data = [
    #     ["Name", "Age", "City"],
    #     ["Alice", 30, "New York"],
    #     ["Bob", 25, "Los Angeles"],
    #     ["Charlie", 35, "Chicago"]
    # ]
    # with open(filename, 'w', newline='') as file:
    #     csv_writer = csv.writer(file)
    #     csv_writer.writerows(data)
    
    with open(filename,'r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            print(row)
filename = 'C:/Users/muska/OneDrive/Desktop/example.csv'
