# Generated by Django 3.0.11 on 2020-11-23 21:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('donors', '0003_auto_20201123_1640'),
    ]

    operations = [
        migrations.AddField(
            model_name='campaign',
            name='display',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='donor',
            name='display',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='expense',
            name='display',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='donor',
            name='comment',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='donor',
            name='display_name',
            field=models.CharField(blank=True, max_length=255, verbose_name='Display Name'),
        ),
        migrations.AlterField(
            model_name='donor',
            name='is_company',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='expense',
            name='amount',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='expense',
            name='comment',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.CreateModel(
            name='Quote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, null=True)),
                ('comment', models.TextField(blank=True, null=True)),
                ('display', models.BooleanField(default=True)),
                ('campaign', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='donors.Campaign')),
            ],
        ),
        migrations.CreateModel(
            name='Partner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, null=True)),
                ('logo', models.ImageField(null=True, upload_to='logos')),
                ('comment', models.TextField(blank=True, null=True)),
                ('display', models.BooleanField(default=True)),
                ('campaign', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='donors.Campaign')),
            ],
        ),
        migrations.CreateModel(
            name='Need',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, null=True)),
                ('quantity', models.FloatField(default=0)),
                ('stock', models.FloatField(default=0)),
                ('supplier', models.CharField(max_length=255, null=True)),
                ('comment', models.TextField(blank=True, null=True)),
                ('display', models.BooleanField(default=True)),
                ('campaign', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='donors.Campaign')),
            ],
        ),
    ]