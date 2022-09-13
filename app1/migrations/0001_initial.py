# Generated by Django 4.1.1 on 2022-09-13 09:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='IrisModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sepal_length', models.DecimalField(blank=True, decimal_places=3, max_digits=3, null=True)),
                ('sepal_width', models.DecimalField(blank=True, decimal_places=3, max_digits=3, null=True)),
                ('petal_length', models.DecimalField(blank=True, decimal_places=3, max_digits=3, null=True)),
                ('petal_width', models.DecimalField(blank=True, decimal_places=3, max_digits=3, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
