import cv2

# Membuka video dari file atau kamera
# Untuk membuka video dari file, ganti 'path/to/your/video.mp4' dengan jalur file video
video_capture = cv2.VideoCapture('path/to/your/video.mp4')

while True:
    # Membaca frame dari video
    ret, frame = video_capture.read()

    # Jika frame berhasil dibaca
    if not ret:
        break

    # Menampilkan frame
    cv2.imshow('Video', frame)

    # Menunggu 1 ms dan memeriksa jika tombol 'q' ditekan
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Menutup video capture dan jendela
video_capture.release()
cv2.destroyAllWindows()
