# Generated by Django 2.2.3 on 2019-09-30 20:54

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Package_Tracking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tracking_number', models.CharField(max_length=20)),
                ('Last_Name', models.CharField(max_length=20)),
                ('Service_Type', models.CharField(max_length=50)),
                ('Date_Time', models.DateTimeField(default=django.utils.timezone.now)),
                ('status', models.TextField()),
                ('Sender', models.CharField(max_length=50)),
                ('Activity', models.TextField()),
                ('Location', models.TextField()),
                ('Details', models.TextField()),
                ('Receiver_Address', models.TextField()),
                ('Estimated_delivery', models.DateTimeField(default=django.utils.timezone.now)),
                ('Ship_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
