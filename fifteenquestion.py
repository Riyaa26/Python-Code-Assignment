import csv

def read_csv_and_print(file_path):
    try:
        with open(file_path, mode='r', newline='', encoding='utf-8') as file:
            csv_reader = csv.reader(file)
            for row in csv_reader:
                print(', '.join(row))
    except FileNotFoundError:
        print(f"The file {file_path} was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


file_path = 'data.csv'  # Replace with your CSV file path
read_csv_and_print(file_path)

