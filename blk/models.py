# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models



class TbAgreementInfo(models.Model):
    agid = models.AutoField(db_column='AgID', primary_key=True)  # Field name made lowercase.
    matrelaid = models.CharField(db_column='MatRelaID', max_length=100, blank=True, null=True)  # Field name made lowercase.
    value = models.DecimalField(db_column='Value', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    validity = models.IntegerField(db_column='Validity', blank=True, null=True)  # Field name made lowercase.
    createtime = models.DateTimeField(db_column='CreateTime', blank=True, null=True)  # Field name made lowercase.
    updatetime = models.DateTimeField(db_column='UpdateTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tb_agreement_info'


class TbCashInfo(models.Model):
    ciid = models.AutoField(db_column='CiID', primary_key=True)  # Field name made lowercase.
    tokennumber = models.IntegerField(db_column='TokenNumber', blank=True, null=True)  # Field name made lowercase.
    cashnumber = models.DecimalField(db_column='CashNumber', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    cashunit = models.CharField(db_column='CashUnit', max_length=20, blank=True, null=True)  # Field name made lowercase.
    builddate = models.DateTimeField(db_column='BuildDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tb_cash_info'


class TbCashRecord(models.Model):
    crid = models.AutoField(db_column='CrID', primary_key=True)  # Field name made lowercase.
    cashownertype = models.CharField(db_column='CashOwnerType', max_length=100, blank=True, null=True)  # Field name made lowercase.
    cashownerid = models.CharField(db_column='CashOwnerID', max_length=100, blank=True, null=True)  # Field name made lowercase.
    cashrecordnumber = models.DecimalField(db_column='CashRecordNumber', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    cashdate = models.DateTimeField(db_column='CashDate', blank=True, null=True)  # Field name made lowercase.
    cashps = models.CharField(db_column='CashPs', max_length=200, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tb_cash_record'


class TbCompanyInfo(models.Model):
    coid = models.AutoField(db_column='CoID', primary_key=True)  # Field name made lowercase.
    coname = models.CharField(db_column='CoName', max_length=100)  # Field name made lowercase.
    cotype = models.CharField(db_column='CoType', max_length=100, blank=True, null=True)  # Field name made lowercase.
    cops = models.CharField(db_column='CoPs', max_length=200, blank=True, null=True)  # Field name made lowercase.
    costatus = models.CharField(db_column='CoStatus', max_length=30, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tb_company_info'


class TbMatCirculation(models.Model):
    mcid = models.AutoField(db_column='McID', primary_key=True)  # Field name made lowercase.
    mid = models.IntegerField(db_column='MID', blank=True, null=True)  # Field name made lowercase.
    mcsn = models.CharField(db_column='McSn', max_length=300, blank=True, null=True)  # Field name made lowercase.
    mcoperate = models.CharField(db_column='McOperate', max_length=200, blank=True, null=True)  # Field name made lowercase.
    mps = models.CharField(db_column='MPs', max_length=200, blank=True, null=True)  # Field name made lowercase.
    mcinittime = models.DateTimeField(db_column='McInitTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tb_mat_circulation'


class TbMaterialInfo(models.Model):
    miid = models.AutoField(db_column='MiID', primary_key=True)  # Field name made lowercase.
    mname = models.CharField(db_column='MName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    mdescription = models.CharField(db_column='MDescription', max_length=200, blank=True, null=True)  # Field name made lowercase.
    munit = models.CharField(db_column='MUnit', max_length=20, blank=True, null=True)  # Field name made lowercase.
    mps = models.CharField(db_column='MPs', max_length=200, blank=True, null=True)  # Field name made lowercase.
    mstatus = models.CharField(db_column='MStatus', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tb_material_info'


class TbPeopleInfo(models.Model):
    pid = models.AutoField(db_column='PID', primary_key=True)  # Field name made lowercase.
    pname = models.CharField(db_column='PName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    pmail = models.CharField(db_column='PMail', max_length=100, blank=True, null=True)  # Field name made lowercase.
    logonpass = models.CharField(db_column='LogonPass', max_length=100, blank=True, null=True)  # Field name made lowercase.
    pstatus = models.CharField(db_column='PStatus', max_length=20, blank=True, null=True)  # Field name made lowercase.
    pps = models.CharField(db_column='PPs', max_length=200, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tb_people_info'


class TbTokenInfo(models.Model):
    tiid = models.AutoField(db_column='TiID', primary_key=True)  # Field name made lowercase.
    ownerid = models.CharField(db_column='OwnerID', max_length=100, blank=True, null=True)  # Field name made lowercase.
    ownertype = models.CharField(db_column='OwnerType', max_length=100, blank=True, null=True)  # Field name made lowercase.
    ownercoid = models.CharField(db_column='OwnerCoID', max_length=30, blank=True, null=True)  # Field name made lowercase.
    holdnumber = models.CharField(db_column='HoldNumber', max_length=100, blank=True, null=True)  # Field name made lowercase.
    tips = models.CharField(db_column='TiPs', max_length=200, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tb_token_info'
