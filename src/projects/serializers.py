from rest_framework.serializers import ModelSerializer, SerializerMethodField

from .models import Project, Contributor, Issue, Comment


class ProjectListSerializer(ModelSerializer):

    class Meta:
        model = Project
        fields = ['title', 'author', 'type']


class ProjectDetailSerializer(ModelSerializer):

    issues = SerializerMethodField()

    class Meta:
        model = Project
        fields = ['title', 'author', 'type', 'description', 'issues']

    def get_issues(self, instance):
        queryset = instance.issues.all()
        serializer = IssueListSerializer(queryset, many=True)
        return serializer.data


class ContributorSerializer(ModelSerializer):

    class Meta:
        model = Contributor
        fields = ['user', 'project', 'permission', 'role']


class IssueListSerializer(ModelSerializer):

    class Meta:
        model = Issue
        fields = ['tag', 'title', 'project', 'author', 'date_created', 'status']


class IssueDetailSerializer(ModelSerializer):

    comments = SerializerMethodField()

    class Meta:
        model = Issue
        fields = ['tag', 'title', 'project', 'author', 'date_created', 'status', 'assignee', 'description', 'comments']

    def get_comments(self, instance):
        queryset = instance.comments.all()
        serializer = CommentListSerializer(queryset, many=True)
        return serializer.data


class CommentListSerializer(ModelSerializer):

    class Meta:
        model = Comment
        fields = ['author', 'issue', 'date_created']


class CommentDetailSerializer(ModelSerializer):

    class Meta:
        model = Comment
        fields = ['author', 'issue', 'date_created', 'content']
