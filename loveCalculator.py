name1 = input("What is your name?")
name2 = input("what is your partner name?")
combineString = name1 + name2
lowerCaseString = combineString.lower()

t = lowerCaseString.count('t')
r = lowerCaseString.count('r')
u = lowerCaseString.count('u')
e= lowerCaseString.count('e')  

true = t+r+u+e

l= lowerCaseString.count('l') 
o = lowerCaseString.count('o') 
v = lowerCaseString.count('v') 
e = lowerCaseString.count('e') 

love = l+o+v+e

loveScore = int(str(true)+str(love))


if loveScore <10 or loveScore>90:
    print(f"You're perfect match and your lovescore is {loveScore}")
elif loveScore>=40 and loveScore<=50:
    print(f"You can be togther and your love score is {loveScore}")
    
else:
    print(f"Your Love Score is {loveScore}")


