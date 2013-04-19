

data_file = open('./training_data/project_8_supporter_files/supporter1.txt', 'rb')
output_file = open('./training_data/project_8_output_files/supporter1_output.csv', 'wb')
for line in data_file:
    #this is one way
    #new_line = line.replace(' ',',')
    #this is a different way
    line_list = line.split(' ')
    new_line = ','.join(line_list)
    #write to file
    output_file.write(new_line)
data_file.close()
output_file.close()
