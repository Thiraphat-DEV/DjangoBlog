from django.db import models

# Create your models here.

class Post(models.Model):
	categories_choice =  (
		("BlockChain", "BlockChain Technology"),
		("AI", "Technology"),
		("NFT", "NFT Technology"),
		("BACKEND", "BACKEND Technology"),
		("FRONTEND", "FRONTEND Technology"),
	)
	title = models.CharField(max_length=300)
	body = models.TextField()
	photo = models.ImageField(upload_to='blog/%Y/%m/%d', blank=True)
	category = models.CharField(max_length=50, choices=categories_choice)
	post_status = models.BooleanField(default=False)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def Meta():
		ordering = ['-created_at']
	def __str__(self):
		return self.title