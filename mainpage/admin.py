
from django.contrib import admin
from .models import  Banner, Image   

# admin.site.register(Banner)
# admin.site.register(Image)


#TARTIB
class BannerAdmin(admin.ModelAdmin):
    list_display = ['image', 'title', 'order']
    ordering = ['order']


class ImageAdmin(admin.ModelAdmin):
    list_display = ['image','title','title1','title2','link', 'link1','link2', 'order']
    ordering = ['order']




admin.site.register(Banner, BannerAdmin)
admin.site.register(Image, ImageAdmin)
