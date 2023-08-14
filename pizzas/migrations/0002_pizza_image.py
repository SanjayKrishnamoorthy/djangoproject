from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizzas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pizza',
            name='image_name_with_file.ext',
            field=models.CharField(default='image.png', max_length=100),
        ),
    ]


