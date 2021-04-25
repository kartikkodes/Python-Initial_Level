#Splitting 

problem ='struggling', 'lazy', 'op', 'broke'
statement = 'Kartik', 'lazy'

print(problem)

l1=problem.split(', ')
print(l1)

l2 = problem.split('lazy')
print(l2)

l3 = problem.split('op')
print(l3)
# One thing about splitting I noticed is that it always print a comma and a space with that no matter what. Even if you are spliiting n a comma and space it will print a comma and a space in the output the place where it is splitting. Could be fucking awesome or could be fucking awful.

# JOINING

joined = ' is '.join(statement)
print(joined)

csv = ' isn\'t '.join(statement)
print(csv)
