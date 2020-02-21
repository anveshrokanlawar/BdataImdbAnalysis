s = open("sorteddata.csv","r",encoding="utf-8")
r = open("maxreduced.csv", "w",encoding="utf-8")

thiskey = ""
thisvalue = 0
max =0


for line in s:
  data = line.strip().split(',')
  director, votes = data

  if thiskey == "":
    if director:
      thiskey = director

  # apply the aggregation function
  
  if director == thiskey:
    if max < int(votes):
      max = int(votes)
  else:
    r.write( thiskey + ',' + str(max)+'\n')
    # start over when changing keys
    thiskey = director
    thisvalue = int(votes)
    max = 0

  # output final entry

r.write( thiskey + ',' + str(max)+'\n')

s.close()
r.close()