from django.contrib import admin

from .models import Horse, Feeding, Training
# Register your models here.

admin.site.register(Horse)
admin.site.register(Feeding)
admin.site.register(Training)

