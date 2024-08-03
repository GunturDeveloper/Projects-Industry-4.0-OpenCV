import cv2

# Membaca gambar dari file
image = cv2.imread('path/to/your/image.jpg')

# Menyimpan gambar ke file baru
cv2.imwrite('path/to/save/your/image.jpg', image)
