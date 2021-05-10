from django.utils.timezone import now
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_api', '0006_alter_userprofile_surname'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='date',
            field=models.DateTimeField(default=now()),
        ),
    ]
