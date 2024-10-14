from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils import timezone

class CandidateTimestamp(models.Model):
    timestamp = models.DateTimeField(unique=True, db_index=True)
    value = models.IntegerField(
        validators=[MinValueValidator(-1000000), MaxValueValidator(1000000)]
    )
    
    year = models.IntegerField(validators=[MinValueValidator(1900), MaxValueValidator(9999)])
    month = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(12)])
    day = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(31)])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-timestamp']
        indexes = [
            models.Index(fields=['year', 'month', 'day']),
        ]
        verbose_name = "Candidate Timestamp"
        verbose_name_plural = "Candidate Timestamps"

    def __str__(self):
        return f"Value: {self.value} at {self.timestamp}"

    def save(self, *args, **kwargs):
        if self.timestamp:
            self.year = self.timestamp.year
            self.month = self.timestamp.month
            self.day = self.timestamp.day
        super().save(*args, **kwargs)