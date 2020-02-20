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

- Max - Leela Krishna Kosaraju
- Question : For each director, find the maximum number of votes.
- Solution : 
    1. Mapper Input : tt0003037,Juve contre Fantômas,Juve contre Fantômas,1913,1913-09-08,"Crime, Drama",61,France,French,Louis Feuillade,"Marcel Allain, Louis Feuillade",Société des Etablissements L. Gaumont,"René Navarre, Edmund Breon, Georges Melchior, Renée Carl, Yvette Andréyor, Laurent Morléas","In Part Two of Louis Feuillade's 5 1/2-hour epic follows FantÃ'mas, the criminal lord of Paris, master of disguise, the creeping assassin in black, as he is pursued by the equally resourceful Inspector Juve.",7.0,1295,,,,,8.0,22.0 
    
    2. Mapper Output/ Reducer input:
    Louis Feuillade       1295
    Louis Feuillade       1853
    Alfred Machin         112

    3. Reducer Output:
    Louis Feuillade       1853
    Alfred Machin         112

    4. Chart: Bar Chart.
   
- Min - Akhil Kumar reddy busireddy
- Question : For each director, find the minimum number of votes.
- Solution : 
    1. Mapper Input : tt0003037,Juve contre Fantômas,Juve contre Fantômas,1913,1913-09-08,"Crime, Drama",61,France,French,Louis Feuillade,"Marcel Allain, Louis Feuillade",Société des Etablissements L. Gaumont,"René Navarre, Edmund Breon, Georges Melchior, Renée Carl, Yvette Andréyor, Laurent Morléas","In Part Two of Louis Feuillade's 5 1/2-hour epic follows FantÃ'mas, the criminal lord of Paris, master of disguise, the creeping assassin in black, as he is pursued by the equally resourceful Inspector Juve.",7.0,1295,,,,,8.0,22.0 
    
    2. Mapper Output/ Reducer input:
    Louis Feuillade      1295
    Louis Feuillade      1853
    Alfred Machin        112

    3. Reducer Output:
    Louis Feuillade      1295
    Alfred Machin        112

    4. Chart: Bar Chart.


- Count - Ravi Varma Devulapally
- Question : For each Production Company, find the total count of records.
- Solution : 
     1. Mapper Input : tt0014702	Beau Brummel	Beau Brummel	1924	1924-03-30	Drama, History, Romance	135	USA		Harry Beaumont	Clyde Fitch, Dorothy Farnum	Warner Bros.	John Barrymore, Mary Astor, Willard Louis, Carmel Myers, Irene Rich, Alec B. Francis, William Humphrey, Richard Tucker, George Beranger, Clarissa Selwynne, John J. Richardson, Claire de Lorez, Michael...	George Bryan Brummel, a British military officer, loves Lady Margery, the betrothed of Lord Alvanley. Despite her own desperate love for Brummel, she submits to family pressure and marries ...	6.7	393		$ 290705
    
    2. Mapper Output/ Reducer input:
    Warner Bros		1
    Milano Film		1
    Warner Bros		1

    3. Reducer Output:
    Warner Bros.      2
    Milano Film       1

    4. Chart: Pie Chart.

- Count - Anvesh Rokanlawar
- Question : For each Production Company, find the average number of votes.
- Solution : 
     1. Mapper Input : tt0014702	Beau Brummel	Beau Brummel	1924	1924-03-30	Drama, History, Romance	135	USA		Harry Beaumont	Clyde Fitch, Dorothy Farnum	Warner Bros.	John Barrymore, Mary Astor, Willard Louis, Carmel Myers, Irene Rich, Alec B. Francis, William Humphrey, Richard Tucker, George Beranger, Clarissa Selwynne, John J. Richardson, Claire de Lorez, Michael...	George Bryan Brummel, a British military officer, loves Lady Margery, the betrothed of Lord Alvanley. Despite her own desperate love for Brummel, she submits to family pressure and marries ...	6.7	393		$ 290705
    
    2. Mapper Output/ Reducer input:
    Warner Bros	 7778
    Milano Film	 1236
    Warner Bros	 4356

    3. Reducer Output:
    Warner Bros.       6067
    Milano Film        1236

    4. Chart: Pie Chart.
