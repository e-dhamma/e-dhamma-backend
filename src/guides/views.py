from django.shortcuts import render
from markdown import markdown
from .models import Guide

def guide(request, header):
    guide = Guide.objects.filter(header=header.capitalize())[0]
    html = markdown(guide.content)
    return render(request, 'guides/guide.html', {'guide': guide, 'html': html})

