import csv
import matplotlib.pyplot as plotter
import numpy as numpy


#variables to store datapoints
xValues = []
yValues = []

with open("datapoints.csv") as datapointsFile:
    datapoints = csv.reader(datapointsFile, delimiter=',')
    #storing datapoints to list filtering non-floats
    for x,y in datapoints:
        try:
            xValues.append(float(x))
            yValues.append(float(y))
        except ValueError:
            next

#variables for the straight line
slope = 10
intercept = 0
xLine = numpy.linspace(min(xValues),max(xValues),len(xValues))
yLine = slope*xLine+intercept


plotter.scatter(xValues, yValues) #scatter plot from csv
plotter.plot(xLine,yLine) #plot straight line

MSE = numpy.square(numpy.subtract(yValues,yLine)).mean()

print(MSE)

plotter.show()
