def main():
	try:
		open('config.txt')
	except FileNotFoundError:
		print("Couldn't find the config.txt file!")
	except IsADirectoryError:
		print("Found config.txt but it is a directory, couldn't read it")
	except PermissionError:
		print("Found config.txtx but we don't have permissions to open it")
	except (BlockingIOError, TimeoutError):
		print("Filesystem under heavy load, can't complete reading configuration file")

if __name__ == '__main__':
	main()