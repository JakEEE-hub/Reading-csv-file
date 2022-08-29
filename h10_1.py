with open("h10_1.csv", "r") as file:
    file_line = file.read().splitlines()

    for line in file_line:
        file_inline = line.split(",")
        print(f"{file_inline[0]} is {file_inline[1]} years old and {file_inline[2]}!")

