from pymel.core import *
Allobj = {}

def store():
	for o in ls():
		Allobj[o] = o.name()
	print Allobj

