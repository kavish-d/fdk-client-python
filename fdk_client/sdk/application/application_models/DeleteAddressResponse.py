"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *
from ..application_models.BaseSchema import BaseSchema






class DeleteAddressResponse(BaseSchema):

    
    id = fields.Str(required=False)
    
    is_deleted = fields.Boolean(required=False)
    

