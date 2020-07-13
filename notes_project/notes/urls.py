from django.urls import path

from notes import views

app_name = 'notes'

urlpatterns = [
    path('', views.ListNoteView.as_view(), name='list'),
    path('create/', views.CreateNoteView.as_view(), name='create'),
    path('detail/<int:pk>', views.DetailNoteView.as_view(), name='detail'),
    path('update/<int:pk>', views.UpdateNoteView.as_view(), name='update'),
    path('delete/<int:pk>', views.DeleteNoteView.as_view(), name='delete'),
]
