# list-tuple-snippets
#assigning elements to different lists
list1=[]
n1=int(input("enter number of elements in list "))
for i in range(n1):
    list1.append(input())
    
#accessing elements from a tuple
tuple=(1,2,3,"sud","fan")
n2=int(input("enter the index of the element u want to access "))
print(tuple[n2])

#deleting different dictionary elements
dictionary={'one':1 ,'two':2 ,'three':3 ,'four':4}
a=input("enter the key u want to delete ")
del dictionary[a]
