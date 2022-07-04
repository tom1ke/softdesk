from rest_framework.viewsets import ReadOnlyModelViewSet, ModelViewSet
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated

from .permissions import IsAuthorAndOrIsAuthenticated
from .models import Project, Contributor, Issue, Comment
from .serializers import (
    ProjectListSerializer, ProjectDetailSerializer, ContributorSerializer, IssueListSerializer, IssueDetailSerializer,
    CommentListSerializer, CommentDetailSerializer
)


class MultipleSerializerMixin:

    detail_serializer_class = None

    def get_serializer_class(self):
        if self.action == 'retrieve' and self.detail_serializer_class is not None:
            return self.detail_serializer_class
        return super().get_serializer_class()


class ProjectViewSet(MultipleSerializerMixin, ModelViewSet):

    serializer_class = ProjectListSerializer
    detail_serializer_class = ProjectDetailSerializer
    permission_classes = [IsAuthorAndOrIsAuthenticated]

    def get_queryset(self):
        return Project.objects.filter(author=self.request.user)


class ContributorViewSet(MultipleSerializerMixin, ModelViewSet):

    serializer_class = ContributorSerializer
    permission_classes = [IsAuthorAndOrIsAuthenticated]

    def get_queryset(self):
        return Contributor.objects.filter(project=self.kwargs['project_id'])


class IssueViewSet(MultipleSerializerMixin, ModelViewSet):

    serializer_class = IssueListSerializer
    detail_serializer_class = IssueDetailSerializer
    permission_classes = [IsAuthorAndOrIsAuthenticated]

    def get_queryset(self):
        queryset = Issue.objects.filter(project=self.kwargs['project_id'])
        project_id = self.request.GET.get('project_id')
        if project_id is not None:
            queryset = queryset.filter(project_id=project_id)
        return queryset


class CommentViewSet(MultipleSerializerMixin, ModelViewSet):

    serializer_class = CommentListSerializer
    detail_serializer_class = CommentDetailSerializer
    permission_classes = [IsAuthorAndOrIsAuthenticated]

    def get_queryset(self):
        queryset = Comment.objects.filter(issue=self.kwargs['issue_id'])
        issue_id = self.request.GET.get('issue_id')
        if issue_id is not None:
            queryset = queryset.filter(issue_id=issue_id)
        return queryset
