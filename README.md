recomposer
==========
Uses Unicode compatibility/ligature characters to shorten strings containing the ASCII representations of those characters.

	>>> from recomposer import *
	>>> r = Recomposer()
	>>> r.process("difficult")
	u'di\ufb03cult'
	>>> print r.process("difficult")
	diﬃcult
