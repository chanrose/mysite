# Generated by Django 3.1.7 on 2021-03-16 15:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('note_keeper', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='LogNote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modify_date', models.DateTimeField(verbose_name='date modified')),
                ('note', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='note_keeper.note')),
            ],
        ),
    ]