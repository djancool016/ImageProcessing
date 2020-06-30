import numpy as np
import cv2

def convolve(image, kernel):
	# i = image size 
	# k = kernel size
	(iH, iW) = image.shape[:2]
	(kH, kW) = kernel.shape[:2]
	
	# "pad" digunakan untuk menambah border
	# .BORDER_ digunakan untuk duplicat pixel terakhir menjadi border
	pad = (kW - 1) // 2
	image = cv2.copyMakeBorder(image, pad, pad, pad, pad,
		cv2.BORDER_WRAP) 
	print("Citra Awal + WRAP Border : \n\n",image, "\n")
	
	# output = matrix kosong dengan ukuran image
	output = np.zeros((iH, iW), dtype="float32")

	# loop mengubah tiap pixel sesuai dengan kernel tiap koordinat x dan y pada image dari kiri ke kana dan atas ke bawah
	for y in np.arange(pad, iH + pad):
		for x in np.arange(pad, iW + pad):

			# Menentuka ROI dari image dengan mengambil titik tengah dari koordinat saat ini(roi)
			roi = image[y - pad:y + pad + 1, x - pad:x + pad + 1]

			# Implementasi konvulsi dengan perkalian elemen matrix roi*kernel dan menjumlah tuap elemennya
			k = (roi * kernel).sum()
			# Memasukkan hasil konvulsi (k) ke dalam matrix output sesuai koordinat (x,y)
			output[y - pad, x - pad] = k
			
			
	print("Citra Baru : \n\n",output, "\n")
	cv2.imwrite("test3.jpg",output) 

image = np.array([
    [200, 180, 130, 90, 80],
    [180, 200, 200, 170, 100],
    [100, 210, 280, 150, 120]
	])

kernel = np.array((
	[-1, 0, 1],
	[-4, 0, 4],
	[-1, 0, 1]), dtype="float32")


print("\nCitra Awal Matrix (5X3) : \n\n",image, "\n")
print("Kernel Konvulsi (3X3) : \n\n",kernel, "\n")
convolve(image,kernel)