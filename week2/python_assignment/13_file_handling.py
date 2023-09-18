sample_data = """sample data line 1
sample data line 2.
"""

with open("sample.txt", "w") as file:
    file.write(sample_data)

with open("sample.txt", "r") as file:
    file_content = file.read()

new_data = "New sample line to be appended"
with open("sample.txt", "a") as file:
    file.write(new_data)  

with open("sample.txt", "r") as file:
    updated_content = file.read()

print(file_content)
print(updated_content)


#--------------------------------------------

import csv

sample_csv_data = [
    ["Name", "Age"],
    ["Atlee", 25],
    ["Lokesh", 30],
]

with open("sample.csv", "w", newline="") as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerows(sample_csv_data)

with open("sample.csv", "r") as csv_file:
    csv_reader = csv.reader(csv_file)
    for row in csv_reader:
        print(row)

# Add another column and update the CSV file
new_column = ["Gender", "Male", "Male"]
updated_csv_data = [row + [gender] for row, gender in zip(sample_csv_data, new_column)]

# temp_csv_data = zip(sample_csv_data, new_column)
# for i in temp_csv_data: print(i)
# print(type(temp_csv_data))

with open("sample.csv", "w", newline="") as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerows(updated_csv_data)

# Read and print the updated CSV data
with open("sample.csv", "r") as csv_file:
    csv_reader = csv.reader(csv_file)
    for row in csv_reader:
        print(row)
