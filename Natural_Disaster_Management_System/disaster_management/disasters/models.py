from django.db import models

class DisasterUpdate(models.Model):
    DISASTER_TYPES = [
        ('EQ', 'Earthquake'),
        ('FL', 'Flood'),
        ('CY', 'Cyclone'),
        ('TS', 'Tsunami'),
        ('OT', 'Other'),
    ]

    disaster_type = models.CharField(max_length=2, choices=DISASTER_TYPES)
    location = models.CharField(max_length=255)
    description = models.TextField()
    magnitude = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    affected_population = models.IntegerField(null=True, blank=True)
    damage_cost = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    date_reported = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.get_disaster_type_display()} at {self.location} on {self.date_reported}"

