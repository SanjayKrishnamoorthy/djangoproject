
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizzas', '0003_image_name_with_file.ext'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pizza',
            name='image',
            field=models.ImageField(upload_to='images/'),
        ),
    ]