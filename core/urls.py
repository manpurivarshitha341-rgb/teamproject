from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render
from django.conf import settings
from django.conf.urls.static import static


# Dashboard / Home Page
def home(request):
    return render(request, "dashboard.html")


urlpatterns = [

    # Home Dashboard
    path('', home, name='home'),

    # Admin Panel
    path('admin/', admin.site.urls),

    # Voters Module
    path('voters/', include('apps.voters.urls')),

    # Voting Module
    path('voting/', include('apps.voting.urls')),

    # Authentication Module
    path('auth/', include('apps.authentication.urls')),

]


# Media files (images for face/iris)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)