# Generated by Django 3.1.3 on 2021-01-02 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0006_auto_20210102_1732'),
    ]

    operations = [
        migrations.AddField(
            model_name='qpapers',
            name='Subject',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='qpapers',
            name='link',
            field=models.URLField(default=''),
        ),
    ]
