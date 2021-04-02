# Generated by Django 3.1 on 2021-03-25 06:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(max_length=150)),
                ('categories', models.CharField(max_length=100)),
                ('archive', models.BooleanField(default=False)),
                ('holiday', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='holiday', to='travel.blog')),
            ],
        ),
    ]