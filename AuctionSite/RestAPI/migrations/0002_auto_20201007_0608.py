# Generated by Django 3.1.2 on 2020-10-07 00:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RestAPI', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bidder',
            old_name='bidder',
            new_name='Bidder',
        ),
        migrations.RenameField(
            model_name='vendor',
            old_name='vendor',
            new_name='Vendor',
        ),
        migrations.RemoveField(
            model_name='bidder',
            name='qualifications',
        ),
        migrations.AddField(
            model_name='bidder',
            name='Address1',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
        migrations.AddField(
            model_name='bidder',
            name='Address2',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
        migrations.AddField(
            model_name='bidder',
            name='City',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='bidder',
            name='CompanyName',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='bidder',
            name='Country',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='bidder',
            name='MobileNumber',
            field=models.CharField(blank=True, max_length=12, null=True),
        ),
        migrations.AddField(
            model_name='bidder',
            name='PostalZip',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='bidder',
            name='State',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='bidder',
            name='Telephone',
            field=models.CharField(blank=True, max_length=12, null=True),
        ),
        migrations.AddField(
            model_name='vendor',
            name='Address1',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
        migrations.AddField(
            model_name='vendor',
            name='Address2',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
        migrations.AddField(
            model_name='vendor',
            name='City',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='vendor',
            name='CompanyName',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='vendor',
            name='Country',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='vendor',
            name='MobileNumber',
            field=models.CharField(blank=True, max_length=12, null=True),
        ),
        migrations.AddField(
            model_name='vendor',
            name='PostalZip',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='vendor',
            name='State',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='vendor',
            name='Telephone',
            field=models.CharField(blank=True, max_length=12, null=True),
        ),
    ]