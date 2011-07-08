class event(models.Model):
	title = models.CharField(max_length=100)
	body = models.TextField()
	venue = models.TextField()
	time = models.DateTimeField(auto_now_add=True)
	rate = models.DecimalField(max_digits=10, decimal_places=2)
	organisers = models.TextField()
	approval = models.BooleanField()
	eventtype = models.BooleanField()
	status = models.CharField(max_length=10)
	def __unicode__(self):
		return self.title

class news(models.Model):
	title = models.CharField(max_length=100)
	body = models.TextField()
	created = models.DateField(auto_now_add=True)
	updated = models.DateField(auto_now=True)
	author = models.CharField(max_length=50)
	def __unicode__(self):
		return self.title

class announcement(models.Model):
	title = models.CharField(max_length=100)
	body = models.TextField()
	created = models.DateField(auto_now_add=True)
	updated = models.DateField(auto_now=True)
	def __unicode__(self):
		return self.title
