with open('file1.txt') as file1:
    n1 = file1.readlines()
with open('file2.txt') as file2:
    n2 = file2.readlines()

common = [int(c) for c in n1 if c in n2]
print(n1)
print(common)