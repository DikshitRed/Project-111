import csv
import pandas as pd 
import plotly.figure_factory as ff
import statistics
import plotly.graph_objects as go

df = pd.read_csv("./studentMarks.csv")
data = df["Math_score"].tolist()

mean = statistics.mean(data)
standardDeviation = statistics.stdev(data)         

fig = ff.create_distplot([data],["Math_score"], show_hist=False)
#fig.add_trace(go.Scatter(x = [mean,mean],y = [0,0.20],mode = "lines",name = "MEAN"))
fig.show()

print("Mean Of Poppulation: ",mean)
print("Standard Deviation of Population: ", standardDeviation)


