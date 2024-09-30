from django.db import models

class Student(models.Model):
	sid = models.CharField(max_length=10)
	sname = models.CharField(max_length=50)
	semail = models.EmailField()
	scontact = models.CharField(max_length=10)

	class Meta:
		db_table = "student"

	def __str__(self):
		return self.sname