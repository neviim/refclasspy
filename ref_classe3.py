#!/usr/bin/env python
# -*- coding: utf-8 -*-

# --- __dict__ e __slots__
class myClass(object):
	#
    __slots__ = ('x', 'y', '__dict__')
    x = 10

    def __init__(self, *args, **kwargs):
       self.y = 2


# --- uso da classe
#
minhaClasse1 = myClass()

print "Classe, valor (x = 10) em __slots__ , valor (y = 2) em __dict__"
print
print minhaClasse1.__dict__
print minhaClasse1.__slots__
print
print minhaClasse1.x
print minhaClasse1.y
print


print "Classe, alterando (x) de __slots__ para valor 100"
minhaClasse1.x = 100
minhaClasse1.y = 200

print minhaClasse1.__dict__
print minhaClasse1.__slots__
print
print minhaClasse1.x
print minhaClasse1.y
print 
