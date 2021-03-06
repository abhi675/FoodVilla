# Generated by Django 3.1.6 on 2021-06-22 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('address', models.TextField()),
                ('email', models.EmailField(max_length=254)),
                ('nameoncard', models.CharField(max_length=50)),
                ('creditcardnumber', models.CharField(max_length=50)),
                ('cvv', models.CharField(max_length=50)),
                ('date', models.DateField()),
                ('price', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('price', models.IntegerField(default=0)),
                ('img', models.ImageField(upload_to='pics')),
            ],
        ),
    ]
