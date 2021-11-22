"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *






class DomainSuggestionsRequest(Schema):

    
    domain_url = fields.Str(required=False)
    
    custom = fields.Boolean(required=False)
    

