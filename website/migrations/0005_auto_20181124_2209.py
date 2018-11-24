# Generated by Django 2.1.2 on 2018-11-24 21:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0004_auto_20181124_1947'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='interaction',
            options={'verbose_name': 'Interaction'},
        ),
        migrations.AlterModelOptions(
            name='refund',
            options={'verbose_name': 'Refund'},
        ),
        migrations.RemoveField(
            model_name='prescription',
            name='story',
        ),
        migrations.AddField(
            model_name='prescription',
            name='doctor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='website.Doctor'),
        ),
        migrations.AddField(
            model_name='prescription',
            name='patient',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='website.Patient'),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='title',
            field=models.CharField(choices=[('LE', 'lek.'), ('DR', 'dr n. med.'), ('DH', 'dr hab. n. med.'), ('PR', 'prof. dr hab. n. med.')], default='LE', max_length=2),
        ),
        migrations.AlterField(
            model_name='patient',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1),
        ),
    ]
