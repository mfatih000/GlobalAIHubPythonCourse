#Day1/Question1

list=[1,2,3,4,5,6,7,8]
half_list1=[]
half_list2=[]
for i in range(1,11):
    if(i<=10/2):
        half_list2.append(i)
    else:
        half_list1.append(i)

changed_list=half_list1+half_list2
print(changed_list)


#Day1/Question2

n=int(input("Write a number:"))

for i in range(0,n+1,2):
    print(i)

