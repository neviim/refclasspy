#!/usr/bin/env python
# -*- coding: utf-8 -*-

# --- __dict__
class myClass(object):
	#
	def __init__(self, *args, **kwargs):
    	# inicializando os parametros.
		self.x = 1
		self.y = 2
		self.c = 3


# --- uso da classe
#
minhaClasse1 = myClass()
minhaClasse2 = myClass()

print "minhaClasse1"
print
print minhaClasse1.__dict__
print minhaClasse1.x
print minhaClasse1.y
print minhaClasse1.c
print


