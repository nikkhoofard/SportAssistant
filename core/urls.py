from django.urls import path, include
from .views import UserActionList
app_name = "core"

urlpatterns = [
    path("user_action/", UserActionList.as_view(), name="list"),
]
