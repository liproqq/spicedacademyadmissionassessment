import csv
import matplotlib.pyplot as plotter
import numpy as numpy


#variables to store datapoints
xValues = []
yValues = []

#returns MSE
def MSE(y,yTrue):
    return numpy.square(numpy.subtract(yTrue,y)).mean()

def calcYLine():
    return slope*xLine+intercept



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
slope = 1 #Task states slope as 10 which would result in 10 being the lowest value for MSE
intercept = 0
xLine = numpy.linspace(min(xValues),max(xValues),len(xValues))

finalMSE = MSE(calcYLine(),yValues)


for loop in range(100):
    slope += 0.1
    tmpMSE = MSE(calcYLine(),yValues)
    if finalMSE>tmpMSE:
        finalMSE=tmpMSE
        finalSlope=slope



print(f'The final value for a is: {finalSlope}\nThe final value for MSE is: {finalMSE}')
