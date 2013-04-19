li = 'coke,coffee,mimosa,water,bloody mary,ice tea'.split(',')
for drink in li:
    print "Donny loves to drink " + drink

raw_input('first for loop done')

age_limits = [['drive',16],['smoke',18],['vote',18],['drink',21],['tell kids they bother you',35], ['collect social security',65]]

age = 1
you_can = 'at age {0} you can {1}'
max_age = 100
while age <= max_age:
    stuff_you_can_do = []
    for capability_and_age in age_limits:
        if age >= capability_and_age[1]:
            stuff_you_can_do.append(capability_and_age[0])
    if len(stuff_you_can_do) == 0:
        print you_can.format(age,'do nothing of interest')
    elif len(stuff_you_can_do) == 1:
        print you_can.format(age,stuff_you_can_do[0])
    else:
        last_one = stuff_you_can_do.pop()
        print you_can.format(age,', '.join(stuff_you_can_do)) + ', and ' + last_one
    age+=1

raw_input('better age test done')
