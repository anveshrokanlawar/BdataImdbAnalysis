unsorted = open("productionmapper.csv", "r",encoding='utf-8')
sorted = open("sorteddata.csv", "w",encoding='utf-8')

dataList = unsorted.readlines()

for line in dataList:
    data = line.strip().split(",")
    production_company,votes=data
    if(production_company!="production_company"):
        dataList.sort()
        # print (line)
        sorted.write(line)

unsorted.close()
sorted.close()