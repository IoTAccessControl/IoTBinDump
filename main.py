# coding: utf-8
# created at 9/1/2022
__author__ = "fripSide"

import os
import sys

BLOCK_SIZE = 2048
ECC_SIZE = 64


def remove_ecc(src, dst):
	block_size = BLOCK_SIZE
	ecc_size = ECC_SIZE
	raw_image = open(src, "rb")
	new_image = open(dst, "wb")
	size = os.path.getsize(src)
	print(f"{src} size: ", size, "save to: ", dst)
	i = 0
	while i <= size:
		raw_image.seek(i)
		temp = raw_image.read(block_size)
		new_image.write(temp)
		i = i + block_size + ecc_size
	new_image.close()
	new_image.close()


def main():
	if len(sys.argv) < 3:
		print("Usage: remvoe_ecc.py image.bin new_image.bin")
		sys.exit(1)
	src = sys.argv[1]
	dst = sys.argv[2]
	remove_ecc(src, dst)


if __name__ == "__main__":
	main()
