"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *
from ..application_models.BaseSchema import BaseSchema

from .Cloud import Cloud









from .Url import Url


class MediaMeta(BaseSchema):

    
    cloud = fields.Nested(Cloud, required=False)
    
    comment = fields.List(fields.Str(required=False), required=False)
    
    description = fields.Str(required=False)
    
    id = fields.Str(required=False)
    
    type = fields.Str(required=False)
    
    url = fields.Nested(Url, required=False)
    
