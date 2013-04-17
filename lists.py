'let\'s list some breakfast drinks'
'coke,coffee,mimosa,water,bloody mary,ice tea'.split(',')
#empty
[]
#different types
['coke','coffee','mimosa','water','bloody mary','ice tea',1]
#indexing
['coke','coffee','mimosa','water','bloody mary','ice tea'][1]
li = ['coke','coffee','mimosa','water','bloody mary','ice tea']
li[4]
#appending
li.append('grapefruit juice')
li
#insertion
li.insert(4,'maple syrup')
li
#pop
li.pop(2)
li
#length
len(li)
li[len(li)]
#inclusion
'mimosa' in li
#find index
li.index('bloody mary')
#count
li.append('grapefruit juice')
li.count('grapefruit juice')
#index again
li
li.index('grapefruit juice')
#combining
li2 = ['pancakes','eggs','potatoes']
li + li2
