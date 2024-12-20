# bubble sort
my_array=[1,23,45,78,34,98,2]
n=len(my_array)
for i in range(n-1):
    for j in range(n-i-1):
        if my_array[j]>my_array[j+1]:
            my_array[j],my_array[j+1]=my_array[j+1],my_array[j]
print("Sorted array:",my_array)
# insertion sort

def insertion_sort(my_array):
    for i in range(1,len(my_array)):
        j=i
        while my_array[j-1] > my_array[j] and j>0:
            my_array[j-1],my_array[j] = my_array[j], my_array[j-1]
            j-=1

my_array=[1,23,45,78,34,98,2]
insertion_sort(my_array)
print(my_array)