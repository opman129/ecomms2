from django.contrib import admin

# Register your models here.
from .models import Cinema
    
class CinemaModelForm(admin.ModelAdmin):
    list_display = ["timestamp", "__str__", "updated", "title"]
    list_display_links = ["updated"]
    list_filter = ["updated", "timestamp"]
    search_fields = ["title", "content"]\
    
    class Meta:
        model = Cinema

admin.site.register(Cinema, CinemaModelForm)