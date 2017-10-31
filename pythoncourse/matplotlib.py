# Import the necessary packages and modules
import matplotlib.pyplot as plt
import numpy as np


# Prepare the data
x = np.linspace(0, 10, 100)

# Plot the data
plt.plot(x, x, label='linear')

# Add a legend
plt.legend()

# Show the plot
plt.show()

# MatplotLib -- Visualization Package.

# pyplot -- A module inside Matplotlib -- create figures and axes to draw plots. 

# pylab -- It bulk imports pyplot and the numpy library and was generally recommended when you were working with arrays, 
#  			doing mathematics interactively and wanted access to plotting features. (Not recommended)


# # The *Figure* is the overall window or page that everything is drawn on. 

# It’s the top-level component of all the ones that you will consider in the following points. You can create multiple independent Figures. 
# A Figure can have several other things in it, such as a suptitle, which is a centered title to the figure. 
# You’ll also find that you can add a legend and color bar, for example, to your Figure.


# To the figure you add Axes. The Axes is the area on which the data is 
# plotted with functions such as plot() and scatter() and that can have ticks, labels, etc. associated with it. 
# This explains why Figures can contain multiple Axes.


fig = plt.figure()

# With set_xlim
ax = fig.add_subplot(111) # called the axis object.
ax.plot([1, 2, 3, 4], [10, 20, 25, 30], color='lightblue', linewidth=3)
ax.scatter([0.3, 3.8, 1.2, 2.5], [11, 25, 9, 26], color='darkgreen', marker='^')
ax.set_xlim(0.5, 4.5)
plt.show()

# with xlim
plt.plot([1, 2, 3, 4], [10, 20, 25, 30], color='lightblue', linewidth=3)
plt.scatter([0.3, 3.8, 1.2, 2.5], [11, 25, 9, 26], color='darkgreen', marker='^')
plt.xlim(0.5, 4.5) # Uses set_xlim internally.
plt.show()

# Each Axes has an x-axis and a y-axis, which contain ticks, which have major and minor ticklines and ticklabels. 
# There’s also the axis labels, title, and legend to consider when you want to customize your axes, 
# but also taking into account the axis scales and gridlines might come in handy.



# Creating a plot

# Import `pyplot`
import matplotlib.pyplot as plt

# Initialize a Figure 
fig = plt.figure()

# Add Axes to the Figure
fig.add_axes([0,0,1,1])


# Subplot -- but to make things a bit more complicated, you’ll sometimes see subplots pop up in code.
# You use subplots to set up and place your Axes on a regular grid.

# When you do call subplot to add Axes to your figure, do so with the add_subplots() function. 

# Import the necessary packages and modules
import matplotlib.pyplot as plt
import numpy as np

# Create a Figure
fig = plt.figure()

# Set up Axes
ax = fig.add_subplot(111)
#  111 -> 1, 1, 1
#  The three arguments designate the number of rows (1), the number of columns (1) and the plot number (1). So you actually make one subplot.

# Scatter the data
ax.scatter(np.linspace(0, 1, 5), np.linspace(0, 5, 5))

# Show the plot
plt.show()



# The difference between fig.add_axes() and fig.add_subplot() doesn’t lie in the result: they both return an Axes object.
#  However, they do differ in the mechanism that is used to add the axes: you pass a list to add_axes() which is the lower left point, 
#  the width and the height. This means that the axes object is positioned in absolute coordinates.

# add_subplot() function doesn’t provide the option to put the axes at a certain position.


# Import `pyplot` from `matplotlib`
import matplotlib.pyplot as plt

# Initialize the plot
fig = plt.figure(figsize=(20,10))
ax1 = fig.add_subplot(121)
ax2 = fig.add_subplot(122)

# or replace the three lines of code above by the following line: 
#fig, (ax1, ax2) = plt.subplots(1,2, figsize=(20,10))

# Plot the data
ax1.bar([1,2,3],[3,4,5])
ax2.barh([0.5,1,2.5],[0,1,2])

# Show the plot
plt.show()


# ax.bar()	Vertical rectangles
# ax.barh()	Horizontal rectangles
# ax.axhline()	Horizontal line across axes
# ax.vline()	Vertical line across axes
# ax.fill()	Filled polygons
# ax.fill_between()	Fill between y-values and 0
# ax.stackplot()	Stack plot


# Import `pyplot` from `matplotlib`
import matplotlib.pyplot as plt

# Initialize the plot
fig = plt.figure()
ax1 = fig.add_subplot(131)
ax2 = fig.add_subplot(132)
ax3 = fig.add_subplot(133)

# Plot the data
ax1.bar([1,2,3],[3,4,5])
ax2.barh([0.5,1,2.5],[0,1,2])
ax2.axhline(0.45)
ax1.axvline(0.65)
ax3.scatter(x,y)

# Show the plot
plt.show()


# ax.arrow()	Arrow
# ax.quiver()	2D field of arrows
# ax.streamplot()	2D vector fields
# ax.hist()	Histogram
# ax.boxplot()	Boxplot
# ax.violinplot()	Violinplot


# ax.pcolor()	Pseudocolor plot
# ax.pcolormesh()	Pseudocolor plot
# ax.contour()	Contour plot
# ax.contourf()	Filled contour plot
# ax.clabel()	Labeled contour plot


# Import `pyplot` from `matplotlib`
import matplotlib.pyplot as plt
import numpy as np

# Initialize the plot
fig = plt.figure()
ax1 = fig.add_subplot(131)
ax2 = fig.add_subplot(132)
ax3 = fig.add_subplot(133)

# Plot the data
ax1.bar([1,2,3],[3,4,5])
ax2.barh([0.5,1,2.5],[0,1,2])
ax2.axhline(0.45)
ax1.axvline(0.65)
ax3.scatter(np.linspace(0, 1, 5), np.linspace(0, 5, 5))

# Delete `ax3`
fig.delaxes(ax3)

# Show the plot
plt.show()




# Saving the plot

# Save Figure
plt.savefig("foo.png")

# Save Transparent Figure
plt.savefig("foo.png", transparent=True)




# Save as PDF

# Import PdfPages
from matplotlib.backends.backend_pdf import PdfPages

# Initialize the pdf file
pp = PdfPages('multipage.pdf')

# Save the figure to the file
pp.savefig()

# Close the file
pp.close()


















