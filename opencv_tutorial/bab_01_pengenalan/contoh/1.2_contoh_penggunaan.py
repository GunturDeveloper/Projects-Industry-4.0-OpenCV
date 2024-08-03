import cv2

# Membaca gambar
image = cv2.imread('path/to/your/image.jpg')

# Menampilkan gambar
cv2.imshow('Image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
