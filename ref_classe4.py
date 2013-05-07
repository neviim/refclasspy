#!/usr/bin/env python
# -*- coding: utf-8 -*-

# __iter__ e next
class Iter(object):
	#
    def __init__(self, until):
        self.i = 0
        self.until = until
    #    
    def __iter__(self):
        return self
    #    
    def next(self):
        if self.i != self.until:
           self.i += 1
           return self.i
        else:
           raise StopIteration


# --- uso da classe
#
print "Classe Iter, realiza uma contagem incremental de 2 em 2, pelo metodo next()"
item = Iter(10)

# imprime passo a passo 
print
print item.next() # retorna 1
print item.next() # retorna 2
print item.next() # retorna 3
print

# continua a imprimir de onde paro.
print "inicia o for de onde paro o item.next(), dando continuidade ao incremento de 2 em 2 até 10"
#
for i in item:
	print i

print
