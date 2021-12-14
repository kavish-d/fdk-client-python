"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *
from ..application_models.BaseSchema import BaseSchema






class Url(BaseSchema):
    # Feedback swagger.json

    
    main = fields.Str(required=False)
    
    thumbnail = fields.Str(required=False)
    

