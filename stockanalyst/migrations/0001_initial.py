# Generated by Django 2.2.12 on 2020-07-19 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GoodsModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('appid', models.CharField(max_length=50)),
                ('goods_code', models.CharField(max_length=50)),
                ('on_hand_stock', models.IntegerField(default=0)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
