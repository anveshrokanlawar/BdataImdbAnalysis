unsorted = open("minmapper.csv", "r",encoding='utf-8')
sorted = open("sorteddata.csv", "w",encoding='utf-8')

data = unsorted.readlines()
data.sort()

for line in data:
    sorted.write(line)

unsorted.close()
sorted.close()