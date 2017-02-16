import random
import urllib

def download_web_image(url):
	name = random.randrange(1, 1000)
	full_name = str(name) + ".jpg"
	urllib.urlopen(url, full_name)

download_web_image("https://nagkumar.com/wp-content/uploads/2016/09/Logomakr_3Xl7WB-1-e1473906195360.png")