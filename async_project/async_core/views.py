from adrf.views import APIView
from asgiref.sync import sync_to_async
from rest_framework.response import Response
from django.contrib.auth.models import User


@sync_to_async
def get_users() -> User:
    return User.objects.values('username')


class AsyncView(APIView):
    async def get(self, request):
        users = await get_users()
        return Response({
            'message': 'This is an async class based view.',
            'users': users,
        })
