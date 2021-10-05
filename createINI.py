# This program will asking the working directory to
# parse image files in ordering path and create ini
# file for further usage.
import configparser as cp
import os
import json

def create(path):
	config = cp.ConfigParser()
	config['Data'] = {}
	config['Data']['path'] = os.path.abspath(path)
	config['Data']['json'] = getJson(path)
	with open('image.ini', 'w') as configfile:
		configfile.write('# This file stores the path and serialized json obj.\n\n')
		config.write(configfile)
	print("\nimage.ini file is successfully created.")

def getJson(path):
	imgDict = {}
	for file in os.listdir():
		if file.endswith('.png') or file.endswith('.jpg'):
			name = os.path.splitext(file)[0].split(' ')[0]
			if name in imgDict:
				imgDict[name] += 1
			else:
				imgDict[name] = 1
	return json.dumps(imgDict)

def main():
	changePath = input('input the working path: ')
	os.chdir(changePath)
	create(os.getcwd())

if __name__ == '__main__':
	main()
