



import matplotlib.pyplot as plt
import pandas as pd
reviews=pd.read_csv("fandango_score_comparison.csv")
norm_reviews=reviews[['FILM','RT_user_norm','Metacritic_user_nom','IMDB_norm','Fandango_Ratingvalue','Fandango_Stars']]
norm_reviews.head()




name_columns=norm_reviews.columns.tolist()
from numpy import arange
bar_positions=arange(5)+0.75
bar_positions=bar_positions.tolist()
bar_heights=norm_reviews.iloc[0,:].tolist()[1:]
fig=plt.figure(figsize=(8,5))
ax=fig.add_subplot(1,1,1)
tick_positions=range(1,6)
ax.bar(left=bar_positions,height=bar_heights,width=0.5,align='center')
ax.xaxis.set(ticks=tick_positions, ticklabels=name_columns)
plt.xticks(rotation=90)
ax.set(title="Average User Rating For Avengers: Age of Ultron (2015)", ylabel="Average Rating", xlabel="Rating Source")
plt.show()