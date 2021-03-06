# Generated by Django 4.0.3 on 2022-04-09 20:31

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=64)),
                ('last_name', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Manager',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=64)),
                ('last_name', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('tasks', models.CharField(max_length=64)),
                ('manager', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projekt.manager')),
            ],
        ),
        migrations.CreateModel(
            name='WorkingTime',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('arrival', models.TimeField(blank=True, null=True)),
                ('leaving', models.TimeField(blank=True, null=True)),
                ('job_description', models.TextField()),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projekt.employee')),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('employee', models.ManyToManyField(to='projekt.employee')),
                ('manager', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='projekt.manager')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projekt.project')),
            ],
        ),
    ]
