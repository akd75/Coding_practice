#DESCRIPTION:
#Your task is very simple. Just write a function takes an input string of lowercase letters and returns true/false depending on whether the string is in alphabetical order or not.

#Examples (input -> output)
#"kata" -> false ('a' comes after 'k')
#"ant" -> true (all characters are in alphabetical order)
#Good luck :)

def alphabetic(s):
    res=[]
    for elem in s:
        res.append(elem)
    res_sorted=sorted(res)
    
    return True if res==res_sorted else False