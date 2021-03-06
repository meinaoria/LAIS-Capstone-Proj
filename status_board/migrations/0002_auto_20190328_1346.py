# Generated by Django 2.0.7 on 2019-03-28 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('status_board', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='domIntBaggageSystems',
            fields=[
                ('domIntBaggageID', models.CharField(max_length=4, primary_key=True, serialize=False)),
                ('DomIntBaggage_Status_Choice', models.CharField(choices=[('GREEN', 'Green'), ('RED', 'Red'), ('YELLOW', 'Yellow')], default='N/A', max_length=6)),
            ],
        ),
        migrations.CreateModel(
            name='domIntOversize',
            fields=[
                ('domIntOversizeID', models.CharField(max_length=4, primary_key=True, serialize=False)),
                ('DomIntOversize_Status_Choice', models.CharField(choices=[('GREEN', 'Green'), ('RED', 'Red'), ('YELLOW', 'Yellow')], default='N/A', max_length=6)),
            ],
        ),
        migrations.CreateModel(
            name='tbBaggageSystems',
            fields=[
                ('tbBaggageID', models.CharField(max_length=4, primary_key=True, serialize=False)),
                ('TbBaggage_Status_Choice', models.CharField(choices=[('GREEN', 'Green'), ('RED', 'Red'), ('YELLOW', 'Yellow')], default='N/A', max_length=6)),
            ],
        ),
        migrations.CreateModel(
            name='tbOversize',
            fields=[
                ('tbOversizeID', models.CharField(max_length=4, primary_key=True, serialize=False)),
                ('TbOversize_Status_Choice', models.CharField(choices=[('GREEN', 'Green'), ('RED', 'Red'), ('YELLOW', 'Yellow')], default='N/A', max_length=6)),
            ],
        ),
        migrations.AlterField(
            model_name='elevators',
            name='Elevator_Status_Choice',
            field=models.CharField(choices=[('GREEN', 'Green'), ('RED', 'Red')], default='N/A', max_length=5),
        ),
        migrations.AlterField(
            model_name='escalators',
            name='Escalator_Status_Choice',
            field=models.CharField(choices=[('GREEN', 'Green'), ('RED', 'Red')], default='N/A', max_length=5),
        ),
    ]
