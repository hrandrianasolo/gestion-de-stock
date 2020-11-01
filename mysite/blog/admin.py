from django.contrib import admin
from . import models

admin.site.register(models.Article)
admin.site.register(models.Provider)
admin.site.register(models.Role)
admin.site.register(models.User)