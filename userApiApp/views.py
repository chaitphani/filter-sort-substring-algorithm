from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.settings import api_settings

from django.db.models import Q
from .models import UserData
from .serializers import UserDataSerializer, UserDataUpdateSerializer
from .pagination import StandardResultsSetPagination
from .sub_string_search import get_string


class UserDataAPIView(APIView, StandardResultsSetPagination):

    serializer_class = UserDataSerializer

    def get(self, request, *args, **kwargs):
        user_results = []
        name_list = []

        users = UserData.objects.all().order_by('id')
        name = self.request.query_params.get('name')
        sort = self.request.query_params.get('sort')

        for i in UserData.objects.values('first_name', 'last_name'):
            name_list.append(i['first_name'])
            name_list.append(i['last_name'])

        if name is not None:
            values = get_string(name, name_list)
            users = users.filter(Q(first_name=values[0][0]) | Q(last_name=values[0][0]))

        if sort is not None:
            users = users.order_by(sort)

        if len(users) > 1:
            user_results = self.paginate_queryset(users, request)
            serializer = self.serializer_class(user_results, many=True)
            return self.get_paginated_response(serializer.data)
        else:
            serializer = self.serializer_class(users, many=True)
            return Response(serializer.data)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserDetailAPIView(APIView):

    serializer_class = UserDataUpdateSerializer

    def get(self, request, id):
        try:
            user_data_obj = UserData.objects.get(id=id)
            serializer = UserDataSerializer(user_data_obj)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            return Response({'error':'No user data found for given ID..'})

    def put(self, request, id):
        try:
            user_data_obj = UserData.objects.get(id=id)
            serializer = self.serializer_class(user_data_obj, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response({'error':'No user data found for given ID..'})

    def delete(self, request, id):
        try:
            user_data_obj = UserData.objects.get(id=id)
            user_data_obj.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except:
            return Response({'error':'No user data found for given ID..'})

