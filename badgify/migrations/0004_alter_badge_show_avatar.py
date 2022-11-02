from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('badgify', '0003_badge_show_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='badge',
            name='show_avatar',
            field=models.BooleanField(default=True, verbose_name='Показывать аватарку'),
        ),
    ]
