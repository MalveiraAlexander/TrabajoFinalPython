# Generated by Django 4.1.4 on 2022-12-31 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('email', models.EmailField(max_length=254)),
                ('nombre', models.CharField(max_length=100)),
                ('avatar', models.ImageField(upload_to='')),
                ('password', models.CharField(max_length=55)),
                ('username', models.CharField(max_length=55)),
            ],
        ),
        migrations.DeleteModel(
            name='Tag',
        ),
        migrations.AddField(
            model_name='post',
            name='date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='img',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='post',
            name='subtitle',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=150),
        ),
    ]
