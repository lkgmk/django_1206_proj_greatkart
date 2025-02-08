from django.contrib import admin
from .models import PersonalData, Album, Song, Author,Books,Vehicle,Car

# Register your models here.
class PersonalDataAdmin(admin.ModelAdmin):
    list_display = ('person_name','person_city')
    list_display_links = ('person_name','person_city',)
    list_filter = ('person_name','person_city',)

class AlbumAdmin(admin.ModelAdmin):
    list_display = ('title','artist')
    list_display_links = ('title','artist')
    list_filter = ('title','artist')


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('title', 'desc')
    list_display_links = ('title', 'desc')
    list_filter = ('title', 'desc')


admin.site.register(PersonalData,PersonalDataAdmin)
admin.site.register(Album,AlbumAdmin)
admin.site.register(Song)
admin.site.register(Author,AuthorAdmin)
admin.site.register(Books)
admin.site.register(Vehicle)
admin.site.register(Car)