"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *






class DocumentsObj(Schema):

    
    pending = fields.Int(required=False)
    
    verified = fields.Int(required=False)
    

