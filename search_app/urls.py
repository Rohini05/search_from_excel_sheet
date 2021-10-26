from django.urls import path,include
from rest_framework import routers

from . import views
from .views import (
    exceltoJsonData,
    searchJsonData,
    searchExcelSheetData
)


# router = routers.DefaultRouter()
# router.register('create-library-book', views.createLibraryBook) 

urlpatterns = [
    path('csv-to-json', exceltoJsonData, name="csv-to-json"),
    path('search-word-json', searchJsonData, name="search-word-json"),
    path('search-word-excel', searchExcelSheetData, name="search-word-excel"),
    # path('login', LoginAPI, name="login"),
    # path('', include(router.urls))
]