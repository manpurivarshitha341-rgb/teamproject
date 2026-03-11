from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

def home(request):
    return HttpResponse("Biometric Voting System Backend Running")

urlpatterns = [
    path('', home),
    path('admin/', admin.site.urls),
    path('voters/', include('apps.voters.urls')),
    path('vote/', include('apps.voting.urls')),
]