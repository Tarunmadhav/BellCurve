
import plotly_express as px
import plotly.figure_factory as ff
import pandas
df=pandas.read_csv("Project-bell cureve\Data.csv")
heightsls=df["Avg Rating"].tolist()
figure1=ff.create_distplot([heightsls],["Mobile Brand"],show_hist=True)
figure1.show()