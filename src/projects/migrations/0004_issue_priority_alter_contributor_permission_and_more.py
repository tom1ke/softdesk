# Generated by Django 4.0.5 on 2022-07-11 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_alter_contributor_permission'),
    ]

    operations = [
        migrations.AddField(
            model_name='issue',
            name='priority',
            field=models.CharField(choices=[('FAIBLE', 'FAIBLE'), ('MOYENNE', 'MOYENNE'), ('ELEVEE', 'ELEVEE')], default='FAIBLE', max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='contributor',
            name='permission',
            field=models.CharField(choices=[('RESTRICTED', 'RESTRICTED'), ('ALL', 'ALL')], max_length=100),
        ),
        migrations.AlterField(
            model_name='issue',
            name='status',
            field=models.CharField(choices=[('A FAIRE', 'A FAIRE'), ('EN COURS', 'EN COURS'), ('TERMINE', 'TERMINE')], max_length=100),
        ),
        migrations.AlterField(
            model_name='issue',
            name='tag',
            field=models.CharField(choices=[('BUG', 'BUG'), ('AMELIORATION', 'AMELIORATION'), ('TACHE', 'TACHE')], max_length=100),
        ),
    ]
