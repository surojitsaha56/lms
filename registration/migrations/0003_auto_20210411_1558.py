# Generated by Django 3.0 on 2021-04-11 10:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0002_issuebook'),
    ]

    operations = [
        migrations.RenameField(
            model_name='issuebook',
            old_name='bid',
            new_name='b_id',
        ),
        migrations.RenameField(
            model_name='issuebook',
            old_name='bname',
            new_name='b_name',
        ),
        migrations.RenameField(
            model_name='issuebook',
            old_name='iid',
            new_name='s_id',
        ),
        migrations.RenameField(
            model_name='issuebook',
            old_name='sname',
            new_name='s_name',
        ),
        migrations.RemoveField(
            model_name='issuebook',
            name='sid',
        ),
    ]