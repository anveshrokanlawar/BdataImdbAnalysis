#### Project Name
## IMDB Analysis

#### Course: 
```
BigData-44517
```

#### Project Number
```
Sec 01-2
```

### Team Members
1. Rajender Ravi Varma Devulapally
1. Anvesh Rokanlawar
1. Leela Krishna Kosaraju
1. Akhil Kumar Reddy Busireddy
<br/>

#### Link to the repo
https://github.com/anveshrokanlawar/bigdata-imdb-analysis



#### Issue tracker link
https://github.com/anveshrokanlawar/bigdata-imdb-analysis/issues

## Introduction:
 In this project, we will be predicting about which director has highest rating, lowest rating,    average rating and finding the count of rating by the end of the project. Through this, we can predict the popularity of the director.

<br/>

#### Data Source Description
- The provided dataset is imdb reviews and movie ratings.Data is saved in .csv format with text data.
- Some of the key attributes are Title, Year, Director, Votes.
- VOLUME: The dataset is of size 164 MB with 81,273 rows and 22 columns. The source of the dataset is publicly available website https://www.imdb.com.
- VARIETY: The data available is in structured format.
- VELOCITY: The velocity of the dataset is medium. It is the monthly dataset and it was last updated 2 months ago.
- VERACITY: The data looks clean without any messy and is trustworthy as the data is obtained(Scraped) from publicly available website. But there are few empty fields in some columns on which we are not performing any computing operations.
- VALUE: From the data we can predict, towards which director movies are the people most interested or eagerly waiting to watch. This data would be useful for filmmaker to get collaborated with the top directors based on the data to make more profits.

#### Data :
- Local : [./data/IMDb-movies.csv](./data/IMDb-movies.csv)
- Original : <https://www.kaggle.com/stefanoleone992/imdb-extensive-dataset#IMDb%20movies.csv>


#### Big Data Problems :

1. Max - Leela Krishna Kosaraju
1. Question : For each director, find the maximum number of votes.
1. Solution : 
    1. Mapper Input : tt0003037,Juve contre Fantômas,Juve contre Fantômas,1913,1913-09-08,"Crime, Drama",61,France,French,Louis Feuillade,"Marcel Allain, Louis Feuillade",Société des Etablissements L. Gaumont,"René Navarre, Edmund Breon, Georges Melchior, Renée Carl, Yvette Andréyor, Laurent Morléas","In Part Two of Louis Feuillade's 5 1/2-hour epic follows FantÃ'mas, the criminal lord of Paris, master of disguise, the creeping assassin in black, as he is pursued by the equally resourceful Inspector Juve.",7.0,1295,,,,,8.0,22.0 
    
    2. Mapper Output/ Reducer input:
    Director: Louis Feuillade       Votes: 1295
    Director: Louis Feuillade      Votes: 1853
    Director: Alfred Machin       Votes: 112

    3. Reducer Output:
    Director: Louis Feuillade       Max_value: 3936

    4. Chart: Bar Chart.


1. Min - Akhil Kumar reddy busireddy
1. Question : For each director, find the minimum number of votes.
1. Solution : 
    1. Mapper Input : tt0003037,Juve contre Fantômas,Juve contre Fantômas,1913,1913-09-08,"Crime, Drama",61,France,French,Louis Feuillade,"Marcel Allain, Louis Feuillade",Société des Etablissements L. Gaumont,"René Navarre, Edmund Breon, Georges Melchior, Renée Carl, Yvette Andréyor, Laurent Morléas","In Part Two of Louis Feuillade's 5 1/2-hour epic follows FantÃ'mas, the criminal lord of Paris, master of disguise, the creeping assassin in black, as he is pursued by the equally resourceful Inspector Juve.",7.0,1295,,,,,8.0,22.0 
    
    2. Mapper Output/ Reducer input:
    Director: Louis Feuillade       Votes: 1295
    Director: Louis Feuillade      Votes: 1853
    Director: Alfred Machin       Votes: 112

    3. Reducer Output:
    Director: Louis Feuillade       Min_Value: 126

    4. Chart: Bar Chart.

