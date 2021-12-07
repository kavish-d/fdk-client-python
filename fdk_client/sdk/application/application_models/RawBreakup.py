"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *
from ..application_models.BaseSchema import BaseSchema


























class RawBreakup(BaseSchema):

    
    total = fields.Float(required=False)
    
    convenience_fee = fields.Float(required=False)
    
    delivery_charge = fields.Float(required=False)
    
    you_saved = fields.Float(required=False)
    
    gst_charges = fields.Float(required=False)
    
    coupon = fields.Float(required=False)
    
    subtotal = fields.Float(required=False)
    
    mrp_total = fields.Float(required=False)
    
    vog = fields.Float(required=False)
    
    fynd_cash = fields.Float(required=False)
    
    cod_charge = fields.Float(required=False)
    
    discount = fields.Float(required=False)
    

