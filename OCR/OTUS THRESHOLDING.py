import cv2
import  matplotlib.pyplot as plt

def main():
    img = cv2.imread('venv/pp.png',0)
    th = 0
    max_val = 255
    ret, o1 = cv2.threshold(img, th , max_val ,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    ret, o2 = cv2.threshold(img, th , max_val ,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
    ret, o3 = cv2.threshold(img, th , max_val ,cv2.THRESH_TOZERO+cv2.THRESH_OTSU)
    ret, o4 = cv2.threshold(img, th , max_val ,cv2.THRESH_TOZERO_INV+cv2.THRESH_OTSU)
    ret, o5 = cv2.threshold(img, th, max_val, cv2.THRESH_TRUNC+cv2.THRESH_OTSU)
    output = [img,o1,o2,o3,o4,o5]
    titles = ['Original', 'Binary', 'Binary Inv',
              'Zero', 'Zero Inv', 'Trunc']
    for i in range(6):
        plt.subplot(2, 3, i+1)
        plt.imshow(output[i],cmap='gray')
        plt.title(titles[i])
        plt.xticks([])
        plt.yticks([])
        plt.show()
if __name__ == "__main__":
     main()
