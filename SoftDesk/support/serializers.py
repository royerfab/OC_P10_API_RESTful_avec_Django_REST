from rest_framework.serializers import ModelSerializer
from support.models import Project, Issue, Comment, Contributor


class ProjectSerializer(ModelSerializer):
    class Meta:
        model = Project
        fields = ['id', 'type', 'title', 'description', 'author', 'time_created']
        extra_kwargs = {'author': {'read_only': True}}

class IssueSerializer(ModelSerializer):
    class Meta:
        model = Issue
        fields = ['id', 'project', 'assign_user', 'title', 'description', 'author', 'time_created', 'priority',
                  'balise', 'status']
        extra_kwargs = {'author': {'read_only': True}}


class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'issue', 'description', 'author', 'time_created', 'uuid']
        extra_kwargs = {'author': {'read_only': True}}

class ContributorSerializer(ModelSerializer):
    class Meta:
        model = Contributor
        fields = ['id', 'project', 'user']
