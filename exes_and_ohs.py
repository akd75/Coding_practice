#DESCRIPTION:
#Check to see if a string has the same amount of 'x's and 'o's. The method must return a boolean and be case insensitive. The string can contain any char.

#Examples input/output:

#XO("ooxx") => true
#XO("xooxx") => false
#XO("ooxXm") => true
#XO("zpzpzpp") => true // when no 'x' and 'o' is present should return true
#XO("zzoo") => false

def xo(s):
    val_x=['x']
    val_o=['o']
    other=[]
    for elem in s:
        if elem == 'x'or elem=='X':
            val_x.append(elem)
        elif elem == 'o' or elem == 'O':
            val_o.append(elem)
        else:
            other.append(elem)
            
    print(s)
    print(val_x)
    print(val_o)
   

    if len(val_x)== len(val_o):
        return True 
    else:
        return False