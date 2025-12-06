from django.db import models


class Review(models.Model):
    full_name = models.CharField(max_length=255)
    email = models.EmailField()
    text = models.TextField()
    is_verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self) -> str:
        return self.full_name
