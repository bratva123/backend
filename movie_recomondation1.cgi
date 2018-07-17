#!/usr/bin/python2

##importing related libraries
import cgi,cgitb 
cgitb.enable()
import numpy as np
import pandas as pd

print("content-type:text/html")
print("")

pa=htmlpage.getvalue("top")

##importing dataset
movies=pd.read_csv('movies_metadata.csv',low_memory=False)
ratings=pd.read_csv('ratings.csv')

movie_temp['genres']=movie_temp['genres'].fillna('[]').apply(eval).apply(lambda x: [i['name'] for i in x])

movie_temp['genres']=movie_temp['genres'].fillna('[]').apply(lambda x:' '.join(map(str,x)))

ratings=ratings[['userId','movieId','rating']]

user_min=ratings['userId'].value_counts()
user_min=user_min[user_min>100]
ratings=ratings[ratings['userId'].isin(user_min.index)]

ratings.columns=['userId','id','rating']

new_movies_data=movie_temp[['title','id','genres','vote_average','popularity']]

new_movies_data=new_movies_data.dropna()

new_movies_data['id']=pd.to_numeric(new_movies_data['id'])

new_rating=ratings.merge(new_movies_data,on='id')

mask=new_rating['genres']==pa

new_rating=new_rating[mask]

table1=new_rating.groupby('title')['rating'].agg('count').reset_index().rename(columns={'rating':'num_ratings'})
table2=new_ratings.merge(table1,on='Book Name')

mask=table2['num_ratings']>=50
table2=table2[mask]

final_table=ultimate_final_table.drop_duplicates(['userId','title'])

pivot_table1=final_table.pivot_table(values='rating',index='title',columns='userId').fillna(0)

from scipy.sparse import csr_matrix
ultimate_sparse=csr_matrix(ultimate_pivot)

from sklearn.neighbors import  NearestNeighbors
nn=NearestNeighbors(metric='cosine',algorithm='brute')

nn.fit(ultimate_sparse)

distances,suggestion=nn.kneighbors(ultimate_pivot.iloc[43,:].values.reshape(1,-1),n_neighbors=6)
suggestion=suggestion.ravel()

for i in range(len(suggestion)):
    if i==0:
        print("books suggestion for {}".format(ultimate_pivot.index[suggestion[i]]))
        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>.")
    else:
        print(ultimate_pivot.index[suggestion[i]])





