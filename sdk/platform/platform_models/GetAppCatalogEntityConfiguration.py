"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *



from .EntityConfiguration import EntityConfiguration


class GetAppCatalogEntityConfiguration(Schema):

    
    is_default = fields.Boolean(required=False)
    
    data = fields.Nested(EntityConfiguration, required=False)
    

