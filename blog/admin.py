from django.contrib import admin
from .models import Post
from django.utils.safestring import mark_safe

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id','title','text_size','created_date','published_date','author']


    def text_size(self, post):
        return mark_safe('<strong>{}글자</strong>'.format(len(post.text)))

