from django.contrib import admin
from .models import Post
# Register your models here.
# control object with @ 
@admin.register(Post)

class PostAdmin(admin.ModelAdmin):
	list_display = ['title', 'category', 'post_status','created_at','updated_at']
	list_filter = ['category', 'post_status']
	list_editable= ['category', 'post_status']