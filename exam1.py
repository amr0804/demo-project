m=[-5,-2,0,3,4]
print([n*2 for n in m])


s= 'ABC'
n= 1
for c in s :
    print (c * n, end="  ")
    n += 1

def find (a, **b):
    print (type(b))
find('letters', A='1',B='2')

#


        
text = "python programming is easy and simple language"

# Convert to uppercase
upper_text = text.upper()
print(upper_text)

# Convert to lowercase
lower_text = text.lower()
print(lower_text)  

# Convert to title case
title_text = text.title()
print(title_text)

# Convert to capitalized case
capitalize_text = text.capitalize()
print(capitalize_text)  

# Swap case
swap_text = text.swapcase()
print(swap_text)


#ques
class  peacock:
    def __init__(self, name):
        self.name = name  

    def color(self):
        return f"{self.name} saw peacock Bright feathers!"

peacock_color = peacock("I")
print(peacock_color.color())  

 
#ques

people={'Arham':'Blue','Lisa':'Yellow','Vinod':'Purple','Jenny':'Pink'}
numstud = len(people)
print("No of student:",numstud)
people['Lisa'] ='Green'
print("updated",people['Lisa'])        
del people ['Jenny']
print("updated1",people)
