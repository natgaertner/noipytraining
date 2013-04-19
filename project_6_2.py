
total_attendees = int(raw_input('what should the total attendees allowed be? '))

command = 'a'
attendee_list = []
i = 0
while command != 'f' and i < total_attendees:
    command = raw_input('do you want to (a)dd an attendee or (f)inalize the list? ')
    if command == 'a':
        name_to_add = raw_input('please enter a name of an attendee to add: ')
        attendee_list.append(name_to_add)
        i = i+1
for attendee in attendee_list:
    print '{0} is attending'.format(attendee)
#print attendee_list
