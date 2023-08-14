from django.db import models

class Pizza(models.Model):
    pizza_name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.p_name

class Topping(models.Model):
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    topping_name = models.CharField(max_length=200)

    def __str__(self):
        return self.topping_name


class Comment(models.Model):
    pizza = models.ForeignKey(Pizza,on_delete=models.CASCADE)
    content = models.TextField(max_length=300)

    def __str__(self):
        return f"Comment by {self.name} on {self.p_name} - {self.time}"

