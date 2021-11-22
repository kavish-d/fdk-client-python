"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *

from .LogisticMeta import LogisticMeta

from .LogisticParents import LogisticParents





from .LogisticError import LogisticError






class LogisticPincodeData(Schema):

    
    meta = fields.Nested(LogisticMeta, required=False)
    
    parents = fields.List(fields.Nested(LogisticParents, required=False), required=False)
    
    sub_type = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    error = fields.Nested(LogisticError, required=False)
    
    uid = fields.Str(required=False)
    
    display_name = fields.Str(required=False)
    

