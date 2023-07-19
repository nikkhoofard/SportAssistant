from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from core.models import UserAction
from .serializers import UserActionSerializer
from .permissions import IsCurrentUser
# Create your views here.


#class UserActionList(ListAPIView):
#    queryset = UserAction.objects.filter(user == request.user.id)
#   serializer_class = UserActionSerializer
#   permission_classes = [IsCurrentUser]
class UserActionList(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        user_actions = UserAction.objects.filter(user=request.user.id)
        serializer = UserActionSerializer(user_actions, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class UserActionCreate(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        data = {
            "user": request.user.id,
            "action": request.data.get("action"),
            "numbers": request.data.get('numbers'),
            "numbers_sets": request.data.get("numbers_sets"),
            "time_duration": request.data.get("time_duration")
        }
        serializer = UserActionSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



