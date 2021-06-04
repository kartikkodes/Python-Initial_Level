def check_unique(n):
  l = []
  for i in n:
    if i not in l:
      l.append(i)
  print(l)
p = [1,2,3,3,4,4,5,6,6]
check_unique(p)  
