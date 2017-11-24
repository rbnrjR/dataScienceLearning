import pandas as pd
import numpy

# olympic data ---- >
countries = ['China', 'USA','UK','Russia','Germany','Australia','India','Pakistan','Korea']
gold = [184,89,78,30,15,9,4,2,0]
silver = [110,76,67,45,34,23,18,14,0]
bronze = [70,89,65,47,44,38,15,9,6]
index = [1,2,3,4,5,6,7,8,9]

olympic_resultTable = {
    'country_name' : pd.Series(countries, index = index),
    'gold' : pd.Series(gold, index = index),
    'silver' : pd.Series(silver, index = index),
    'bronze' : pd.Series(bronze, index = index)
}

olympic_resultTable_df = pd.DataFrame(olympic_resultTable)

bronze_atleast_oneGold = olympic_resultTable_df['bronze'][olympic_resultTable_df['gold']>=1]

avg_bronze_atleast_oneGold = numpy.mean(bronze_atleast_oneGold)

avg_medals = olympic_resultTable_df[['gold','bronze','silver']].apply(numpy.mean)

print('olympic result -- > ')
print(olympic_resultTable_df)

print('analytics of bronze_atleast_oneGold -- > ')
print(bronze_atleast_oneGold)

print('average bronze_atleast_oneGold -- > ')
print(avg_bronze_atleast_oneGold)

print('average number of medals distributed -- >')
print(avg_medals)



# calcualting total points for each country
# 4 points for gold , 2 for silver, 1 for bronze

gold_points = numpy.dot(4, gold)
silver_points = numpy.dot(2,silver)
bronze_points = numpy.dot(1, bronze)

print('gold points -------------------- > ',gold_points)
print('gold points -------------------- > ',silver_points)
print('gold points -------------------- > ',bronze_points)

total_points = numpy.add(gold_points,silver_points,bronze_points) #add function is not properly adding the matrix
print('gold points -------------------- > ',total_points)


points_table = {
    'country_name' : pd.Series(countries, index = index),
    'points' : pd.Series(total_points, index = index)
}
points_table_df = pd.DataFrame(points_table)

print('Total points acquired by each country in olympics')
print(points_table_df)


medal_counts = olympic_resultTable_df[['gold','silver','bronze']]
points = numpy.dot(medal_counts,[4,2,1])

olympic_pointsTable = {
    'country_name' : pd.Series(countries),
    'points' : pd.Series(points)
}
olympic_pointsTable_df = pd.DataFrame(olympic_pointsTable)
print(olympic_pointsTable_df)
