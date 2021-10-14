import cv2
from skimage import measure


img1 = cv2.imread('1.png')
img2 = cv2.imread('2.png')
score = measure.compare_ssim(img1,img2,multichannel=True)
print(score)
