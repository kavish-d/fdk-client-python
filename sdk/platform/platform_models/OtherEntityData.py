"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *




class OtherEntityData(Schema):

    
    article_identifier = fields.Str(required=False)
    

