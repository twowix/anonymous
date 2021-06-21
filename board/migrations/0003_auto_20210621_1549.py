# Generated by Django 3.2.4 on 2021-06-21 06:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0002_alter_post_table'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='post',
            table='post',
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('reg_date', models.DateTimeField(auto_now_add=True)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='board.post')),
            ],
            options={
                'db_table': 'comment',
            },
        ),
    ]
