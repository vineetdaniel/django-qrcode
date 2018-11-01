# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.core.files import File

from django.db import models
import qrcode
from django.contrib.staticfiles.templatetags.staticfiles import static

# Create your models here.
class Qrdata(models.Model):
    tml_po_number = models.BigIntegerField()
    order_item_no = models.IntegerField()
    field3 =  models.IntegerField()
    field4 =  models.IntegerField()
    field5 =  models.IntegerField()
    field6 =  models.IntegerField()
    field7 =  models.IntegerField()
    field8 =  models.IntegerField()
    field9 =  models.IntegerField()
    field10 =  models.IntegerField()
    field11 =  models.IntegerField()
    field12 =  models.IntegerField()
    field13 =  models.IntegerField()
    field14 =  models.IntegerField()
    field15 = models.IntegerField()
    field16 =  models.IntegerField()
    field17 =  models.IntegerField()
    field18 =  models.IntegerField()
    image = models.ImageField(blank=True, upload_to="qrcodes")

    def save(self, *args, **kwargs):
        o_no = str(self.order_item_no)
        fname = str(self.order_item_no) + ".png"
        path =  static(fname)
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,   
            )
        data = {
            "field1" : self.field3
        }
        qr.add_data("field1" + str(self.field3) + "field2" + str(self.field10))
        qr.make(fit=True)

        img = qr.make_image()

        img.save(path, 'PNG')
        destination_file = open(path, 'rb')
        self.image.save(o_no+".png", File(destination_file), save=False)
        destination_file.close()

        # self.image.save = path
        super(Qrdata, self).save(*args, **kwargs)
    
    
    # def __str__(self):
    #     return self.tml_po_number


