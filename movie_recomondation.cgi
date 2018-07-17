#!/usr/bin/python2

##importing related libraries
import cgi,cgitb 
cgitb.enable()
import numpy as np
import pandas as pd

print("content-type:text/html")
print("")

##importing dataset
movies=pd.read_csv('movies_metadata.csv',low_memory=False)

##removing column from movies which are not use fuland store it into new variable
new_movies_data=movies[['budget','genres','title','popularity','production_companies','revenue','vote_average']]
htmlpage=cgi.FieldStorage()
pa=htmlpage.getvalue("top")

##removing the string from budget column which can not be typecasted to integer and they are replaced with '0'
new_movies_data['budget'][19730]='0'
new_movies_data['budget'][35587]='0'
new_movies_data['budget'][29503]='0'
##converting  budget valuein numeric(given in string)
new_movies_data[pa]=pd.to_numeric(new_movies_data[pa])

##calculating top_movie_budegt acording highest values of budget
top_movie_budget=new_movies_data.groupby('title')[pa].agg(sum).sort_values(ascending=False).reset_index()

##printing top 10 movies acording to highest budget
print("Top 10 Movies Acording To Their Budget----------------------------------------------------------------------------------------------------")
print("</br>")
print("</br>")
for i in range(0,10):
    print("{}>>>>>>>>for ${}".format(top_movie_budget['title'][i],top_movie_budget[pa][i]))
    print("</br>")
    print("</br>")
