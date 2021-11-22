"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *




class AttributeMasterDetails(Schema):

    
    display_type = fields.Str(required=False)
    

