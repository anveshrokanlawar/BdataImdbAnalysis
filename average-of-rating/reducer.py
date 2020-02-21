# Average
s = open("sorteddata.csv", "r", encoding='utf-8')
r = open("productionreducer.csv", "w", encoding='utf-8')

counter = 0
thiskey = ""
thisvalue = 0

r.write("Production_company,Average number of votes"+"\n")
for line in s:
  data = line.strip().split(',')
  production_company, votes = data

  if thiskey == "":
    if production_company:
      thiskey = production_company

  # apply the aggregation function
  
  if production_company == thiskey:
    thisvalue = thisvalue + int(votes)
    counter = counter + 1
  else:
    r.write( thiskey + ',' + str(thisvalue/counter)+'\n')
    # start over when changing keys
    thiskey = production_company
    thisvalue = int(votes)
    counter = 1

  # output final entry

r.write( thiskey + ',' + str(thisvalue/counter)+'\n')

s.close()
r.close()
