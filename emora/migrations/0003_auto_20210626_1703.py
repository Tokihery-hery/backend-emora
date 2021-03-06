# Generated by Django 3.2.4 on 2021-06-26 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emora', '0002_auto_20210626_1647'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductsEmora',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('owner_id', models.CharField(max_length=120)),
                ('name', models.CharField(max_length=120)),
                ('category', models.CharField(max_length=120)),
                ('description', models.TextField()),
                ('connected', models.BooleanField(default=False)),
                ('priceUi', models.CharField(max_length=120)),
                ('disponibilite', models.CharField(max_length=13)),
                ('images', models.CharField(max_length=120)),
                ('state', models.CharField(max_length=120)),
                ('stock', models.CharField(max_length=130)),
                ('avatar', models.BinaryField()),
            ],
        ),
        migrations.RemoveField(
            model_name='usersemora',
            name='identify',
        ),
    ]
