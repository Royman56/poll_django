# Generated by Django 4.0.3 on 2022-03-10 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=50)),
                ('question', models.CharField(max_length=100)),
                ('opt_1', models.CharField(max_length=50)),
                ('opt_2', models.CharField(max_length=50)),
                ('opt_3', models.CharField(max_length=50)),
                ('count_opt_1', models.IntegerField(default=0)),
                ('count_opt_2', models.IntegerField(default=0)),
                ('count_opt_3', models.IntegerField(default=0)),
                ('ip_add', models.TextField(default=0)),
            ],
        ),
    ]
