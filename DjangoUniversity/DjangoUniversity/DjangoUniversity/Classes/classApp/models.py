from django.db import models

# Creating model of the University classes
class UniversityClasses(models.Model):
    title = models.CharField(max_length=60, default="", blank=True, null=False)
    course_number = models.IntegerField(default="", blank=True, null=False)
    instructor_name = models.CharField(max_length=60, default="", blank=True, null=False)
    duration = models.FloatField(null=True, blank=True, default=None)

    #this creates model manager
    object = models.Manager()

    #this dispays the object output values in the form of string
    def __str__(self):
        #returns the input value of the title and istructor name
        #field as a tuple to display in teh browser istead of the default titles
        display_course = '{0.title}: {0.instructor_name}'
        return display_course.format(self)

    #removes added 's' that Django adds to the model name in the browser display
    class Meta:
        verbose_name_plural = "University Classes"  