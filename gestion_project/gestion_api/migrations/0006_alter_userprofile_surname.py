from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_api', '0005_alter_userprofile_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='surname',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
