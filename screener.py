import numpy as np
import pyautogui
import imutils
import cv2
import os
# from screeninfo import get_monitors 
# for m in get_monitors(): 
# 	print(str(m))


class Screener():
	# """docstring for Screener"""
	# def __init__(self, arg):
	# 	super(Screener, self).__init__()
	# 	self.arg = arg

	def get(self):
		screen = os.popen("xrandr -q -d :0").readlines()[0]
		screen = screen.split(",")[1].replace("current", "").split("x")
		curent_screen = {"width": int(screen[0]), "height": int(screen[1])}
		image = pyautogui.screenshot(region=(0,0, curent_screen["width"], curent_screen["height"]))
		image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)

		self.image = image
		return self.image

	def createLight(self, top_horizont, bottom_horizont, left_vertical, right_vertical):
		
		print curent_screen
		print image[1079]





		# cv2.imshow("Screenshot", imutils.resize(image, width=600))
		# # cv2.waitKey(5000)
		# cv2.imwrite("pic.png", image)

screener = Screener()

screener.get()	