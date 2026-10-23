import matplotlib
print("\nThe MATPLOTLIB Library Version:",matplotlib.__version__)   # output: 3.11.2

import matplotlib.pyplot as plt

days = [1,2,3,4,5,6]
temperature = [30,32,34,31,29,35]
plt.plot(days,temperature, color='yellow',linewidth=2)  # it is used to create a line graph.
# plt.bar(days,temperature)    # it is used to create a bar graph.
plt.scatter(days,temperature, color='black',linewidth=3)  # it is used to create a scatter plot.

# add a graph title and labels for x and y axis.    
plt.title("---- DAYS v/s TEMPERATURE ----\n")

# it is the name of the x-axis and y-axis.
plt.xlabel("------ DAYS ------")
plt.ylabel("------ TEMPERATURE ------")

# add a grid line to the graph.
# plt.grid()
plt.xticks(days, ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT'])   # it is used to set the x-ticks of the current axes.
plt.yticks(temperature, ['30°C', '32°C', '34°C', '31°C', '29°C', '35°C']) 
plt.gca().set_facecolor('blue')
plt.grid()
plt.legend(["Temperature"], loc="upper left")   # it is used to place a legend on the axes.

plt.show()

