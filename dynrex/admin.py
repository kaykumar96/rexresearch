from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Content)
admin.site.register(ContentDetails)
admin.site.register(ContentDetailsImage)
admin.site.register(ContentDetailsFile)
admin.site.register(ContentDetailsUrl)
