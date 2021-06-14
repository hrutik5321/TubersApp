from django.contrib import admin
from .models import Youtuber

# Register your models here.
class YtAdmin(admin.ModelAdmin):
    


admin.site.register(Youtuber)
