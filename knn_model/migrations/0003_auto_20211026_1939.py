# Generated by Django 3.2.4 on 2021-10-26 12:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('knn_model', '0002_auto_20211026_1929'),
    ]

    operations = [
        migrations.AlterField(
            model_name='history',
            name='id_history',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='message',
            name='id_message',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='message',
            name='id_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='knn_model.user'),
        ),
        migrations.AlterField(
            model_name='user',
            name='id_user',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
