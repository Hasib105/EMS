# Generated by Django 5.1.1 on 2024-10-01 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_remove_employee_achievements_and_more'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='achievementemployee',
            unique_together={('achievement', 'employee')},
        ),
        migrations.AlterField(
            model_name='achievementemployee',
            name='achievement_date',
            field=models.DateField(auto_now_add=True),
        ),
    ]
