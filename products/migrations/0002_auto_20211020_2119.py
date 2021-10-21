# Generated by Django 3.2.7 on 2021-10-20 21:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['-parentGroup', '-subParentGroup', '-parentProductCategory']},
        ),
        migrations.RenameField(
            model_name='product',
            old_name='productCategory',
            new_name='parentProductCategory',
        ),
        migrations.AddField(
            model_name='product',
            name='subParentProductCategory',
            field=models.CharField(max_length=100, null=True),
        ),
    ]