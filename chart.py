import matplotlib.pyplot as k
query=['Thailand','America','china','Vietnam','Korea']
values=[20,15,35,10,20]
exp=[0,0,0,0.5,0]
k.pie(values,labels=query,autopct='%.f',startangle=90,explode=exp)
k.show()