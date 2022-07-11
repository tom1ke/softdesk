from rest_framework.serializers import ModelSerializer, SerializerMethodField

from .models import Project, Contributor, Issue, Comment


class ContributorSerializer(ModelSerializer):

    class Meta:
        model = Contributor
        fields = ['user', 'project', 'permission', 'role']


class ProjectListSerializer(ModelSerializer):

    class Meta:
        model = Project
        fields = ['title', 'author', 'type', 'description']


class ProjectDetailSerializer(ModelSerializer):

    issues = SerializerMethodField()
    contributors = SerializerMethodField()

    class Meta:
        model = Project
        fields = ['title', 'author', 'type', 'description', 'contributors', 'issues']

    def get_issues(self, instance):
        queryset = instance.issues.all()
        serializer = IssueListSerializer(queryset, many=True)
        return serializer.data

    def get_contributors(self, instance):
        queryset = instance.contributors.all()
        serializer = ContributorSerializer(queryset, many=True)
        return serializer.data


class IssueListSerializer(ModelSerializer):

    class Meta:
        model = Issue
        fields = ['tag', 'priority', 'status', 'title', 'project', 'author', 'date_created', 'assignee', 'description']


class IssueDetailSerializer(ModelSerializer):

    comments = SerializerMethodField()

    class Meta:
        model = Issue
        fields = ['tag', 'title', 'project', 'author', 'date_created', 'status', 'assignee', 'description', 'comments']

    def get_comments(self, instance):
        queryset = instance.comments.all()
        serializer = CommentSerializer(queryset, many=True)
        return serializer.data


class CommentSerializer(ModelSerializer):

    class Meta:
        model = Comment
        fields = ['author', 'issue', 'date_created', 'content']

