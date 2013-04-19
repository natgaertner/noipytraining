raw_input('a while loop example')

driving_age = 16
smoking_age = 18
voting_age = 18
drinking_age = 21
curmudgeon_age = 35
social_security_age = 65
max_age = 100

age = 1
you_can = 'at age {0} you can {1}'
while age <= max_age:
    stuff_you_can_do = []
    if age >= driving_age:
        stuff_you_can_do.append('drive')
    if age >= smoking_age:
        stuff_you_can_do.append('smoke')
    if age >= voting_age:
        stuff_you_can_do.append('vote')
    if age >= drinking_age:
        stuff_you_can_do.append('drink')
    if age >= curmudgeon_age:
        stuff_you_can_do.append('tell kids they bother you')
    if len(stuff_you_can_do) == 0:
        print you_can.format(age,'do nothing of interest')
    elif len(stuff_you_can_do) == 1:
        print you_can.format(age,stuff_you_can_do[0])
    else:
        last_one = stuff_you_can_do.pop()
        print you_can.format(age,', '.join(stuff_you_can_do)) + ', and ' + last_one
    age+=1

raw_input('first while loop done')

done = False
while not done:
    inp = raw_input('enter an age (or "done" to exit): ')
    if inp == 'done':
        done = True
    elif not inp.isdigit():
        print 'please enter an integer'
    else:
        age = int(inp)
        stuff_you_can_do = []
        if age >= driving_age:
            stuff_you_can_do.append('drive')
        if age >= smoking_age:
            stuff_you_can_do.append('smoke')
        if age >= voting_age:
            stuff_you_can_do.append('vote')
        if age >= drinking_age:
            stuff_you_can_do.append('drink')
        if age >= curmudgeon_age:
            stuff_you_can_do.append('tell kids they bother you')
        if len(stuff_you_can_do) == 0:
            print you_can.format(age,'do nothing of interest')
        elif len(stuff_you_can_do) == 1:
            print you_can.format(age,stuff_you_can_do[0])
        else:
            last_one = stuff_you_can_do.pop()
            print you_can.format(age,', '.join(stuff_you_can_do)) + ', and ' + last_one


raw_input('second while loop done')

shifts_coverable = [2,4,1,3,2,5]
shifts_needed = 11
i = 0
shifts_covered = 0
while shifts_covered < shifts_needed:
    shifts_covered += shifts_coverable[i]
    i += 1
print i

raw_input('while list done')

try:
    shifts_coverable = [2,4,1,3,2,5]
    shifts_needed = 20
    i = 0
    shifts_covered = 0
    while shifts_covered < shifts_needed:
        shifts_covered += shifts_coverable[i]
        i += 1
    print i
except Exception as error:
    print error

raw_input('bad list while done')
