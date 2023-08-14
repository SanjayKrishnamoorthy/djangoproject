from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizzas', '0002_pizza_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pizza',
            name='image_name_with_file.ext',
        ),
        migrations.AddField(
            model_name='pizza',
            name='image',
            field=models.ImageField(default='default', upload_to='pizzas/static/media/'),
            preserve_default=False,
        ),
    ]