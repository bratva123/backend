#/usr/bin/python3
import numpy as np
import pandas as pd
import cgi

print("content-type:text/html")
print("")

data=cgi.FieldStorage()
pa=data.getvalue('book_name')
print(pa)

def suggest(book_name):
    b_index=np.where(ultimate_pivot.index==book_name)[0][0]
    distances,suggestion=nn.kneighbors(ultimate_pivot.iloc[b_index,:].values.reshape(1,-1),n_neighbors=6)
    suggestion=suggestion.ravel()
    for i in range(len(suggestion)):
        if i==0:
	  print("books suggestion for {}".format(ultimate_pivot.index[suggestion[i]]))
	  print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>.")
        else:
	  print(ultimate_pivot.index[suggestion[i]])
	    
books=pd.read_csv('BX-Books.csv',sep=';',error_bad_lines=False,encoding='latin-1')
books=books[['ISBN','Book-Title','Book-Author']]
books.columns=['ISBN','Book Name','Author']
ratings=pd.read_csv('BX-Book-Ratings.csv',sep=';',error_bad_lines=False,encoding='latin-1')
ratings.columns=['User_id','ISBN','rating']
user_min=ratings['User_id'].value_counts()
user_min=user_min[user_min>200]
ratings=ratings[ratings['User_id'].isin(user_min.index)]
ratings_with_bookname=ratings.merge(books,on='ISBN')
final_total_rating=ratings_with_bookname.groupby('Book Name')['rating'].agg('count').reset_index().rename(columns={'rating':'num_ratings'})
ultimate_final_table=ratings_with_bookname.merge(final_total_rating,on='Book Name')
mask=ultimate_final_table['num_ratings']>=50
ultimate_final_table=ultimate_final_table[mask]
ultimate_final_table=ultimate_final_table.drop_duplicates(['User_id','Book Name'])
ultimate_pivot=ultimate_final_table.pivot_table(values='rating',index='Book Name',columns='User_id').fillna(0)

from scipy.sparse import csr_matrix
ultimate_sparse=csr_matrix(ultimate_pivot)

from sklearn.neighbors import  NearestNeighbors
nn=NearestNeighbors(metric='cosine',algorithm='brute')
nn.fit(ultimate_sparse)
#distances,suggestion=nn.kneighbors(ultimate_pivot.iloc[237,:].values.reshape(1,-1),n_neighbors=6)
#suggestion=suggestion.ravel()

suggest(pa)
