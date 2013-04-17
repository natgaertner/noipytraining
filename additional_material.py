#remove
li = ['coke','coffee','mimosa','water','bloody mary','ice tea']
li.remove('water')
li
li.append('coffee')
li
li.remove('coffee')
li
#extend
li2 = ['pancakes','eggs','potatoes']
li.extend(li2)
li

raw_input('a while loop with break')

while True:
    inp = raw_input('did you find it? ')
    if inp == 'yup':
        break

raw_input('break while loop done')

for i in range(0,10):
    print i*3

raw_input('range for loop done')

divisible_by_three = [i % 3 == 0 for i in range(0,100)]
print divisible_by_three

raw_input('first list comprehension done')

divisible_by_three_only = [i for i in range(0,100) if i % 3 == 0]
print divisible_by_three_only

raw_input('second list comprehension done')
