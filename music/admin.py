from django.contrib import admin

# Register your models here.
from .models import Albums, Songs

admin.site.register(Albums)
admin.site.register(Songs)

