from video import df
from bokeh.plotting import figure,show,output_file

p=fiure(x_axis_type="datetime",height=160,width=500,responsive=True,title="Motion Graph")

q=p.quad(left=df["start"],right=df["End"],bottom=0,top=1,color="green")

output_file("Graph.html")
show(p)
