from django.contrib import admin
from .models import Post,Comment,Profile
# Register your models here.

class Post_admin(admin.ModelAdmin):
    list_display=[ 'title','content','author','created_at','updated_at']

class Comment_admin(admin.ModelAdmin):
    list_display=['post','author','content','created_at']
class Profile_admin(admin.ModelAdmin):
    list_display=['user','image']

admin.site.register(Post,Post_admin)
admin.site.register(Comment,Comment_admin)
admin.site.register(Profile,Profile_admin)