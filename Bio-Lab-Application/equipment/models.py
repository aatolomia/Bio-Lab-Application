from django.db import models

# Create your models here.
class EquipmentType(models.Model):
	type_of_equipment = models.CharField(max_length = 100)
	description = models.CharField(max_length=1000)
	type_of_equipment_picture = models.CharField(max_length=1000)

	def __str__(self): #specify what to print out
		return self.type_of_equipment + " - " + self.description


class Equipment(models.Model):
	size_choices = (
		('S', 'Small'),
		('M', 'Medium'),
		('L', 'Large'),
		('XL', "Extra Large"),
	)

	functional_or_not_choices = (
		('Functional', 'Functional'),
		('Non-Functional', 'Non-Functional'),
	)

	equipment_type = models.ForeignKey(EquipmentType, on_delete=models.CASCADE)
	name_of_equipment = models.CharField(max_length = 100)	
	number_of_items = models.IntegerField()
	size = models.CharField(max_length = 2, choices = size_choices, blank = True)
	functional_or_not = models.CharField(max_length = 15, choices= functional_or_not_choices, blank = True)
	equipment_picture = models.CharField(max_length = 1000)

	def __str__(self): #specify what to print out
		return self.name_of_equipment