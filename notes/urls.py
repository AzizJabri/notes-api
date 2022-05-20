from django.urls import path
from .views import noteList, noteDetail, noteCreate, noteUpdate, noteDelete, apiOverview

urlpatterns = [
    path('', apiOverview, name='api'),
    path('note-list/', noteList, name='note-list'),
    path('note-detail/<str:pk>/', noteDetail, name='note-detail'),
    path('note-create/', noteCreate, name='note-create'),
    path('note-update/<str:pk>/', noteUpdate, name='note-update'),
    path('note-delete/<str:pk>/', noteDelete, name='note-delete'),
]
