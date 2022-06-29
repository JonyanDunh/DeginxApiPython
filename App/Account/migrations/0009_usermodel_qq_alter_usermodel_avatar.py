# Generated by Django 4.0.5 on 2022-06-29 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0008_auto_20220629_1331'),
    ]

    operations = [
        migrations.AddField(
            model_name='usermodel',
            name='qq',
            field=models.CharField(max_length=25, null=True),
        ),
        migrations.AlterField(
            model_name='usermodel',
            name='avatar',
            field=models.CharField(blank=True, default='https://message.biliimg.com/bfs/im/5a7310c3a47c0b1ac6c9153b5aa84dd4bb641f8f.png', max_length=200, null=True),
        ),
    ]
