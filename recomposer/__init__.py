import unicodedata
import re
import string
import sys

class Recomposer:
	def __init__(self):
		self.make_substitutions()

	def make_substitutions(self):
		self.substitutions = {}
		for i in range(1, 65535):
			char = unichr(i)
			decomposed = unicodedata.normalize('NFKD', char)
			if len(decomposed) > 1:
				result = re.match(r'^[A-z]+$', decomposed)
				if result:
					self.substitutions[decomposed] = char

	def process(self, instr):
		outstr = unicode(instr)
		for sub in sorted(self.substitutions.keys(), lambda x, y: len(y) - len(x)):
			if sub in outstr:
				outstr = string.replace(outstr, sub, self.substitutions[sub])
		return outstr

def main():
    r = Recomposer()
    for line in sys.stdin:
        print r.process(line)
