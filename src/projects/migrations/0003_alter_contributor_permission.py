# Generated by Django 4.0.5 on 2022-07-07 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_contributor_permission_alter_comment_issue_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contributor',
            name='permission',
            field=models.CharField(choices=[('RESTRICTED', 'ALL')], max_length=100),
        ),
    ]
