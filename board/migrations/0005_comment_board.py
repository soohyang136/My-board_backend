# Generated by Django 4.0.3 on 2022-07-26 16:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0004_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='board',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='board.board'),
        ),
    ]