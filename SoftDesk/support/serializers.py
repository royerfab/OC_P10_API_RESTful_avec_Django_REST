from rest_framework.serializers import ModelSerializer
from support.models import Project, Issue, Comment, Contributor


# On utilise une classe Meta pour sérialiser à partir du Modèle, il est possible ici d'intégrer d'autres champs avant la classe Meta.
# Ils pourront servir à calculer de nouveaux champs à partir de ceux existants ou autres manipulations.
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
