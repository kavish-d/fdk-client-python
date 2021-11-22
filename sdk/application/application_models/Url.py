"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *






class Url(Schema):

    
    main = fields.Str(required=False)
    
    thumbnail = fields.Str(required=False)
    

