# Generated by Django 3.2.15 on 2022-12-01 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administer_data', '0003_auto_20221023_2138'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='upcominglecinfos',
            name='is_iphone',
        ),
        migrations.AddField(
            model_name='upcominglecinfos',
            name='target_unit_type',
            field=models.CharField(choices=[('iPhone', 'iPhone'), ('Android', 'Android'), ('Tablet', 'Tablet'), ('Other', 'Other')], default='Other', max_length=20),
        ),
        migrations.AlterField(
            model_name='classinfo',
            name='lecture',
            field=models.ManyToManyField(blank=True, related_name='class_info', to='administer_data.Lecture'),
        ),
    ]
