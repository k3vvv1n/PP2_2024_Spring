
#Using Asterisk*

fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, yellow, *red) = fruits
print(green)
print(yellow)
print(red)

#apple
#banana
#['cherry', 'strawberry', 'raspberry']


ruits = ("apple", "mango", "papaya", "pineapple", "cherry")
(green, *tropic, red) = fruits
print(green)
print(tropic)
print(red)

#apple
#['mango', 'papaya', 'pineapple']
#cherry