# This program will asking the working directory to 
# rename image files in ordering path. 
import os
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
	print('Success rename : {:>3}'.format(success))
	print('Fail to rename : {:>3}'.format(target-success))

	
def Rename(file):
	global success

	height, width = getHW(file)
	try:
		os.rename(file, f'{width}x{height}{os.path.splitext(file)[-1]}')
		success += 1
		print(f'{file}改名成功')
	except FileExistsError:
		i = 1
		while True:
			try:
				os.rename(file, f'{width}x{height} ({i}){os.path.splitext(file)[-1]}')
				success += 1
				print(f'{file}改名成功')
				break
			except FileExistsError: 
				i += 1
	except Exception as e:
		show_err(e)


def main():
	global success, target

	changePath = input('input the working path: ')
	os.chdir(changePath)

	for file in os.listdir():
		if file.endswith('png') or file.endswith('jpg'):
			target += 1
			try: Rename(file)
			except: pass
	summary()


if __name__ == '__main__':
	main()