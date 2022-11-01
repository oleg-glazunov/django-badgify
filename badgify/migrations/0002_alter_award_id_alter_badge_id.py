from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('badgify', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='award',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='badge',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
