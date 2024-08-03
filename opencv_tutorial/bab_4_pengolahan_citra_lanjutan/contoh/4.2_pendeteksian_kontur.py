import cv2

# Membaca gambar dari file
image = cv2.imread('path/to/your/image.jpg')

# Mengonversi gambar ke grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Menerapkan deteksi tepi menggunakan operator Canny
edges = cv2.Canny(gray_image, 100, 200)

# Mendeteksi kontur dalam gambar
contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Menggambar kontur pada gambar asli
contour_image = image.copy()
cv2.drawContours(contour_image, contours, -1, (0, 255, 0), 2)

# Menyimpan gambar hasil pendeteksian kontur
cv2.imwrite('path/to/save/contour_image.jpg', contour_image)

# Menampilkan gambar hasil pendeteksian kontur
cv2.imshow('Contour Image', contour_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
