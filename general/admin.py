from django.contrib import admin
from .models import LetterToAdmin

class LetterToAdminAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'title', 'solved')

admin.site.register(LetterToAdmin, LetterToAdminAdmin)
admin.site.site_header = 'E-dhamma'
