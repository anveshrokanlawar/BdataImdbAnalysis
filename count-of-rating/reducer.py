# Average
s = open("sorteddata.csv", "r", encoding='utf-8')
r = open("countreducer.csv", "w", encoding='utf-8')

counter = 0
thiskey = ""
thisvalue = 0

r.write("Production_company,No. of movies"+"\n")
for line in s:
  data = line.strip().split(',')
  production_company, title = data

  if thiskey == "":
    if production_company:
      thiskey = production_company

  # apply the aggregation function
  
  if production_company == thiskey:
    counter = counter + 1
  else:
    r.write( thiskey + ',' + str(counter)+'\n')
    # start over when changing keys
    thiskey = production_company
    thisvalue = (title)
    counter = 1

  # output final entry

r.write( thiskey + ',' + str(counter)+'\n')

s.close()
r.close()
