# Generated by Django 3.0.5 on 2020-04-30 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('axfapp', '0005_maingood'),
    ]

    operations = [
        migrations.CreateModel(
            name='FoodType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('typeid', models.CharField(max_length=20)),
                ('typename', models.CharField(max_length=100)),
                ('childtypenames', models.CharField(max_length=100)),
                ('typesort', models.IntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='Goods',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productid', models.CharField(max_length=20)),
                ('productimg', models.CharField(max_length=200)),
                ('productname', models.CharField(max_length=100)),
                ('productlongname', models.CharField(max_length=200)),
                ('isselected', models.IntegerField(default=1)),
                ('onefree', models.CharField(max_length=100)),
                ('specifics', models.CharField(max_length=100)),
                ('price', models.FloatField(default=0)),
                ('originprice', models.FloatField(default=1)),
                ('categoryid', models.CharField(max_length=20)),
                ('childcid', models.CharField(max_length=20)),
                ('childcidname', models.CharField(max_length=100)),
                ('detailid', models.CharField(max_length=20)),
                ('inventory', models.IntegerField(default=1)),
                ('soldnum', models.IntegerField(default=1)),
            ],
        ),
    ]
