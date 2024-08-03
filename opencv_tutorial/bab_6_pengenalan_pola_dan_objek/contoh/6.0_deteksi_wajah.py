import cv2

# Memuat classifier Haar Cascade untuk deteksi wajah
# Pastikan file 'haarcascade_frontalface_default.xml' berada di jalur yang benar
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Membaca gambar dari file
image = cv2.imread('path/to/your/image.jpg')

# Mengonversi gambar ke grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Mendeteksi wajah dalam gambar
# Gantilah 1.3 dan 5 dengan parameter scaleFactor dan minNeighbors yang sesuai
faces = face_cascade.detectMultiScale(gray_image, scaleFactor=1.3, minNeighbors=5)

# Menggambar kotak di sekitar wajah yang terdeteksi
for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)

# Menyimpan gambar hasil deteksi wajah
cv2.imwrite('path/to/save/detected_faces.jpg', image)

# Menampilkan gambar hasil deteksi wajah
cv2.imshow('Detected Faces', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
