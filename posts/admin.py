from django.contrib import admin
from .models import Post, Entry

class PostAdmin(admin.ModelAdmin):
   list_display = ('title', 'user', 'published_date')

admin.site.register(Post, PostAdmin)


class EntryAdmin(admin.ModelAdmin):
   list_display = ('user', 'body', 'date_posted')
   
admin.site.register(Entry, EntryAdmin)