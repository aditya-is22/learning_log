from django.db import models
from django.contrib.auth.models import User # 1. Import the User model

class Topic(models.Model):
    """A topic the user is learning about"""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE) # 2. Add the owner field

    def __str__(self):
        """Return a string representation of the model."""
        return self.text

# Defining the Entry Model
class Entry(models.Model):
    """Something specific learned about a topic"""

    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    """ on_delete=models.CASCADE means that if the related Topic instance is deleted, 
    all related Entry instances will also be deleted."""

    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        """set a special attribute telling Django to use
        'Entries' when it needs to refer to more than one entry (Otherwise would have been Entrys)"""
        verbose_name_plural = 'entries'

    def __str__(self):
        """Return a string representation of the model."""
        if len(self.text) > 50:
            return f"{self.text[ :50]}..."
        return self.text