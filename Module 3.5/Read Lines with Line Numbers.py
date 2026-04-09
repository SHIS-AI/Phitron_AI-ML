def Read_Lines_with_Line_Numbers(filename):
    with open(f"./test data/{filename}",'w+') as file:
        n=int(input())
        for i in range(1,n+1):
            ip_str = str(input())
            file.write(f"{ip_str}\n")
        file.seek(0)
        print(file.read())

Read_Lines_with_Line_Numbers("data.txt")
