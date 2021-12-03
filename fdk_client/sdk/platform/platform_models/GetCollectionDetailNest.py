"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema





















from .Media1 import Media1







from .ActionPage import ActionPage





from .ImageUrls import ImageUrls




class GetCollectionDetailNest(BaseSchema):

    
    meta = fields.Dict(required=False)
    
    tag = fields.List(fields.Str(required=False), required=False)
    
    cron = fields.Dict(required=False)
    
    visible_facets_keys = fields.List(fields.Str(required=False), required=False)
    
    badge = fields.Dict(required=False)
    
    is_active = fields.Boolean(required=False)
    
    allow_facets = fields.Boolean(required=False)
    
    _schedule = fields.Dict(required=False)
    
    name = fields.Str(required=False)
    
    query = fields.Dict(required=False)
    
    logo = fields.Nested(Media1, required=False)
    
    uid = fields.Str(required=False)
    
    allow_sort = fields.Boolean(required=False)
    
    slug = fields.Str(required=False)
    
    action = fields.Nested(ActionPage, required=False)
    
    type = fields.Str(required=False)
    
    description = fields.Str(required=False)
    
    banners = fields.Nested(ImageUrls, required=False)
    
    app_id = fields.Str(required=False)
    
