"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *




class MetaSchema(Schema):

    
    fynd_default = fields.Boolean(required=False)
    

