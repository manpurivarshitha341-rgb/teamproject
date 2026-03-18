from django.urls import path
from . import views

urlpatterns = [
    path('', views.vote, name='vote'),                # "/voting/" landing page
    path('start/', views.start_vote, name='start_vote'),  # "/voting/start/"
    path('scan-face/', views.scan_face, name='scan_face'),  # "/voting/scan-face/"
    path('submit-vote/', views.submit_vote, name='submit_vote'),  # "/voting/submit-vote/"
    path('results/', views.results, name='results'),  # "/voting/results/"
]