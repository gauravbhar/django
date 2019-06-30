from django.contrib import admin


# Register your models here.
from project1.models import Reported,Article
admin.site.register(Reported)
admin.site.register(Article)
