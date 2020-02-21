unsorted = open("countmapper.csv", "r",encoding='utf-8')
sorted = open("sorteddata.csv", "w",encoding='utf-8')

dataList = unsorted.readlines()

for line in dataList:
    data = line.strip().split(",")
    production_company,title=data
    if(production_company!="production_company"):
        dataList.sort()
        sorted.write(line)

unsorted.close()
sorted.close()