from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('badgify', '0002_alter_award_id_alter_badge_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='badge',
            name='show_avatar',
            field=models.BooleanField(default=False, verbose_name='Показывать аватарку'),
        ),
    ]
