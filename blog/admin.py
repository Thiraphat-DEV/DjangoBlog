from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Post
# Register your models here.
# control object with @ 
@admin.register(Post)

class PostAdmin(SummernoteModelAdmin):
	list_display = ['title', 'category', 'post_status','created_at','updated_at']
	list_filter = ['category', 'post_status']
	list_editable= ['category', 'post_status']
	summernote_fields = ('body', )