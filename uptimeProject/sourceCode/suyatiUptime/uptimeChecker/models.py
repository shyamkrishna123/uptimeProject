from django.db import models
from django.utils import timezone

# Create your models here.
class addServer(models.Model):
	user = models.ForeignKey('auth.User')
	server = models.CharField(max_length=200)
	details = models.TextField()
	ipAddress = models.CharField(max_length=200)
	created_date = models.DateTimeField(default=timezone.now)
	deployed_date = models.DateTimeField(blank=True, null=True)

	def creation(self):
		self.created_date = timezone.now()
		self.save()

	def __str__(self):
		return self.server