from django.urls import path
from fountain.views import (
    CinemaListView, 
    CinemaDetailView,
    CinemaCreateView,
    CinemaUpdateView,
    CinemaDeleteView
)

app_name = 'fountain'
urlpatterns = [
    path('', CinemaListView.as_view(), name ='cinema-list'),
    path('create/', CinemaCreateView.as_view(), name = 'cinema-create'),
    path('<int:id>/', CinemaDetailView.as_view(), name= 'cinema-detail'),
    path('<int:id>/update/', CinemaUpdateView.as_view(), name='cinema-update'),
    path('<int:id>/delete/', CinemaDeleteView.as_view(), name='cinema-delete'),
]
    


