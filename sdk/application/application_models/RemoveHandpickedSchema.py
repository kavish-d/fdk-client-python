"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *
from ..application_models.BaseSchema import BaseSchema




class RemoveHandpickedSchema(BaseSchema):

    
    tags = fields.List(fields.Str(required=False), required=False)
    

