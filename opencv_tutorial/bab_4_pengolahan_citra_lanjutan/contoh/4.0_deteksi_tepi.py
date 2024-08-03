import cv2

# Membaca gambar dari file
image = cv2.imread('path/to/your/image.jpg')

# Mengonversi gambar ke grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Menerapkan deteksi tepi menggunakan operator Canny
# Gantilah 100 dan 200 dengan nilai threshold yang sesuai
edges = cv2.Canny(gray_image, 100, 200)

# Menyimpan gambar hasil deteksi tepi
cv2.imwrite('path/to/save/edges_image.jpg', edges)

# Menampilkan gambar hasil deteksi tepi
cv2.imshow('Edges Image', edges)
cv2.waitKey(0)
cv2.destroyAllWindows()
