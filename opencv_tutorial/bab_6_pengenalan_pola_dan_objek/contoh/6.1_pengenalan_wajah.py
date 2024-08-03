import cv2

# Memuat classifier Haar Cascade untuk deteksi wajah
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Memuat model LBPH untuk pengenalan wajah
recognizer = cv2.face.LBPHFaceRecognizer_create()

# Melatih model dengan gambar wajah
# Pastikan Anda telah mempersiapkan dataset wajah untuk pelatihan
# Berikut adalah contoh memuat dataset dan melatih model
def train_model():
    faces = []
    labels = []
    # Gantilah 'path/to/your/faces/' dengan jalur ke direktori dataset wajah
    for i in range(1, 11):  # Misalkan ada 10 gambar per orang
        img_path = f'path/to/your/faces/person_{i}.jpg'
        img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
        faces.append(img)
        labels.append(i)  # Label untuk orang ke-i
    recognizer.train(faces, np.array(labels))

train_model()

# Membaca gambar dari file
image = cv2.imread('path/to/your/image.jpg')
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Mendeteksi wajah dalam gambar
faces = face_cascade.detectMultiScale(gray_image, scaleFactor=1.3, minNeighbors=5)

# Mengidentifikasi wajah yang terdeteksi
for (x, y, w, h) in faces:
    face = gray_image[y:y + h, x:x + w]
    label, confidence = recognizer.predict(face)
    cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)
    cv2.putText(image, f'ID: {label}', (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

# Menyimpan gambar hasil pengenalan wajah
cv2.imwrite('path/to/save/recognized_faces.jpg', image)

# Menampilkan gambar hasil pengenalan wajah
cv2.imshow('Recognized Faces', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
