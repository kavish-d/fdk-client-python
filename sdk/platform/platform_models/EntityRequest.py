"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *






class EntityRequest(Schema):

    
    entity_id = fields.Str(required=False)
    
    entity_type = fields.Str(required=False)
    

