
#Else in For Loop

for x in range(6):
  print(x)
else:
  print("Finally finished!")
'''
0
1
2
3
4
5
Finally finished!
'''


for x in range(6):
  if x == 3: break
  print(x)
else:
  print("Finally finished!")
#If the loop breaks, the else block is not executed.
'''
0
1
2
'''