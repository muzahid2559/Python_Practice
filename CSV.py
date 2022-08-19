# csv file read

'''import csv
file = open('example.csv')   # make object
file_reader = csv.reader(file)

data = list(file_reader)  # make list
print(data)
print(data[0][2])

for row in file_reader:
    print('Row no ='+str(file_reader.line_num)+' '+str(row))'''


# csv file write and append
import csv

output_file = open('out.csv', 'a', newline='')   # write = w and append = a
output_writer = csv.writer(output_file, delimiter='.')
output_writer.writerow(['1', '2', '3'])
output_writer.writerow(['15', '25', '35'])
output_file.close()
