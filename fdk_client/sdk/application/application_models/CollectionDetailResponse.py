"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *
from ..application_models.BaseSchema import BaseSchema











from .ImageUrls import ImageUrls

















from .Media import Media






class CollectionDetailResponse(BaseSchema):
    # Catalog swagger.json

    
    description = fields.Str(required=False)
    
    tag = fields.List(fields.Str(required=False), required=False)
    
    type = fields.Str(required=False)
    
    allow_sort = fields.Boolean(required=False)
    
    allow_facets = fields.Boolean(required=False)
    
    banners = fields.Nested(ImageUrls, required=False)
    
    is_active = fields.Boolean(required=False)
    
    cron = fields.Dict(required=False)
    
    slug = fields.Str(required=False)
    
    meta = fields.Dict(required=False)
    
    query = fields.Dict(required=False)
    
    badge = fields.Dict(required=False)
    
    _schedule = fields.Dict(required=False)
    
    visible_facets_keys = fields.List(fields.Str(required=False), required=False)
    
    logo = fields.Nested(Media, required=False)
    
    name = fields.Str(required=False)
    
    app_id = fields.Str(required=False)
    

