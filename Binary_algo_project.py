import random
import random as rn
Start=rn.randint(0,100)
#print(Start)
end= rn.randint(Start+2,100)
#print(end)
li=[x for x in range(Start,end,2)]
print(li)
user_input= int(input("Enter any number from 1 to 100 from list to find the index of the same : "))

def binary_search(li,user_input):
    lower=0
    upper=len(li)-1

    while lower<=upper:
        mid=(lower+upper)//2
        if li[mid]<user_input:
            lower=mid+1

#if user_input is samaller , ignore right half
        elif li[mid]>user_input:
            upper=mid-1
        else:
            return mid
        return -1

answer = binary_search(li, user_input)
if answer !=-1:
    print(f"{user_input} is present at index {answer}")
else:
    print("Not in list")