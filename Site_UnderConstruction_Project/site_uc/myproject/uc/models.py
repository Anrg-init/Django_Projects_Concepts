from django.db import models


# Create your models here.
class UnderContstruction(models.Model):
    is_uc  = models.BooleanField(default=False)
    uc_note = models.TextField(null=True, blank=True, help_text="Note for under construction mode")
    uc_duration = models.DateTimeField(null=True, blank=True, help_text="End date and time of the construction")
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Undeconstruction: {self.is_uc}"    
    
