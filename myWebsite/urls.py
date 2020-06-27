# API Lib
from rest_framework import routers 

# general
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

from home import views as home_views

from dataset import views as dataset_views
from testing import views as testing_views
router = routers.DefaultRouter()
router.register('datasets', dataset_views.APIView)

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', home_views.index, name="home"),
    path('home/', home_views.index, name="home"),

    path('dataset/', dataset_views.index, name="dataset"),
    path('dataset/upload', dataset_views.upload, name="upload_dataset"),
    path('dataset/delete/<int:id>', dataset_views.delete, name="delete_dataset"),
    path('dataset/API', include(router.urls)),


    path('testing/', testing_views.index, name="testing"),
    path('testing/upload', testing_views.upload, name="upload_dataTesting"),
    path('testing/delete/<int:id>', testing_views.delete, name="delete_dataTesting"),



]

# urlpatterns += routers.urls




if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)