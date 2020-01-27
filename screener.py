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
		self.curent_screen = curent_screen
		return self.image

	def createLight(self, top_horizont, bottom_horizont, left_vertical, right_vertical, width):
			

		top_horizont_led_count = self.curent_screen["width"]//top_horizont
		top_horizont_led_left = self.curent_screen["width"]%top_horizont

		top_led = []
		current_led = 1
		while current_led <= top_horizont_led_count :
			red = 0
			green = 0
			blue = 0
			pixel_count = 0
			for x in range(top_horizont_led_count) :
				for y in range(width) :
					pixel_count += 1
					red += self.image[y][x][0]
					green += self.image[y][x][1]
					blue += self.image[y][x][2]


			top_led.append([red//pixel_count, green//pixel_count, blue//pixel_count]) 
			current_led +=1


		# for y in range(top_horizont_led) :
		# 	for y in range(width) :



		# print top_led
		# print top_horizont_led_count, "  ", top_horizont_led_left

		# print self.curent_screen
		# print self.image[1079]





		# cv2.imshow("Screenshot", imutils.resize(image, width=600))
		# # cv2.waitKey(5000)
		# cv2.imwrite("pic.png", image)

screener = Screener()

screener.get()	
screener.createLight(13, 13, 13, 13, 15)