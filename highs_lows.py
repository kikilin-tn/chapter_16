"""
印出檔案標頭及其位置
藉此可了解每個標頭的索引值
"""
import csv

#Get high temperature form file
filename = 'sitka_weather_2018_full.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    #for index, column_header in enumerate(header_row):
        #print(index, column_header)
    highs = []
    for row in reader:
        highs.append(row[8])

    print(highs)
