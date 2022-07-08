from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .permissions import IsAuthorAndOrIsAuthenticated, IsProjectAuthorAndIsAuthenticated
from .models import Contributor, Project, Issue, Comment
from .serializers import ContributorSerializer, ProjectListSerializer, ProjectDetailSerializer, \
    IssueListSerializer, IssueDetailSerializer, CommentSerializer


class MultipleSerializerMixin:

    detail_serializer_class = None

    def get_serializer_class(self):
        if self.action == 'retrieve' and self.detail_serializer_class is not None:
            return self.detail_serializer_class
        return super().get_serializer_class()


class ContributorViewSet(MultipleSerializerMixin, ModelViewSet):

    serializer_class = ContributorSerializer
    permission_classes = [IsProjectAuthorAndIsAuthenticated]

    def get_queryset(self):
        return Contributor.objects.filter(project=self.kwargs['project_id'])

    def create(self, request, *args, **kwargs):
        contributor_data = request.data

        new_contributor = Contributor.objects.create(
            user_id=contributor_data['user'],
            permission=contributor_data['permission'],
            role=contributor_data['role'],
            project_id=kwargs['project_id']
        )

        new_contributor.save()

        serializer = ContributorSerializer(new_contributor)

        return Response(serializer.data)


class ProjectViewSet(MultipleSerializerMixin, ModelViewSet):

    serializer_class = ProjectListSerializer
    detail_serializer_class = ProjectDetailSerializer
    permission_classes = [IsAuthorAndOrIsAuthenticated]

    def get_queryset(self):
        return Project.objects.filter(contributors__user=self.request.user)

    def create(self, request, *args, **kwargs):
        project_data = request.data

        new_project = Project.objects.create(
            title=project_data['title'],
            description=project_data['description'],
            type=project_data['type'],
            author=self.request.user
        )

        new_project.save()

        Contributor.objects.create(user=self.request.user, project=new_project, role='author', permission='ALL')

        serializer = ProjectListSerializer(new_project)

        return Response(serializer.data)


class IssueViewSet(MultipleSerializerMixin, ModelViewSet):

    serializer_class = IssueListSerializer
    detail_serializer_class = IssueDetailSerializer
    permission_classes = [IsAuthorAndOrIsAuthenticated]

    def get_queryset(self):
        return Issue.objects.filter(project=self.kwargs['project_id'])

    def create(self, request, *args, **kwargs):
        issue_data = request.data

        new_issue = Issue.objects.create(
            tag=issue_data['tag'],
            title=issue_data['title'],
            status=issue_data['status'],
            description=issue_data['description'],
            project_id=kwargs['project_id'],
            author=self.request.user,
            assignee=self.request.user
        )

        new_issue.save()

        serializer = IssueListSerializer(new_issue)

        return Response(serializer.data)


class CommentViewSet(MultipleSerializerMixin, ModelViewSet):

    serializer_class = CommentSerializer
    permission_classes = [IsAuthorAndOrIsAuthenticated]

    def get_queryset(self):
        return Comment.objects.filter(issue=self.kwargs['issue_id'])

    def create(self, request, *args, **kwargs):
        comment_data = request.data

        new_comment = Comment.objects.create(
            content=comment_data['content'],
            author=self.request.user,
            issue_id=kwargs['issue_id']
        )

        new_comment.save()

        serializer = CommentSerializer(new_comment)

        return Response(serializer.data)
