input = open('../data/IMdb-movies.csv',"r",encoding='utf-8')
output = open("maxmapper.csv", "w", encoding='utf-8')

for line in input:
    datalist = line.strip().split(",")
    imdb_title_id,title,year,date_published,duration,director,production_company,avg_vote,votes,reviews_from_users,reviews_from_critics = datalist
    if director!="director":
        output.write(director + "," + votes +"\n")

input.close()
output.close()