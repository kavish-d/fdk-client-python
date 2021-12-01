"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *
from ..application_models.BaseSchema import BaseSchema



from .ConfigPage import ConfigPage




class ListSchemaItem(BaseSchema):

    
    global_config = fields.Dict(required=False)
    
    page = fields.List(fields.Nested(ConfigPage, required=False), required=False)
    
    name = fields.Str(required=False)
    

