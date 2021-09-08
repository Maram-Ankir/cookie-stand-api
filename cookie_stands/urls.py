from django.urls import path
from .views import CookieList, CookieDetail

urlpatterns = [
    path("", CookieList.as_view(), name="thing_list"),
    path("<int:pk>/", CookieDetail.as_view(), name="thing_detail"),
]
