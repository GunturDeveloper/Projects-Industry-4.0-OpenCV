import cv2

# Membaca gambar dari file
image = cv2.imread('path/to/your/image.jpg')

# Menerapkan pengaburan Gaussian pada gambar
# Gantilah (15, 15) dengan ukuran kernel yang sesuai
blurred_image = cv2.GaussianBlur(image, (15, 15), 0)

# Menyimpan gambar hasil pengaburan
cv2.imwrite('path/to/save/blurred_image.jpg', blurred_image)

# Menampilkan gambar hasil pengaburan
cv2.imshow('Blurred Image', blurred_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
