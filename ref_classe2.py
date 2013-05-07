#!/usr/bin/env python
# -*- coding: utf-8 -*-

# --- __slots__
class myClass(object):
	#
	__slots__ = ('x', 'y') # definindo o slots.

	def __init__(self, *args, **kwargs):
    	# inicializando os parametros.
		self.x = 1
		self.y = 2


# --- uso da classe
#
minhaClasse1 = myClass()

print "minhaClasse1"
print
print minhaClasse1.__slots__
print minhaClasse1.x
print minhaClasse1.y
print