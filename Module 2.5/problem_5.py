lst = [1,2,3,4,5,6]
even = list(filter(lambda x: x%2==0,lst))
square = list(map(lambda x : x **2,even))
print(square)