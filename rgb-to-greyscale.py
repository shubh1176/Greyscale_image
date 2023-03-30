from PIL import Image

img = Image.open('test.jpg')
imgGray = img.convert('L')
imgGray.save('test_gray.jpg')