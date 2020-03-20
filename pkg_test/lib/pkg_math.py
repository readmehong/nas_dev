#!/usr/bin/env python
#!-*- coding: utf-8 -*-


class MathClass():
	def __init__(self):
		print('ini MathClass')

	def sum(self, m1, m2):
		rst = m1 + m2
		return rst

def main():
	print('test')
	obj = MathClass()
	print(obj.sum(1,2))

if __name__== '__main__':
	main()
