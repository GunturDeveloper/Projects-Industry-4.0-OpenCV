import cv2
import numpy as np

# Membaca gambar dari file
image = cv2.imread('path/to/your/image.jpg')

# Mendapatkan dimensi gambar
(h, w) = image.shape[:2]

# --- Rotasi Gambar ---

# Menentukan pusat rotasi dan sudut rotasi
center = (w // 2, h // 2)
angle = 45  # Sudut rotasi dalam derajat
scale = 1.0  # Skala

# Membuat matriks transformasi rotasi
M_rot = cv2.getRotationMatrix2D(center, angle, scale)

# Menerapkan rotasi pada gambar
rotated_image = cv2.warpAffine(image, M_rot, (w, h))

# Menyimpan gambar yang telah dirotasi
cv2.imwrite('path/to/save/rotated_image.jpg', rotated_image)

# Menampilkan gambar yang telah dirotasi
cv2.imshow('Rotated Image', rotated_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# --- Translasi Gambar ---

# Menentukan offset translasi
tx = 100  # Translasi horizontal
ty = 50   # Translasi vertical

# Membuat matriks transformasi translasi
M_trans = np.float32([[1, 0, tx], [0, 1, ty]])

# Menerapkan translasi pada gambar
translated_image = cv2.warpAffine(image, M_trans, (w, h))

# Menyimpan gambar yang telah ditranslasi
cv2.imwrite('path/to/save/translated_image.jpg', translated_image)

# Menampilkan gambar yang telah ditranslasi
cv2.imshow('Translated Image', translated_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
