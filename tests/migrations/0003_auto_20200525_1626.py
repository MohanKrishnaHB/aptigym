# Generated by Django 3.0.6 on 2020-05-25 16:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tests', '0002_studentquestionoption'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testquestions',
            name='partition',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='questions', to='tests.TestPartition'),
        ),
    ]
