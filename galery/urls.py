from django.urls import path
from . import views

app_name = "galery"

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('upload', views.UploadView.as_view(), name='upload_view'),
    path('upload/uploading', views.uploadig_view, name='uploading'),
    path('<int:pk>/image', views.ImageView.as_view(), name='image')
    
]
