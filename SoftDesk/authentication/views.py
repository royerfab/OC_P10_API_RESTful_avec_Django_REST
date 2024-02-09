from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.exceptions import PermissionDenied

from authentication.models import User
from authentication.serializers import UserSerializer, UserListSerializer
from authentication.permissions import IsOwnerOrReadOnly


class UserViewset(ModelViewSet):
    serializer_class = UserSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def get_queryset(self):
        return User.objects.all()
    
    #pour récupérer des informations dans les fonctions perform on passe par le serializer et validated_data
    def perform_create(self, serializer):
        age = serializer.validated_data['age']
        if int(age) >= 15:
            user = serializer.save()
            user.set_password(user.password)
            user.save()
        else:
            raise PermissionDenied("Il faut avoir au moins 15 ans pour créer un compte.")

    #l'action 'list' est une requête get, prévue par django
    def get_serializer_class(self):
        if self.action == 'list':
            self.serializer_class = UserListSerializer
        else:
            self.serializer_class = UserSerializer
        return self.serializer_class
    
    #fonction qui se déclenche lorsqu'on fait get one user, prévue par django
    def retrieve(self, request, *args, **kwargs):
        user = self.get_object()
        if user.can_data_be_shared or user == request.user:
            return super().retrieve(request, *args, **kwargs)
        else:
            raise PermissionDenied("Les données de cet utilisateur ne sont pas partagées.")