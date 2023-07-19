from django.urls import path, include
from .views import *
app_name = "core"

urlpatterns = [
    path("user_action/", UserActionList.as_view(), name="list"),
    path("user_action/create/", UserActionCreate.as_view(), name="create"),
    path("user_action/<int:user_action_id>", UserActionDetail.as_view(), name="detail"),
]
