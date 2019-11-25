from django.db import models

# Create your models here.

class Elevators(models.Model):
    GREEN = 'GR'
    RED = 'RE'
    NA = 'N/A'
    elevatorID = models.CharField(max_length=4, primary_key=True)
    elevatorTableID = models.IntegerField(null=False,unique=True)
    Elevator_Status = (
        ('GREEN', 'Green'),
        ('RED', 'Red'),
    )
    Elevator_Status_Choice = models.CharField(max_length=5, choices=Elevator_Status, default=NA)
    updated = models.DateTimeField(auto_now=True)


class Escalators(models.Model):
    GREEN = 'GR'
    RED = 'RE'
    NA = 'N/A'
    escalatorID = models.CharField(max_length=4, primary_key=True)
    escalatorTableID = models.IntegerField(null=False,unique=True)
    Escalator_Status = (
        ('GREEN', 'Green'),
        ('RED', 'Red'),

    )
    Escalator_Status_Choice = models.CharField(max_length=5, choices=Escalator_Status, default=NA)
    updated = models.DateTimeField(auto_now=True)

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
    bridgeUpdated = models.DateTimeField(auto_now=True)

    PCA_Status = (
        ('GREEN', 'Green'),
        ('YELLOW', 'Yellow'),
        ('RED', 'Red'),
    )
    PCA_Status_Choice = models.CharField(max_length=6, choices=PCA_Status, default=NA)
    pcaUpdated = models.DateTimeField(auto_now=True)

    GPU_Status = (
        ('GREEN', 'Green'),
        ('YELLOW', 'Yellow'),
        ('RED', 'Red'),
    )
    GPU_Status_Choice = models.CharField(max_length=6, choices=GPU_Status, default=NA)
    gpuUpdated = models.DateTimeField(auto_now=True)
    
    class Meta:
        permissions = (
            ("has_write_access", "Can change the status"),

        )

class message(models.Model):
    message = models.CharField(max_length=240)
    messageID = models.IntegerField(primary_key=True,default = 0)
    updated = models.DateTimeField(auto_now=True)

class bagCarousel(models.Model):
    GREEN = 'GR'
    RED = 'RE'
    YELLOW = 'YE'
    NA = 'N/A'
    bagCarouselID = models.IntegerField(primary_key=True)

    bagCarousel_Status = (
        ('GREEN', 'Green'),
        ('YELLOW', 'Yellow'),
        ('RED', 'Red'),

    )
    bagCarousel_Status_Choice = models.CharField(max_length=6, choices=bagCarousel_Status, default=NA)
    updated = models.DateTimeField(auto_now=True)


# Baggage systems
# Dom/Int Baggage Systems
class domIntBaggageSystems(models.Model):
    GREEN = 'GR'
    RED = 'RE'
    YELLOW = 'YE'
    NA = 'N/A'
    domIntBaggageID = models.CharField(max_length=4, primary_key=True)

    DomIntBaggage_Status = (
        ('GREEN', 'Green'),
        ('YELLOW', 'Yellow'),
        ('RED', 'Red'),
    )
    DomIntBaggage_Status_Choice = models.CharField(max_length=6, choices=DomIntBaggage_Status, default=NA)
    updated = models.DateTimeField(auto_now=True)

# TB Baggage System
class tbBaggageSystems(models.Model):
    GREEN = 'GR'
    RED = 'RE'
    YELLOW = 'YE'
    NA = 'N/A'
    tbBaggageID = models.CharField(max_length=4, primary_key=True)

    TbBaggage_Status = (
        ('GREEN', 'Green'),
        ('YELLOW', 'Yellow'),
        ('RED', 'Red'),


    )
    TbBaggage_Status_Choice = models.CharField(max_length=6, choices=TbBaggage_Status, default=NA)
    updated = models.DateTimeField(auto_now=True)

# TB Oversize Baggage
class tbOversize(models.Model):
    GREEN = 'GR'
    RED = 'RE'
    YELLOW = 'YE'
    NA = 'N/A'
    tbOversizeID = models.CharField(max_length=4, primary_key=True)

    TbOversize_Status = (
        ('GREEN', 'Green'),
        ('YELLOW', 'Yellow'),
        ('RED', 'Red'),

    )
    TbOversize_Status_Choice = models.CharField(max_length=6, choices=TbOversize_Status, default=NA)
    updated = models.DateTimeField(auto_now=True)

# Dom/Int Oversize Baggage
class domIntOversize(models.Model):
    GREEN = 'GR'
    RED = 'RE'
    YELLOW = 'YE'
    NA = 'N/A'
    domIntOversizeID = models.CharField(max_length=4, primary_key=True)

    DomIntOversize_Status = (
        ('GREEN', 'Green'),
        ('YELLOW', 'Yellow'),
        ('RED', 'Red'),


    )
    DomIntOversize_Status_Choice = models.CharField(max_length=6, choices=DomIntOversize_Status, default=NA)
    updated = models.DateTimeField(auto_now=True)






