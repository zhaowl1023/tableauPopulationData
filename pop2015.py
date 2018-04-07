import csv
import xlsxwriter

num_in_2015={}
with open('respopagsex2000to2017.csv', newline='') as csvfile:
	reader = csv.reader(csvfile, delimiter=',')
	for row in reader:
		if row[5] == '2015':
			if row[0] in num_in_2015:
				num_in_2015[row[0]] = num_in_2015[row[0]] + int(row[4])
			else:
				num_in_2015[row[0]] = int(row[4])

book = xlsxwriter.Workbook('pop2015.xlsx')
sh = book.add_worksheet("2015")
row = 0
col = 0
sh.write(row, col, 'PA')
sh.write(row, col+1, 'Pop')
row = row + 1;
for item in num_in_2015:
	sh.write(row, col, item)
	sh.write(row, col+1, num_in_2015[item])
	row = row+1
book.close()
