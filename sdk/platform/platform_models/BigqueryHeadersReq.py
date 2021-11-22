"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *






class BigqueryHeadersReq(Schema):

    
    query = fields.Str(required=False)
    
    type = fields.Str(required=False)
    

