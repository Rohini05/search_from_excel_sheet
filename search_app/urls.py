from django.urls import path,include
from rest_framework import routers

from . import views
from .views import (
    universityCsvIntoJsonData,
    searchJsonData
)


# router = routers.DefaultRouter()
# router.register('create-library-book', views.createLibraryBook) 

urlpatterns = [
    path('csv-to-json', universityCsvIntoJsonData, name="csv-to-json"),
    path('search-word-json', searchJsonData, name="search-word-json"),
    # path('login', LoginAPI, name="login"),
    # path('', include(router.urls))
]