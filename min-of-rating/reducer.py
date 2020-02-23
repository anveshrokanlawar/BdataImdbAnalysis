s = open("sorteddata.csv","r",encoding="utf-8")
r = open("minreduced.csv", "w",encoding="utf-8")

thisKey = ""
thisValue = 0

for line in s:
    data = line.strip().split('\t')
    director,votes = data

    if director != thisKey:
        if thisKey:
            # output the last key value pair result
            r.write( thisKey + ',' + str(thisValue) + '\n')
        
        #startover when changing keys
        thisKey = director
        thisValue = int(votes)

    # apply the aggregation function

    if(int(votes) < int(thisValue)):
        thisValue = int(votes)

# output the final entry when done
r.write( thisKey + ',' + str(thisValue) + '\n')

s.close()
r.close()