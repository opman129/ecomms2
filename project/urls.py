from django.urls import path
from project.views import (project_detail_view, 
    project_create_view, 
    project_delete_view,
    project_detail_view,
    project_list_view,
    dynamic_lookup_view,
)

app_name = 'project'
urlpatterns = [
    path('', project_list_view, name = 'project-list'),
    path('create/', project_create_view, name ='project-create'),
    path('<int:id>/', dynamic_lookup_view, name='project-detail'),
    path('<int:id>/delete/', project_delete_view, name='project-delete'),
]