#!/usr/bin/env python
#!-*- coding: utf-8 -*-
import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(os.path.curdir))))

def main():

	from pkg_test.lib import pkg_math
	
	obj = pkg_math.MathClass()
	rst = obj.sum(1,2)
	print(rst)


if __name__== '__main__':
	main()
