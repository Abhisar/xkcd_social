from django.db import models

# Create your models here.

class Comments(models.Model):
    """
    creates a model/table Comments
    """
    name = models.CharField(max_length=25)
    comment = models.CharField(max_length=200)
    page_id = models.CharField(max_length=10)

    def __unicode__(self):
        """
        Will call the __unicode__ method of the User class and  to give
        an object a readable name
        """
        return self.title
