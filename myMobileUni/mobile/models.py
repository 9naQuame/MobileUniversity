class Course(models.Model):
	code = models.CharField(max_length = 10)
	name = models.CharField(max_length = 40)
	abbreviation = models.CharField(max_length = 10)

class Timetable(models.Model):
	examVenue = models.CharField(max_length = 10)
	examTime = models.DateField()
	lectureVenue = models.CharField(max_length = 10)
	lectureTime = models.DateField()
	semester = models.IntegerField()
	year = models.IntegerField()
	code = models.ForeignKey(Course)
	major = models.ForeignKey(Major)

class Major(models.Model):
	faculty = models.CharField(max_length = 60)
	department = models.CharField(max_length = 60)
	majors = models.CharField(max_length = 60)


	
	
	
	















