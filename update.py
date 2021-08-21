# This program will asking the working directory to 
# move image files into another path. Finally, the 
# ini file is updated.
import os
import json
import shutil
import configparser as cp
import matplotlib.image as mpimg

def getHW(file):
	height, width, depth = mpimg.imread( os.path.abspath(file), 0 ).shape
	return height, width


def show_err(err, i=[1]):
	print(f'Error{i[0]}')
	print(f'----------\n{e}\n----------')
	i[0] += 1


target = 0
success = 0

def summary():
	global success, target

	print('***Work completed***')
	print('Success update : {:>3}'.format(success))
	print('Fail to update : {:>3}'.format(target-success))


imgDict = {}

def readINI(cpfile):
	global imgDict

	config = cp.ConfigParser()
	with open(cpfile, 'r') as configfile:
		config.read_file(configfile)
	if not imgDict:
		imgDict = json.loads( config['Data']['json'] )

	return config


def Rename(file, ref_path):
	global success, imgDict

	height, width = getHW(file)
	name = f'{width}x{height}'
	if name in imgDict:
		i = imgDict[name]
		new_name = f'{width}x{height} ({i}){os.path.splitext(file)[-1]}'
		imgDict[name] += 1
	else:
		new_name = f'{width}x{height}{os.path.splitext(file)[-1]}'
		imgDict[name] = 1

	os.rename(file, new_name)
	shutil.move( os.path.abspath(new_name), ref_path + '/' + new_name )
	success += 1
	print(f'{file}移動成功')


def updateINI(cpfile):
	global imgDict

	config = readINI(cpfile)
	config['Data']['json'] = json.dumps(imgDict)
	with open(cpfile, 'w') as configfile:
		config.write(configfile)


def main():
	global success, target, imgDict

	changePath = input('input the working path: ')
	os.chdir(changePath)

	intoPath = input('input the moving path: ')
	cpfile = intoPath + '/' + 'image.ini'
	readINI(cpfile)

	for file in os.listdir():
		if file.endswith('png') or file.endswith('jpg'):
			target += 1
			try: Rename(file, intoPath)
			except: pass

	updateINI(cpfile)
	summary()


if __name__ == '__main__':
	main()