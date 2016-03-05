import matplotlib.pyplot as plt
import csv
import matplotlib.pyplot as pyplot
import numpy as np

#defines lists
year = [1, 2]
budget = [1, 2]

#function designed to convert y value into visual color representation
def rgbToHex (y):
    if 2.25 > y:
        variable = 113.4 * y
        return '#%02x%02x%02x' % (255, variable, 0)
    elif 2.25 < y:
        variable = 573.75 / y
        return '#%02x%02x%02x' % (variable, 255, 0)
        print (variable)
    
'''
#opens file and reads columns and rows into year and budget lists
with open('input.txt', 'rb') as f:
    reader = csv.reader(f, delimiter=' ')
    for row in reader:
        #year.append(int(row[1]))
        #budget.append(int(row[2]))
'''

with open('input.txt') as f:
    array = []
    w, h = [float(x) for x in f.readline().split()] # read first line
    array.append([float(x) for x in f.readline().split()])
    i = 0
    #plots the first bar
    plt.bar(array[i][0], array[i][1], color = rgbToHex(array[i][1]))
    for line in f: # read rest of lines
        array.append([float(x) for x in line.split()])
        #plots the rest
        plt.bar(array[i][0], array[i][1], color = rgbToHex(array[i][1]))
        i += 1
    for p in array: print p
    plt.bar(array[i][0], array[i][1], color = rgbToHex(array[i][1]))



#defines a list
x = [5,7,9]
y = [5,7,9]

#second plot
x2 = [2, 5, 6]
y2 = [3, 5, 8]

'''
#plots lines with legend ()
plt.plot(x, y, label = 'first line');
plt.plot(x2, y2, label = 'second line');
'''

#adds labels to the graph
plt.xlabel('Year')
plt.ylabel('Percentage of Federal Budget')

#adds a title
plt.title("NASA Budget by Year");

#sets limits for the years
pyplot.xlim(1958, 2016)

#sets tick frequency for the respective axis
#plt.ticks(np.arrange(xmin, xmax, interval))
plt.xticks(np.arange(1960, 2016, 5.0))
plt.yticks(np.arange(0.0, 5.0, 0.5))

#draws/renders graph
plt.show()

