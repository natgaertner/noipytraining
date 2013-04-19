


email = raw_input('please enter an email: ')

if '@' in email and not email[-1] == '@' and '.' in email:
    print 'so far so good'

at_location = email.find('@')
post_at_email = email[at_location:]
dot_location = email.find('.')
if dot_location > at_location:
    print 'dot in right place'

if email.count('@') == 1:
    print 'right number of @s'
