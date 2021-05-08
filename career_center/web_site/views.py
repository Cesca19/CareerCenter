from django.shortcuts import render
from web_site.models import Companies

# Create your views here.

from django.http import HttpResponse
from django.http import FileResponse


def index(request):
    return render(request, 'web_site/index.html')


def offer(request):
    companies = Companies.objects.all()
    context = {'companies': companies}
    return render(request, 'web_site/offers.html', context)

def detail(request, companie_name):
    fd = open("./static/" + companie_name, 'rb')
    return FileResponse(fd, content_type='application/pdf')
