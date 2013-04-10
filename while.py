
x = 4
while x >= 0:
    print 'you have {number} iterations left'.format(number=x)
    x = x - 1
    #x-=1

raw_input('first while loop done')

found = False
while not found:
    inp = raw_input('did you find it? ')
    if inp == 'yup':
        found = True

raw_input('second while loop done')

while True:
    inp = raw_input('did you find it? ')
    if inp == 'yup':
        break

raw_input('break while loop done')

li = [1,2,3,4,5,6]
i = 0
s = 0
while s < 15:
    s += li[i]
    i += 1
print i

raw_input('while list done')

try:
    li = [1,2,3,4,5,6]
    i = 0
    s = 0
    while s < 30:
        s += li[i]
        i += 1
    print i
except Exception as error:
    print error

raw_input('bad list while done')
