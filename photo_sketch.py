import cv2 as cv

# read the image
img = cv.imread(r"C:\Programming\Open CV\Image.png")

# resize the image
img = cv.resize(img, (500, 300))

# convert to gray scale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# invert the gray image
inverted = cv.bitwise_not(gray)

# guasssian blur
blur = cv.GaussianBlur(inverted, (21, 21), 0)

# invert the blurred image
inverted_blur = cv.bitwise_not(blur)

# create the pencil sketch image
sketch = cv.divide(gray, inverted_blur, scale=256.0)

# Show results
cv.imshow("Original Image", img)
cv.imshow("Pencil Sketch", sketch)
cv.waitKey(0)
cv.destroyAllWindows()

# Save the output
cv.imwrite("sketch_output.jpg", sketch)