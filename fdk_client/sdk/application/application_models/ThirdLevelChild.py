"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *
from ..application_models.BaseSchema import BaseSchema







from .ImageUrls import ImageUrls

from .ActionPage import ActionPage






class ThirdLevelChild(BaseSchema):

    
    _custom_json = fields.Dict(required=False)
    
    childs = fields.List(fields.Dict(required=False), required=False)
    
    slug = fields.Str(required=False)
    
    banners = fields.Nested(ImageUrls, required=False)
    
    action = fields.Nested(ActionPage, required=False)
    
    uid = fields.Int(required=False)
    
    name = fields.Str(required=False)
    
