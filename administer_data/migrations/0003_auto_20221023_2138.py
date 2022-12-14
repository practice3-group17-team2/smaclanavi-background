# Generated by Django 3.2.15 on 2022-10-23 12:38

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('administer_data', '0002_auto_20221001_0942'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClassOrganizer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('organizer_name', models.CharField(max_length=20, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='classinfo',
            name='has_parking',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AddField(
            model_name='classinfo',
            name='is_barrier_free',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AddField(
            model_name='classinfo',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='review',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.CreateModel(
            name='UpcomingLecInfos',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('is_personal_lec', models.BooleanField(blank=True, default=True)),
                ('is_iphone', models.BooleanField(blank=True, default=True)),
                ('can_select_date', models.BooleanField(blank=True, default=False)),
                ('lecture_content', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='upcoming_lecs', to='administer_data.lecture')),
                ('which_class_held', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='upcoming_lecs', to='administer_data.classinfo')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='LecSchedule',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('date', models.DateTimeField()),
                ('lec_info', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='schedules', to='administer_data.upcominglecinfos')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='classinfo',
            name='class_organizer',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='administer_data.classorganizer'),
        ),
    ]
