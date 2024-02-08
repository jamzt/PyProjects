from django.db import models

# Creating model of the University campus
class UniversityCampus(models.Model):
    campus_name = models.CharField(max_length=60, default="", blank=True, null=False)
    state = models.CharField(max_length=2, default="", blank=True, null=False)
    campus_id = models.IntegerField(default="", blank=True, null=False)
   

    #this creates model manager
    object = models.Manager()

    #this dispays the object output values in the form of string
    def __str__(self):
        #returns the input value of the title and istructor name
        #field as a tuple to display in teh browser istead of the default titles
        display_campus = '{0.title}: {0.campus_name}'
        return display_campus.format(self)

    #removes added 's' that Django adds to the model name in the browser display
    class Meta:
        verbose_name_plural = "University Campuses"