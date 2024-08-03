import cv2

# Membaca gambar dari file
image = cv2.imread('path/to/your/image.jpg')

# Menentukan area yang akan dipotong
# Gantilah (y1, y2, x1, x2) dengan koordinat yang diinginkan
cropped_image = image[y1:y2, x1:x2]

# Menyimpan gambar yang telah dipotong
cv2.imwrite('path/to/save/cropped_image.jpg', cropped_image)

# Menampilkan gambar yang telah dipotong
cv2.imshow('Cropped Image', cropped_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
