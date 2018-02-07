from django.shortcuts import render
from .models import Guide

def guide(request, header):
    guide = Guide.objects.filter(header=header)
    return render(request, 'guides/guide.html', {'guide': guide})

