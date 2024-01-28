import matplotlib.pyplot as plt
from PIL import Image

#image goes here
filename = "Cube.jpg"
#filename = "Gradient.jpg"
#filename = "Gradient.png"

img = Image.open(filename)

# Creating the graph
yAxisRed = [0] * 256
yAxisGreen = [0] * 256
yAxisBlue = [0] * 256

xAxis = [0] * 256
for Loop in range(256):
	xAxis[Loop] = Loop
#for Loop in range



# Going through the image
for x in range(img.size[0]):
	for y in range(img.size[1]):
		red, green, blue = img.getpixel((x, y))
		yAxisRed[red] = yAxisRed[red] + 1
		yAxisGreen[green] = yAxisGreen[green] + 1
		yAxisBlue[blue] = yAxisBlue[blue] + 1
	#for y in range
#for x in range

img.show()


# Plotting the graph

plot1 = plt.subplot2grid((3, 1), (0, 0))
plot2 = plt.subplot2grid((3, 1), (1, 0)) 
plot3 = plt.subplot2grid((3, 1), (2, 0))


plot1.bar(xAxis, yAxisRed, color='red')

plot2.bar(xAxis, yAxisGreen, color='green')

plot3.bar(xAxis, yAxisBlue, color='blue')

plot1.set_title("Fourier transformation of the image in RGB subpixels")
plt.xlabel("Value of the subpixel (0 to 255)")
plot2.set_ylabel("Amount of subpixels")
plt.show()

