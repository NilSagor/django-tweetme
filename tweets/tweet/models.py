from django.db import models
from django.conf import settings
from django.urls import reverse
from .validators import validate_content

# Create your models here.
class Tweet(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, default = 1, on_delete = models.CASCADE)
	content = models.CharField(max_length=140, validators = [validate_content])
	updated = models.DateTimeField(auto_now = True)
	timestamp = models.DateTimeField(auto_now_add = True)

	def __str__(self):
		return self.content

	def get_absolute_url(self):
		return reverse("tweet:tweet-detail", kwargs={"pk":self.pk})