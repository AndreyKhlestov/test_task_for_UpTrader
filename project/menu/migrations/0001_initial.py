# Generated by Django 2.2.16 on 2023-04-01 18:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MenuModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='MenuItemModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('slug', models.CharField(blank=True, max_length=50)),
                ('url', models.CharField(blank=True, max_length=50)),
                ('menu_name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='menu_item', to='menu.MenuModel')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='menu.MenuItemModel')),
            ],
        ),
    ]
