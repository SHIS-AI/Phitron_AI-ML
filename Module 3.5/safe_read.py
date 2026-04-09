try:
    with open('simple.txt','r') as file:
        print(file.read())

except Exception as e:

    print(e)
else:
    print(f"Hello, {file.read()}")
finally:
    print("Operation complete.")