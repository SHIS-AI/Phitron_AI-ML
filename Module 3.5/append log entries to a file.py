def add_log(message):
    with open("./logger/log.txt",'a') as file:
        file.write(f"{message}\n")

add_log("User logged in")
add_log("File uploaded")