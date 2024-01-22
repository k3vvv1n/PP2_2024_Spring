
#while Loop
i = 1
while i < 6:
  print(i)
  i += 1
'''
1
2
3
4
5
'''


#With the break statement we can stop the loop even if the while condition is true:
i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1
'''
1
2
3
'''
