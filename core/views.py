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


class UserActionDetail(APIView):
        permission_classes = [permissions.IsAuthenticated]

        def get_object(self, user_action_id, user_id):
            try:
                return UserAction.objects.get(id=user_action_id, user=user_id)
            except UserAction.DoesNotExist:
                return None

        def get(self, request, user_action_id, *args, **kwargs):
            user_action_instance = self.get_object(user_action_id, request.user.id)
            if not user_action_instance:
                return Response(
                    {"res": "Object with action id does not exists"},
                    status=status.HTTP_400_BAD_REQUEST
                )

            serializer = UserActionSerializer(user_action_instance)
            return Response(serializer.data, status=status.HTTP_200_OK)

        def put(self, request, user_action_id, *args, **kwargs):
            user_action_instance = self.get_object(user_action_id, request.user.id)
            if not user_action_instance:
                return Response(
                    {"res": "Object with action id does not exists"},
                    status=status.HTTP_400_BAD_REQUEST
                )
            data = {
                "user": request.user.id,
                "action": request.data.get("action"),
                "numbers": request.data.get('numbers'),
                "numbers_sets": request.data.get("numbers_sets"),
                "time_duration": request.data.get("time_duration")
            }
            serializer = UserActionSerializer(instance=user_action_instance, data=data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        def delete(self, request, user_action_id, *args, **kwargs):
            '''
            Deletes the todo item with given todo_id if exists
            '''
            user_action_instance = self.get_object(user_action_id, request.user.id)
            if not user_action_instance:
                return Response(
                    {"res": "Object with action id does not exists"},
                    status=status.HTTP_400_BAD_REQUEST
                )
            user_action_instance.delete()
            return Response(
                {"res": "Object deleted!"},
                status=status.HTTP_200_OK
            )
