
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

mechlty = Human(first='David', last='Gibson', weight=78, height=1.85)
matt = Human(first='Matt', last='Gibson', weight=88, height=1.85)
print matt
msg = 'studies have shown that BMI is not indaicative of health'
def well():
    return msg
oldBmi= mechlty.bmi
mechlty.bmi = well
 
mechlty.bmi = matt.bmi

print str(matt),matt.bmi()
print str(mechlty),mechlty.bmi()
