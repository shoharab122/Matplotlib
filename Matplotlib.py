import matplotlib.pyplot as plt
import numpy as np


arr=np.array([1,2,3,4,5])
arr2=np.array([54,12,32,22,83])
arr3=np.array([47,28,59,160,167])
arr4=np.array([5,15,25,35,45])
plt.grid(color='blue',linestyle='--',linewidth=0.5)
plt.title("Profit Chart",fontsize=10,color="blue",family="Comic Sans MS",loc="center",fontweight="bold")
plt.xlabel("DAYS",fontsize=10,color="green",family="Comic Sans MS",loc="center",fontweight="bold")
plt.ylabel("PROFIT",fontsize=10,color="green",family="Comic Sans MS",loc="center",fontweight="bold")

linestyles=dict(marker=".",markersize=20,markerfacecolor="yellow",markeredgecolor="red",linestyle='--',color="green",linewidth=3)

plt.plot(arr,arr2,**linestyles)

plt.plot(arr,arr3,**linestyles)
plt.plot(arr,arr4,**linestyles)
plt.tick_params(axis='both',color='blue',direction='inout',length=10,width=2)
plt.show()


#barchart
x=np.array(["A","B","C","D","E"])
y=np.array([23,45,56,78,89])
plt.bar(x,y,color="orange",edgecolor="red",width=0.5)
plt.title("Bar Chart",fontsize=10,color="blue",family="Comic Sans MS",
loc="center",fontweight="bold")
plt.xlabel("ITEMS",fontsize=10,color="green",family="Comic Sans MS",loc="center",fontweight="bold")
plt.ylabel("SALES",fontsize=10,color="green",family="Comic Sans MS",loc="center",fontweight="bold")
plt.show()

#piechart
labels = ['Python', 'Java', 'C++', 'Ruby']
sizes = [215, 130, 245, 210]
colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue']
explode = (0.1, 0, 0, 0)
plt.pie(sizes, explode=explode, labels=labels, colors=colors,
autopct='%1.1f%%', shadow=True, startangle=140)
plt.title("Programming Language Popularity",fontsize=10,color="blue",family="Comic Sans MS",
loc="center",fontweight="bold")
plt.axis('equal')
plt.show()

#scatter plot
x=np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y=np.array([99,86,87,88,100,86,103,87,94,78,77,85,86])
plt.scatter(x,y,color="purple",marker="*",s=100)
plt.title("Scatter Plot",fontsize=10,color="blue",family="Comic Sans MS",
loc="center",fontweight="bold")
plt.xlabel("X-AXIS",fontsize=10,color="green",family="Comic Sans MS",loc="center",fontweight="bold")
plt.ylabel("Y-AXIS",fontsize=10,color="green",family="Comic Sans MS",loc="center",fontweight="bold")
plt.show()

#histogram
data = np.random.randn(1000)
plt.hist(data, bins=30, color='cyan', edgecolor='black')
plt.title("Histogram",fontsize=10,color="blue",family="Comic Sans MS",
loc="center",fontweight="bold")
plt.xlabel("Value",fontsize=10,color="green",family="Comic Sans MS",loc="center",fontweight="bold")
plt.ylabel("Frequency",fontsize=10,color="green",family="Comic Sans MS",loc="center",fontweight="bold")
plt.show()

#area chart
x = np.arange(1, 6)
y1 = np.array([3, 5, 2, 8, 7])
y2 = np.array([1, 6, 4, 3, 5])
plt.fill_between(x, y1, color="skyblue", alpha=0.5)
plt.fill_between(x, y2, color="lightgreen", alpha=0.5)
plt.title("Area Chart",fontsize=10,color="blue",family="Comic Sans MS",
loc="center",fontweight="bold")
plt.xlabel("X-AXIS",fontsize=10,color="green",family="Comic Sans MS",loc="center",fontweight="bold")
plt.ylabel("Y-AXIS",fontsize=10,color="green",family="Comic Sans MS",loc="center",fontweight="bold")
plt.show()

#stackplot
x = np.arange(1, 6)
y1 = np.array([1, 3, 2, 4, 3])
y2 = np.array([2, 4, 1, 3, 5])
y3 = np.array([3, 2, 4, 1, 2])
plt.stackplot(x, y1, y2, y3, colors=['lightcoral', 'lightblue', 'lightgreen'])
plt.title("Stack Plot",fontsize=10,color="blue",family="Comic Sans MS",
loc="center",fontweight="bold")
plt.xlabel("X-AXIS",fontsize=10,color="green",family="Comic Sans MS",loc="center",fontweight="bold")
plt.ylabel("Y-AXIS",fontsize=10,color="green",family="Comic Sans MS",loc="center",fontweight="bold")
plt.show()

#subplots
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)
fig, (ax1, ax2) = plt.subplots(2)
ax1.plot(x, y1, color='blue')
ax1.set_title('Sine Wave')
ax2.plot(x, y2, color='red')
ax2.set_title('Cosine Wave')
plt.tight_layout()
plt.show()