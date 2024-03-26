from django.db import models


class Restaurant(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name


class Review(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    rating = models.DecimalField(max_digits=3, decimal_places=2)
    comment = models.TextField()

    def __str__(self):
        return f"Review for {self.restaurant.name}"


class Comment(models.Model):
    text = models.TextField(
        "Messages",
        max_length=5000
    )
    parent = models.ForeignKey(
        'self',
        verbose_name="Parent",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="children"
    )
    restaurant = models.ForeignKey(
        Restaurant,
        verbose_name="product",
        on_delete=models.CASCADE,
        null=True,
        related_name="reviews",
    )

    def __str__(self):
        return f"{self.username} - {self.product}"