"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *




class Google(Schema):

    
    app_id = fields.Str(required=False)
    

