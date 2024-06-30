import requests,openpyxl
from bs4 import BeautifulSoup
import pandas as pd
try:
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    source = requests.get('https://www.imdb.com/chart/top/', headers=headers)
    source.raise_for_status()
    soup = BeautifulSoup(source.text, 'html.parser')

    # Find the section containing the movie list
    movie_list = soup.find('ul',class_="ipc-metadata-list ipc-metadata-list--dividers-between sc-a1e81754-0 eBRbsI compact-list-view ipc-metadata-list--base")
    #movies = movie_list.find_all('tr')
    #df=pd.DataFrame(columns=['moviename',''
    movv=[]
    #print(len(movie_list))
    df=pd.DataFrame(columns=["Movie","Year","Duration","Age"])
    for movie in movie_list:
       # movi=movie.find('div',class_="ipc-metadata-list-summary-item__c")
       # mov=movie.find('div',class_="ipc-metadata-list-summary-item__tc")
       # mo=mov.find('div',"sc-b189961a-0 hBZnfJ cli-children")
        ll=[]
        na=movie.find('div',class_="ipc-title ipc-title--base ipc-title--title ipc-title-link-no-icon ipc-title--on-textPrimary sc-b189961a-9 iALATN cli-title").a.text
        ll.append(na[4:])
        ye=movie.find('div',class_="sc-b189961a-7 feoqjK cli-title-metadata").find_all('span',class_='sc-b189961a-8 kLaxqf cli-title-metadata-item')
        for i in ye:
            pp=i.text
            ll.append(pp)
        df.loc[len(df)]=ll
        #print(ye)
        #sheet.append([na,ye])
    print(df)
except Exception as e:
    print(e)
"""for movie in movie_list:
        title = movie.find('td', class_='titleColumn').a.text
        rank = movie.find('td', class_='titleColumn').get_text(strip=True).split('.')[0]
        rating = movie.find('td', class_='ratingColumn imdbRating').strong.text
        print(f'{rank}. {title} - Rating: {rating}')"""



#pd.to_csv("data.csv")

"""
output :
                                               Movie  Year Duration Age
0                            he Shawshank Redemption  1994   2h 22m   A
1                                       he Godfather  1972   2h 55m   A
2                                     he Dark Knight  2008   2h 32m  UA
3                              he Godfather: Part II  1974   3h 22m   A
4                                        2 Angry Men  1957   1h 36m   U
5                                    chindler's List  1993   3h 15m   A
6       he Lord of the Rings: The Return of the King  2003   3h 21m   U
7                                        ulp Fiction  1994   2h 34m   A
8   he Lord of the Rings: The Fellowship of the Ring  2001   2h 58m   U
9                    Il Buono, Il Brutto, Il Cattivo  1966   2h 41m   A
10                                      Forrest Gump  1994   2h 22m  UA
11             The Lord of the Rings: The Two Towers  2002   2h 59m  UA
12                                        Fight Club  1999   2h 19m   A
13                                         Inception  2010   2h 28m  UA
14    Star Wars: Episode V - The Empire Strikes Back  1980    2h 4m  UA
15                                        The Matrix  1999   2h 16m   A
16                                        GoodFellas  1990   2h 25m   A
17                   One Flew Over the Cuckoo's Nest  1975   2h 13m   A
18                                             Se7en  1995    2h 7m   A
19                                      Interstellar  2014   2h 49m  UA
20                             It's a Wonderful Life  1946   2h 10m  PG
21                              Shichinin No Samurai  1954   3h 27m   U
22                          The Silence of the Lambs  1991   1h 58m   A
23                               Saving Private Ryan  1998   2h 49m   A
24                                       City of God  2002   2h 10m   A
"""