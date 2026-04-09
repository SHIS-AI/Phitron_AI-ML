def read_from_position(filename,message,position):
    with open("./test data/{filename}","w+") as file:
        file.write(message)
        file.seek(0)
        print(file.read(position))

read_from_position('hello.txt','World!',7)