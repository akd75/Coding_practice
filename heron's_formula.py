#DESCRIPTION:
#Write function heron which calculates the area of a triangle with sides a, b, and c (x, y, z in COBOL).

#Heron's formula:

#s*(s-a)*(s-b)*(s-c))**0.5
 
#where
#s= (a+b+c)/2​
 
#Output should have 2 digits precision.

#link =https://www.codewars.com/kata/57aa218e72292d98d500240f

def heron(a,b,c):
    s=(a+b+c)/2

    return round((s*(s-a)*(s-b)*(s-c))**0.5,2)