recomposer
==========
Uses Unicode compatibility/ligature characters to shorten strings containing the ASCII representations of those characters.

	>>> import recomposer
	>>> r = recomposer.Recomposer()
	>>> r.process("difficult")
	u'di\ufb03cult'
	>>> print r.process("difficult")
	diﬃcult
