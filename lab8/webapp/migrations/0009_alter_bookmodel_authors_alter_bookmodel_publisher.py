# Generated by Django 4.2 on 2023-05-04 11:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0008_productmodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookmodel',
            name='authors',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webapp.authormodel'),
        ),
        migrations.AlterField(
            model_name='bookmodel',
            name='publisher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webapp.publishermodel'),
        ),
    ]
