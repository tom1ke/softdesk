from django.contrib import admin

from .models import Project, Contributor, Issue, Comment


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'id', 'author', 'type')


class ContributorAdmin(admin.ModelAdmin):
    list_display = ('user', 'id', 'project', 'permission', 'role')


class IssueAdmin(admin.ModelAdmin):
    list_display = ('title','id', 'project', 'author', 'tag', 'status', 'date_created')


class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'id', 'issue', 'date_created')


admin.site.register(Project, ProjectAdmin)
admin.site.register(Contributor, ContributorAdmin)
admin.site.register(Issue, IssueAdmin)
admin.site.register(Comment, CommentAdmin)
