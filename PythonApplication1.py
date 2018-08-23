
class Human (object):

	def __init__(self, *args, **kwargs):
		self.firstName = kwargs.setdefault('first')
		self.lastName = kwargs.setdefault('last')
		self.height = kwargs.setdefault('height')
		self.weight = kwargs.setdefault('weight')

	def bmi(self):
		return self.weight / float(self.height) ** 2
		Human.bmi = bmi

	def human_str(self):
		return '%s %s' % (self.firstName, self.lastName)
		Human.__str__ = human_str()

	def human_repr(self):
		return
		'''Human(%s='%s',%s='%s',%s=%s,%s=%s,)'''%(
			'first',self.firstName,
			'last',self.lastName,
			'height',self.height,
			'weight',self.weight
			)
		Human.__repr__ = human_repr
	
mechlty = Human(first='David', last='Gibson', weight=78, height=1.85)
matt = Human(first='Matt', last='Gibson', weight=88, height=1.85)

sis= Human(first='Ruth', last='Gibson')
baby_sis= Human(first='Ruth', last='Gibson')
print mechlty.__repr__(),baby_sis