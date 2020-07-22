from django.contrib import admin
from app01 import models

class Author(admin.ModelAdmin):
    list_display=('name','age','au_detail_id',)
    search_fields = ('name',)
    fieldsets = (
            ['Main',{
                'classes':(),
                'fields' : ('name','age'),
                }],
            ['Advance',{
                'classes':('collapse',),
                'fields':('au_detail_id',), 
                }] 
            )

admin.site.register(models.Author,Author)
class Publish(admin.ModelAdmin):
    list_display=('name','city','email')
admin.site.register(models.Publish,Publish)    
admin.site.register([models.Book,models.AuthorDetail])
