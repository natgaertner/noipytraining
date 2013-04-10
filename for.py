li = 'coke,coffee,mimosa,water,bloody mary,ice tea'.split(',')
for drink in li:
    #print "Donny loves to drink {drink}".format(drink=drink)
    print "Donny loves to drink " + drink

raw_input('first for loop done')

for i in range(0,10):
    print i*3

raw_input('range for loop done')

has_e = []
for drink in li:
    has_e.append('e' in drink)

print has_e

raw_input('building with a for loop done')

divisible_by_three = [i % 3 == 0 for i in range(0,100)]
print divisible_by_three

raw_input('first list comprehension done')

divisible_by_three_only = [i for i in range(0,100) if i % 3 == 0]
print divisible_by_three_only

raw_input('second list comprehension done')
