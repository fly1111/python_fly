from django.contrib import admin
from TestModel.models import Test,Contact,Tag
# Register your models here.

class TagInline(admin.TabularInline):
    model = Tag
class ContactAdmin(admin.ModelAdmin):
    inlines  = [TagInline]
    list_display=('name','email','age',)
    search_fields = ('name',)
    fieldsets = (
            ['Main',{
                'classes':(),
                'fields' : ('name','email'),
                }],
            ['Advance',{
                'classes':('collapse',),
                'fields':('age',), 
                }] 
            )

admin.site.register(Contact,ContactAdmin)
admin.site.register([Test,Tag])


