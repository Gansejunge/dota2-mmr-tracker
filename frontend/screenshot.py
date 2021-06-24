from mss import mss, tools
from requests import request
from re import sub
from json import loads
from os import environ as environment
from os import remove

OCR_SPACE_API_URL = ''

def get_mmr_as_image():
	with mss() as sct:
		print("Taking screenshot")
		monitor = {"top": 206, "left": 1591, "width": 50, "height": 30}
		output = "mmr.png".format(**monitor)
		sct_img = sct.grab(monitor)
		tools.to_png(sct_img.rgb, sct_img.size, output=output)


def process_screenshot():
	get_mmr_as_image()
	payload = {'language': 'eng', 'isOverlayRequired': 'false',
	           'iscreatesearchablepdf': 'false', 'issearchablepdfhidetextlayer': 'false'}
	files = {'file': ("mmr.png", open("mmr.png", "rb"), 'image/png')}
	headers = {'apikey': environment['OCR_SPACE_API_KEY']}
	print("Uploading image")
	response = request("POST", OCR_SPACE_API_URL, headers=headers, data=payload, files=files)
	answer = loads(response.text.encode('utf8'))
	remove('mmr.png')
	return int(sub('[^0-9]+', '', answer['ParsedResults'][0]['ParsedText']))


if __name__ == '__main__':
	print(process_screenshot())
