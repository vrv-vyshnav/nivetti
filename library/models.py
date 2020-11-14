from django.db import models

# Create your models here.

class PASSIVE(models.Model):
    choices = (
        ('passive','passive'),
        ('Clock_Timing','clock Timing'),
        ('CONNECTOR','CONNECTOR'),
        ('DISCRETE_ANALOG','DISCRETE_ANALOG'),
        ('ELECTRO_MECHANICAL','ELECTRO_MECHANICAL'),
        ('ANALOG_POWER','ANALOG_POWER'),
        ('IC_CLASS_A','IC_CLASS_A'),
        ('IC_MEMORY','IC_MEMORY'),
        ('INTERFACE_LOGIC','INTERFACE_LOGIC'),
        ('MECHANICAL','MECHANICAL'),
        ('IC_RF','IC_RF'),
        ('IC_SENSOR','IC_SENSOR'),
    )
    

    mpn = models.CharField(max_length=150, blank=True, null=True)
    mfr = models.CharField(max_length=150, blank=True, null=True)
    desc = models.CharField(max_length=150, blank=True, null=True)
    pkg = models.CharField(max_length=150, blank=True, null=True)
    ctype = models.CharField(max_length=150, choices=choices)
    ptype = models.CharField(max_length=150, blank=True, null=True)
    altmpn = models.CharField(max_length=150, blank=True, null=True) 
    altmfr = models.CharField(max_length=150, blank=True, null=True)
    tol = models.CharField(max_length=150, blank=True, null=True)
    rating = models.CharField(max_length=150, blank=True, null=True)
    temp = models.CharField(max_length=150, blank=True, null=True)
    values = models.CharField(max_length=150, blank=True, null=True)
    pcb_footprint = models.CharField(max_length=150, blank=True, null=True)
    symbol_id = models.CharField(max_length=150, blank=True, null=True)
    detete = models.CharField(max_length=150, blank=True, null=True)

    def __str__(self):
        return self.mpn
class CLOCK_TIMING(PASSIVE):
    pass
class CONNECTOR(PASSIVE):
    pass
class DISCRETE_ANALOG(PASSIVE):
    pass
class ELECTRO_MECHANICAL(PASSIVE):
    pass
class ANALOG_POWER(PASSIVE):
    pass
class IC_CLASS_A(PASSIVE):
    pass
class IC_MEMORY(PASSIVE):
    pass
class INTERFACE_LOGIC(PASSIVE):
    pass
class MECHANICAL(PASSIVE):
    pass
class IC_RF(PASSIVE):
    pass
class IC_SENSOR(PASSIVE):
    pass
