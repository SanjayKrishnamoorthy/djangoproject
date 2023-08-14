from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pizzas', '0004_image_change'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=50)),
                ('pizza', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pizzas.pizza')),
            ],
        ),
    ]