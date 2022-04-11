# Generated by Django 3.2.12 on 2022-04-11 20:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Technology',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=225)),
                ('image', models.ImageField(upload_to='technologies')),
            ],
            options={
                'verbose_name': 'Technology',
                'verbose_name_plural': 'Technologies',
            },
        ),
    ]
