from django.contrib import admin

from .models import Pic

# admin.site.site_header = "Image Editor In Free"
# admin.site.site_title = "IMAGE"
# admin.site.index_title = "Welcome to Online Image Editor in Free"
admin.site.register(Pic)
