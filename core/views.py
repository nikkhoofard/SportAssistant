from rest_framework.generics import ListAPIView
from core.models import UserAction
from .serializers import UserActionSerializer
# Create your views here.


class UserActionList(ListAPIView):
    queryset = UserAction.objects.all()
    serializer_class = UserActionSerializer
