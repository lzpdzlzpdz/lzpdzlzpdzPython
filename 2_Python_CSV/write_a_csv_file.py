import csv


csvfile = open('result.csv','wb')
csvoutput = csv.writer(csvfile,delimiter =',',quotechar='|',quoting=csv.QUOTE_MINIMAL)

csvoutput.writerow(['1','2','3'])
csvoutput.writerow(['a','b','c'])


csvfile.close()


print 'finish!'