from django.db import models

from django.urls import reverse # Used to generate URLs by reversing the URL patterns

class Medicine(models.Model):
    # Model representing a Medicine 
    med_name = models.CharField(max_length=200)
    purpose = models.TextField(max_length=200, help_text='Enter a brief description')
    unit = models.CharField('Unit', max_length=100, help_text='Enter the unit of Med')
    dosage = models.IntegerField('dosage',blank=True, null=True, help_text='Dosage of Med')
    stock = models.IntegerField('available',blank=True, null=True, help_text='Availability')
    
    
    
    def __str__(self):
        """String for representing the Model object."""
        return self.med_name
    
    def get_absolute_url(self):
        """Returns the url to access a detail record for this book."""
        return reverse('medicine-detail', pk=[str(self.id)])
    
 
    

