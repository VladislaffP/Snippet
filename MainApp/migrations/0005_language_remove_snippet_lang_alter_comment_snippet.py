# Generated by Django 4.1.7 on 2023-02-28 17:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0004_comment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('short_name', models.CharField(max_length=8)),
                ('full_name', models.CharField(max_length=32)),
            ],
        ),
        migrations.RemoveField(
            model_name='snippet',
            name='lang',
        ),
        migrations.AlterField(
            model_name='comment',
            name='snippet',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='MainApp.snippet'),
        ),
    ]
