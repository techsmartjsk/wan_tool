from django.db import models

class CircuitData(models.Model):
    GSP = models.CharField(max_length=100, default='Beddington')
    Node = models.CharField(max_length=100, default='Beddington')
    Substation = models.CharField(max_length=100, default='Beddington')
    dest_node = models.CharField(max_length=100, default='Beddington')
    dest_substation = models.CharField(max_length=100, default='Beddington')
    line_name = models.CharField(max_length=100, default='Beddington')
    oper_vol = models.CharField(max_length=100, default='Beddington')
    pos_R = models.CharField(max_length=100, default='Beddington')
    pos_X = models.CharField(max_length=100, default='Beddington')
    pos_B = models.CharField(max_length=100,default='Beddington')
    Summer_Rating = models.CharField(max_length=100, default='Beddington')
    Winter_Rating = models.CharField(max_length=100,default='Beddington')
    cir_leng = models.CharField(max_length=100,default='Beddington')

    def __str__(self):
        return self.GSP
        