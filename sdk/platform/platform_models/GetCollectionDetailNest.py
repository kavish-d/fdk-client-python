"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *



from .ImageUrls import ImageUrls























from .Media1 import Media1









from .ActionPage import ActionPage


class GetCollectionDetailNest(Schema):

    
    allow_facets = fields.Boolean(required=False)
    
    banners = fields.Nested(ImageUrls, required=False)
    
    app_id = fields.Str(required=False)
    
    is_active = fields.Boolean(required=False)
    
    _schedule = fields.Dict(required=False)
    
    badge = fields.Dict(required=False)
    
    cron = fields.Dict(required=False)
    
    query = fields.Dict(required=False)
    
    description = fields.Str(required=False)
    
    visible_facets_keys = fields.List(fields.Str(required=False), required=False)
    
    allow_sort = fields.Boolean(required=False)
    
    tag = fields.List(fields.Str(required=False), required=False)
    
    slug = fields.Str(required=False)
    
    logo = fields.Nested(Media1, required=False)
    
    name = fields.Str(required=False)
    
    type = fields.Str(required=False)
    
    uid = fields.Str(required=False)
    
    meta = fields.Dict(required=False)
    
    action = fields.Nested(ActionPage, required=False)
    

