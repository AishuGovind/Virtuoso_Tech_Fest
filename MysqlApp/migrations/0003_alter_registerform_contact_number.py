# Generated by Django 4.1.7 on 2023-04-02 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MysqlApp', '0002_alter_registerform_table'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registerform',
            name='Contact_Number',
            field=models.CharField(max_length=50),
        ),
    ]
