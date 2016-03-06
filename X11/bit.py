'Utility for enumerating integers and naming bitmask fields'


class enum:
	def __init__(self, n, i=1, s=0, t=int):
		for a in n.split():
			if a is not '.':
				setattr(self, a, t(s))
			s += i
			self.last = s
		
	def name(self, n):
		a = self.__dict__
		d = dict((a[k], k) for k in a)
		return d[n] if n in d else n
		
	@property
	def items(self):
		d = self.__dict__
		for k in d:
			yield d[k]


class mask:
	def __init__(self, n, i=1, s=0):
		for a in n.split():
			if a is not '.':
				setattr(self, a, i << s)
			s += i

	def __call__(self, n):
		m = 0
		for a in n.split():
			m |= getattr(self, a)
		return m
		
	def name(self, n):
		a = self.__dict__
		d = dict((a[k], k) for k in a)
		return d[n] if n in d else n

	@property
	def items(self):
		d = self.__dict__
		for k in d:
			yield d[k]

	@property
	def every(self):
		m = 0
		for a in self.items:
			m |= a
		return m

