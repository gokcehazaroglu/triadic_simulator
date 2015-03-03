class Agent(object):
	"""docstring for Agent"""
	def __init__(self, *args,**kwargs):
		#super(Agent, self).__init__()
		#self.arg = arg
		attr=['money','num_turns','name']
		itr=iter(attr)

		for i in args:
			setattr(self,next(itr),i)

		for i in kwargs.keys():
			if i in attr:
				setattr(self,i,kwargs[i])

		if not hasattr(self,'money'):
			self.money=0
		if not hasattr(self,'num_turns'):
			self.num_turns=0
		if not hasattr(self,'name'):
			self.name='Agent'

	def __str__(self):
		return 'Money: '+str(self.money)+'\nnum_turns: '+str(self.num_turns)+'\nName: '+self.name

