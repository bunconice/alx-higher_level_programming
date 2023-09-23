#!/usr/bin/python3
if __name__ == "__main__":
	import sys
	size = len(sys.argv)
	if size == 1:
		print(size - 1, "Arguments.")
	elif size == 2:
		print(size - 1, "Argument:")
	else:
		print(size - 1, "Arguments:")
	for i in range(1, size):
		print(i, ": ", sys.argv[i], sep="")
