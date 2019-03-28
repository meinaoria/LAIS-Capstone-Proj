from django.db import models

# Create your models here.

class Elevators(models.Model):
    GREEN = 'GR'
    RED = 'RE'
    NA = 'N/A'
    elevatorID = models.CharField(max_length=4, primary_key=True)
    Elevator_Status = (
        ('GREEN', 'Green'),
        ('RED', 'Red'),
        ('NA', 'Not Available'),
    )
    Elevator_Status_Choice = models.CharField(max_length=5, choices=Elevator_Status, default=NA)

class Escalators(models.Model):
    GREEN = 'GR'
    RED = 'RE'
    NA = 'N/A'
    escalatorID = models.CharField(max_length=4, primary_key=True)
    Escalator_Status = (
        ('GREEN', 'Green'),
        ('RED', 'Red'),
        ('NA', 'Not Available'),
    )
    Escalator_Status_Choice = models.CharField(max_length=5, choices=Escalator_Status, default=NA)

class bridgeTable(models.Model):
    GREEN = 'GR'
    YELLOW = 'YE'
    RED = 'RE'
    NA = 'N/A'
    bridgeTableID = models.IntegerField(primary_key=True)

    Bridge_Status = (
        ('GREEN', 'Green'),
        ('YELLOW', 'Yellow'),
        ('RED', 'Red'),
    )

    Bridge_Status_Choice = models.CharField(max_length=6, choices=Bridge_Status, default=NA)

    PCA_Status = (
        ('GREEN', 'Green'),
        ('YELLOW', 'Yellow'),
        ('RED', 'Red'),
    )
    PCA_Status_Choice = models.CharField(max_length=6, choices=PCA_Status, default=NA)

    GPU_Status = (
        ('GREEN', 'Green'),
        ('YELLOW', 'Yellow'),
        ('RED', 'Red'),
    )
    GPU_Status_Choice = models.CharField(max_length=6, choices=GPU_Status, default=NA)

    class Meta:
        permissions = (
            ("has_write_access", "Can change the status"),

        )

# Baggage Tables 
# Dom/Int Baggage System
class domIntBaggageSystems(models.Model):
    GREEN = 'GR' 
    RED = 'RE'
    YELLOW = 'YE'
    NA = 'N/A'
    domIntBaggageID = models.CharField(max_length=4, primary_key=True)

    DomIntBaggage_Status = (
        ('GREEN', 'Green'),
        ('RED', 'Red'),
        ('YELLOW', 'Yellow'),
        ('NA', 'Not Available'),
    )
    DomIntBaggage_Status_Choice = models.CharField(max_length=5, choices=DomIntBaggage_Status, default=NA)

# TB Baggage System
class tbBaggageSystems(models.Model):
    GREEN = 'GR' 
    RED = 'RE'
    YELLOW = 'YE'
    NA = 'N/A'
    tbBaggageID = models.CharField(max_length=4, primary_key=True)

    TbBaggage_Status = (
        ('GREEN', 'Green'),
        ('RED', 'Red'),
        ('YELLOW', 'Yellow'),
        ('NA', 'Not Available'),
    )
    TbBaggage_Status_Choice = models.CharField(max_length=5, choices=TbBaggage_Status, default=NA)

# TB Oversize
class tbOversize(models.Model):
    GREEN = 'GR' 
    RED = 'RE'
    YELLOW = 'YE'
    NA = 'N/A'
    tbOversizeID = models.CharField(max_length=4, primary_key=True)

    TbOversize_Status = (
        ('GREEN', 'Green'),
        ('RED', 'Red'),
        ('YELLOW', 'Yellow'),
        ('NA', 'Not Available'),
    )
    TbOversize_Status_Choice = models.CharField(max_length=5, choices=TbOversize_Status, default=NA)

# Dom/Int Oversize
class domIntOversize(models.Model):
    GREEN = 'GR' 
    RED = 'RE'
    YELLOW = 'YE'
    NA = 'N/A'
    domIntOversizeID = models.CharField(max_length=4, primary_key=True)

    DomIntOversize_Status = (
        ('GREEN', 'Green'),
        ('RED', 'Red'),
        ('YELLOW', 'Yellow'),
        ('NA', 'Not Available'),
    )
    DomIntOversize_Status_Choice = models.CharField(max_length=5, choices=DomIntOversize_Status, default=NA)

class message(models.Model):
    message = models.CharField(max_length=240)