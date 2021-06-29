## Python program to sort numbers

to_sort=input("Enter some numbers and we will sort them in asceding rder \n")

to_sort=to_sort.split()

i=0
for s in to_sort:
    to_sort[i] = int(s)
    i+=1

a=sorted(to_sort)
print("Sorted string is: ")
print(a)