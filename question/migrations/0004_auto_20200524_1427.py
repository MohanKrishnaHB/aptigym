# Generated by Django 3.0.6 on 2020-05-24 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('question', '0003_auto_20200524_0850'),
    ]

    operations = [
        migrations.AlterField(
            model_name='options',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/options/'),
        ),
        migrations.AlterField(
            model_name='question',
            name='question_image',
            field=models.ImageField(blank=True, null=True, upload_to='images/question/'),
        ),
        migrations.AlterField(
            model_name='question',
            name='solution_image',
            field=models.ImageField(blank=True, null=True, upload_to='images/solution/'),
        ),
        migrations.AlterUniqueTogether(
            name='options',
            unique_together={('question', 'option')},
        ),
    ]