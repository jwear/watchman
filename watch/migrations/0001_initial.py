# Generated by Django 2.0 on 2017-12-16 05:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Price',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.FloatField()),
                ('changed', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Watch',
            fields=[
                ('url', models.URLField()),
                ('item_id', models.CharField(max_length=256, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=512)),
                ('image_url', models.URLField()),
                ('service', models.CharField(choices=[('amz', 'Amazon'), ('eby', 'eBay')], max_length=3)),
            ],
        ),
        migrations.AddField(
            model_name='price',
            name='watch',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='prices', to='watch.Watch'),
        ),
    ]
