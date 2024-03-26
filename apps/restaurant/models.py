from django.db import models


class Restaurant(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name


class Review(models.Model):
    restaurant = models.ForeignKey(
        Restaurant,
        on_delete=models.CASCADE,
        related_name='reviews'
    )
    rating = models.DecimalField(
        max_digits=3,
        decimal_places=2,
    )
    comment = models.TextField()

    def __str__(self):
        return f"Review for {self.restaurant.name}"
