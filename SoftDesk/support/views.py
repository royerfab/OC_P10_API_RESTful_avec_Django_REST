from django.shortcuts import render
from django.db.models import Q
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied

from support.permissions import IsAdminAuthenticated, IsAuthorOrReadOnly
from support.models import Project, Issue, Comment, Contributor
from support.serializers import ProjectSerializer, IssueSerializer, CommentSerializer, ContributorSerializer


class ProjectViewset(ModelViewSet):
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]

    #Ici on autorise l'utilisateur à faire des requêtes pour le projet s'il est auteur OU s'il est contributeur.
    def get_queryset(self):
        print(self.request.user)
        #return Project.objects.all()
        return self.queryset.filter(Q(author = self.request.user) | Q(contributor__user = self.request.user))

    #Ici le serializer sait que author est en read only mais pour le modèle c'est un champ obligatoire, ici la vue indique au modèle
    # que le champ author sera forcément l'utilisateur.
    def perform_create(self, serializer):
        serializer.save(author = self.request.user)


class IssueViewset(ModelViewSet):
    serializer_class = IssueSerializer
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]

    #à quoi sert cette fonction dans la fonction suivante?
    def get_queryset(self):
        return self.queryset.filter(Q(author = self.request.user) | Q(project__contributor__user = self.request.user))

    #on prend l'user de chaque contributeur du projet, il faut être dans cette liste d'user pour qua la vue dise au modèle que l'auteur est l'user.
    def perform_create(self, serializer):
        project = serializer.validated_data['project']
        contributors = [contributor.user for contributor in project.contributor_set.all()]
        if self.request.user in contributors or self.request.user == project.author:
            serializer.save(author = self.request.user)
        else:
            raise PermissionDenied("Vous n'êtes pas contributeur sur ce projet.")


class CommentViewset(ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]

    def get_queryset(self):
        return self.queryset.filter(Q(author = self.request.user) | Q(issue__project__contributor__user = self.request.user))

    def perform_create(self, serializer):
        issue = serializer.validated_data['issue']
        project = issue.project
        contributors = [contributor.user for contributor in project.contributor_set.all()]
        if self.request.user in contributors or self.request.user == project.author:
            serializer.save(author = self.request.user)
        else:
            raise PermissionDenied("Vous n'êtes pas contributeur sur ce projet.")

class ContributorViewset(ModelViewSet):
    serializer_class = ContributorSerializer
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        return self.queryset.filter(Q(project__author = self.request.user) | Q(project__contributor__user = self.request.user))
    
    #Permet de faire que seul l'auteur d'un projet peut ajouter un contributeur au projet.
    def perform_create(self, serializer):
        project = serializer.validated_data['project']
        if project.author == self.request.user:
            serializer.save()
        else:
            raise PermissionDenied("Vous n'avez pas la permission d'ajouter cet utilisateur à ce projet.")

