def create_and_write_file(filename, content):
    with open(f"./test data/{filename}","w+") as file:
        file.write(content)
        file.seek(0)
        print(file.read())


create_and_write_file("notes.txt","Hello, this is my first file.")