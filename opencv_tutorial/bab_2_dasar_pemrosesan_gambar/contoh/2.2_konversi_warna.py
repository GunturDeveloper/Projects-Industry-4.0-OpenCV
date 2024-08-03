import cv2

# Membaca gambar dari file
image = cv2.imread('path/to/your/image.jpg')

# Mengkonversi gambar ke grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Menyimpan gambar grayscale
cv2.imwrite('path/to/save/gray_image.jpg', gray_image)
