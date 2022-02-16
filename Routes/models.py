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
    Network_Area = models.CharField(max_length=100,default='EPN')

    def __str__(self):
        return self.Substation

class TransformerData(models.Model):
    GSP = models.CharField(max_length=50)
    HV_Node = models.CharField(max_length=50)
    HV_Substn = models.CharField(max_length=50)
    VoltHV_kV = models.CharField(max_length=50)
    LV_Node = models.CharField(max_length=50)
    LV_Substn = models.CharField(max_length=50)
    VoltLV_kV = models.CharField(max_length=50)
    VecGrp = models.CharField(max_length=50)
    PSeqImp_R = models.CharField(max_length=50)
    PSeqImp_X = models.CharField(max_length=50)
    ZSeqImp_X = models.CharField(max_length=50)
    TapMin = models.CharField(max_length=50)
    TapMax = models.CharField(max_length=50)
    TRatingMVA_Sum = models.CharField(max_length=50)
    TRatingMVA_Win = models.CharField(max_length=50)
    RevPowCap = models.CharField(max_length=50)
    Earth_HV = models.CharField(max_length=50)
    Earth_LV = models.CharField(max_length=50)
    Network_Area = models.CharField(max_length=100,default='EPN')

    def __str__(self):
        return self.GSP

class LoadData(models.Model):
    GSP = models.CharField(max_length=50)
    Substn = models.CharField(max_length=50)
    Season = models.CharField(max_length=50)
    MaxDem_19_20_MW = models.CharField(max_length=50)
    MaxDem_19_20_PF = models.CharField(max_length=50)
    MaxDem_20_21 = models.CharField(max_length=50)
    MaxDem_21_22 = models.CharField(max_length=50)
    MaxDem_22_23 = models.CharField(max_length=50)
    MaxDem_23_24 = models.CharField(max_length=50)
    MaxDem_24_25 = models.CharField(max_length=50)
    FirmCap_MW = models.CharField(max_length=50)
    MinLoadSF = models.CharField(max_length=50)
    Network_Area = models.CharField(max_length=100,default='EPN')

    def __str__(self):
        return self.Substn

class phFaultData(models.Model):
    GSP = models.CharField(max_length=50)
    Substn = models.CharField(max_length=50)
    NodeName = models.CharField(max_length=50)
    VoltLvl_kV = models.CharField(max_length=50)
    SysImp_R = models.CharField(max_length=50)
    SysImp_X = models.CharField(max_length=50)
    ESFC_PeakMake_kA = models.CharField(max_length=50)
    ESFC_RMSBreak_kA = models.CharField(max_length=50)
    FR_PeakMake_kA = models.CharField(max_length=50)
    FR_Break_kA = models.CharField(max_length=50)
    Network_Area = models.CharField(max_length=100,default='EPN')

    def __str__(self):
        return self.Substn

class earthFaultData(models.Model):
    GSP = models.CharField(max_length=50)
    Substn = models.CharField(max_length=50)
    NodeName = models.CharField(max_length=50)
    VoltLvl_kV = models.CharField(max_length=50)
    SysImp_R = models.CharField(max_length=50)
    SysImp_X = models.CharField(max_length=50)
    ESFC_PeakMake_kA = models.CharField(max_length=50)
    ESFC_RMSBreak_kA = models.CharField(max_length=50)
    FR_PeakMake_kA = models.CharField(max_length=50)
    FR_Break_kA = models.CharField(max_length=50)
    Network_Area = models.CharField(max_length=100,default='EPN')

    def __str__(self):
        return self.Substn

class Generation(models.Model):
    GSP = models.CharField(max_length=50)
    Substn = models.CharField(max_length=50)
    ConVolt_kV = models.CharField(max_length=50)
    InsCap_MW = models.CharField(max_length=50)
    FuelType = models.CharField(max_length=50)
    ConAcc = models.CharField(max_length=50)
    Network_Area = models.CharField(max_length=100,default='EPN')

    def __str__(self):
        return self.Substn

class InterestConnections(models.Model):
    GSP = models.CharField(max_length=50)
    Substn = models.CharField(max_length=50)
    PCVolt_kV = models.CharField(max_length=50)
    ConStat = models.CharField(max_length=50)
    Dem_TN = models.CharField(max_length=50)
    Dem_TC = models.CharField(max_length=50)
    Gen_TN = models.CharField(max_length=50)
    Gen_TC = models.CharField(max_length=50)
    Network_Area = models.CharField(max_length=100,default='EPN')

    def __str__(self):
        return self.Substn

class OppRestrictions(models.Model):
    GSP = models.CharField(max_length=50)
    Substn = models.CharField(max_length=50)
    FL_OpRes = models.CharField(max_length=50)

    def __str__(self):
        return self.Substn

class FaultData(models.Model):
    GSP = models.CharField(max_length=50)
    Substn = models.CharField(max_length=50)
    NodeName = models.CharField(max_length=50)
    VoltLvl_kV = models.CharField(max_length=50)
    ResPro_Mit_Rev = models.CharField(max_length=150)
    ActYr = models.CharField(max_length=50)

    def __str__(self):
        return self.Substn







