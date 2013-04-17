raw_input('first, an absurd method')
working = True
voter_file = []
while working:
    row = raw_input('Please enter the next line of the California voter file: ')
    if row == 'quit':
        working=False
    else:
        voter_file.append(row)

raw_input('next, use actual files')

f = open('input.csv')
voter_file = []
for line in f:
    voter_file.append(line.lower())
    print line.lower()
f.close()

raw_input('what if we try to open a file for reading that doesn\'t exist?')

try:
    f = open('nothere.csv')
except Exception as error:
    print error

raw_input('can read arbitrary number of characters from a file')

f = open('input.csv')

print f.read(100)

raw_input('can read lines from a file')
print f.readline()
print f.readline()

raw_input('write to a file')
g = open('output.csv','wb')

g.write(f.read(10))
g.writelines([f.read(100)])
g.close()
f.close()
f = open('input.csv','rU')
g = open('output.csv','w')
for line in f:
    g.write(line.lower())
g.close()
f.close()

raw_input('use string.split()')

f = open('input.csv', 'rU')
g = open('output_split.csv','w')
for line in f:
    split_line = line.split(',')
    g.write(split_line[4]+'\n')
f.close()
g.close()

raw_input('use csv')

import csv

f = open('input.csv','rU')
g = open('output_with_csv.csv','w')
f_csv = csv.reader(f)
g_csv = csv.writer(g)
for row in f_csv:
    #lengths = [len(r) for r in row]
    #g_csv.writerow(lengths)
    g_csv.writerow([row[4], row[6]])
f.close()
g.close()
