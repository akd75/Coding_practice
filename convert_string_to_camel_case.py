#DESCRIPTION:
#Complete the method/function so that it converts dash/underscore delimited words into camel casing.
#The first word within the output should be capitalized only if the original word was capitalized (known as Upper Camel Case, also often referred to as Pascal case). 
#The next words should be always capitalized.

#Examples
#"the-stealth-warrior" gets converted to "theStealthWarrior"
#"The_Stealth_Warrior" gets converted to "TheStealthWarrior"

def to_camel_case(text):
    if text=='':
        return ''
    else:
        n=0
        res=[]
        #trouver emplacement où mettre les majuscules"
        for mot in text:
            if mot =='_' or mot=='-':
                res.append(n+1)
            n+=1

        #mettre les majuscules
        text=list(text)

        for val in res:

            text[val]=text[val].upper()
        if text[0].isupper():
            text[0]=text[0].upper()
            
        text=''.join(text)    

        #retirer les '-'
        text=text.replace('-','')
        text=text.replace('_','')
        return text