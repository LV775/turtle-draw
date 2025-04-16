# Turtle Draw
#
# By: Lucas Vasquez
#


print ("Turtle Draw")
TurtleDrawDataFileName = "turtle-draw-lv.txt"

TurtleDrawDataFile = open(TurtleDrawDataFileName, 'r')
DataFileLine = TurtleDrawDataFile.readline()

while DataFileLine:
	print(DataFileLine, end='')
	DataFileLine = TurtleDrawDataFile.readline()

print('End')