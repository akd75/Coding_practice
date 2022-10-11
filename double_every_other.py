#DESCRIPTION:
#Write a function that doubles every second integer in a list, starting from the left.
#Example:
#For input array/list :
#[1,2,3,4]
#the function should return :
#[1,4,3,8]


def double_every_other(lst):
    a=1
    res=[]
    for elem in lst:
        if a%2!=0:
            res.append(elem)
            a+=1
        else:
            res.append(elem*2)
            a+=1
    return res