from sys import argv

script, file_name = argv

print(f"Working with {file_name}, press ENTER to continue:")
input()

line_number = input(f"Line number of {file_name} to insert data:")
line_number = int(line_number)
inputdata = input(f"\n\nData to be written to line {line_number}:")
inputdata = inputdata + "\n"

try:
    data = open(file_name, "r")
    list_of_lines = data.readlines()
    list_of_lines[line_number - 1] = inputdata
except IndexError:
    print(f"\nThere is not that many lines in {file_name}")

data = open(file_name, "w")
data.writelines(list_of_lines)
data.close()
