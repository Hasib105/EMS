# Generated by Django 5.1.1 on 2024-10-01 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_achievementemployee_unique_together_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='achievements',
            field=models.ManyToManyField(related_name='employees', to='core.achievement'),
        ),
    ]
