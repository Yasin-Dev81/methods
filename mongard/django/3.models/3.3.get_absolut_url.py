"""
- یه آبجکت به چه لینکی ریدایرکت بشه؟

- in html
    * {{ <...>.get_absolute_url }}
"""

from django.db import models
from django.urls import reverse

class DBFields(models.Model):
    
    x001 = models.CharField(
        max_length=150,
        unique=True,
    )

    def __str__(self) -> str:
        return '...'
    
    def get_absolut_url(self):
        return reverse('[url-name]', args=['...', ])
    
