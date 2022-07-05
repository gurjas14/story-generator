import random
when = ['10 years back','Yeasterday','Day before yesterday','Few years back']
name = ['Rohit','Rohan','Yash','Sanjay','Shyam']
who = ['a rabbit','a mouse','an elephant','a horse','a dog']
residence = ['India','Canada','America','Germany','Brazil']
went = ['college','school','home','office','unversity']
happened = ['ate pizza','wrote a book','played games','watched tv','solved a mistery']
print(random.choice(when)+','+random.choice(who) +'they lived in'+ random.choice(residence)
+',went to the'+ random.choice(went) +'and'+ random.choice(happened))