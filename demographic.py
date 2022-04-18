import pandas as pd 
import numpy as np 

df = pd.read_csv('articles.csv')
qf = df.sort_values(['total_events'],ascending = [False])
output = qf.head(20)