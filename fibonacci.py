#Q3 Display Fibonacci series up to 10 terms
#example, 0, 1, 1, 2, 3, 5, 8, 13, 21. 

#########

# num=int(input("enter your number\n"))
# a=0
# b=1
# if num<=0:
#     print("please enter a positive integer")
# elif num==1:
#     print(a)
# else:
#     print(a,",",end="")
#     print(b,",",end="")
#     for i in range(2,num):
#         c=a+b
#         a=b
#         b=c
#         print(c,",",end="")

num=int(input("enter your number\n"))
a=0
b=1
if num<=0:
    print("please enter a positive integer")
elif num==1:
    print(a)
else:
    print(a,",",end="")
    print(b,",",end="")
    if num>2:
        for i in range(2,num):
                c=a+b
                a=b
                b=c
                print(c,",",end="")    