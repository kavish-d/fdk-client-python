"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *






class DeleteAddressResponse(Schema):

    
    id = fields.Str(required=False)
    
    is_deleted = fields.Boolean(required=False)
    

