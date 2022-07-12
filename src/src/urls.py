"""src URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from projects.views import ProjectViewSet, ContributorViewSet, IssueViewSet, CommentViewSet

projects = routers.SimpleRouter()
projects.register('projects', ProjectViewSet, basename='projects')

contributors = routers.SimpleRouter()
contributors.register('contributors', ContributorViewSet, basename='contributors')

issues = routers.SimpleRouter()
issues.register('issues', IssueViewSet, basename='issues')

comments = routers.SimpleRouter()
comments.register('comments', CommentViewSet, basename='comments')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-browser-auth/', include('rest_framework.urls')),
    path('signup/', include('dj_rest_auth.registration.urls')),
    path('login/', TokenObtainPairView.as_view(), name='login'),
    path('refresh/', TokenRefreshView.as_view(), name='refresh'),
    path('', include(projects.urls)),
    path('projects/<int:project_id>/', include(contributors.urls)),
    path('projects/<int:project_id>/', include(issues.urls)),
    path('projects/<int:project_id>/issues/<int:issue_id>/', include(comments.urls)),
]
