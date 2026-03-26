# def average(a,b):
#     print("The average is",(a+b)/2)
# average(1,5)
###################################################################################################
# def average(a=9,b=1):
#     print("The average is",(a+b)/2)

# average(1,5)
###################################################################################################
# def average(a=9,b=1):
#     print("The average is",(a+b)/2)

# average(1,5)
###################################################################################################
# def name(fname,mname="Jhon",lname="Whatson"):
#     print("Hello,",fname,mname,lname)
# name("Amy")
###################################################################################################  
# def name(fname,mname,lname):
#     print("Hello,",fname,mname,lname)
# name(mname="peter",lname="hs",fname="ghost")
###################################################################################################
# def name(fname,mname,lname="df"):
#     print("Hello,",fname,mname,lname)
# name("Perer","amy")
###################################################################################################
# def average(*numbers):
#     sum=0
#     for i in numbers:
#         sum=sum+i
#     print("The average is",sum/len(numbers))

# average(10,5,45)
###################################################################################################
# def name(**name):
#     print("Hello,",name["fname"],name["mname"],name["lname"])
# name(mname="peter",lname="hs",fname="ghost")
###################################################################################################
def average(*numbers):
    sum=0
    for i in numbers:
        sum=sum+i
    # print("The average is",sum/len(numbers))
    return sum/len(numbers)


c=average(10,5,45)
print(c)