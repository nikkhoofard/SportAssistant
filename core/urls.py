from django.urls import path, include
from .views import UserActionList, UserActionRetrieve, UserActionCreate
app_name = "core"

urlpatterns = [
    path("user_action/", UserActionList.as_view(), name="list"),
    path("user_action/create/", UserActionCreate.as_view(), name="create"),
    path("user_action/<int:pk>", UserActionRetrieve.as_view(), name="detail"),
]
