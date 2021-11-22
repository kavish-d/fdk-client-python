"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *






class AvailablePageUserPredicate(Schema):

    
    authenticated = fields.Boolean(required=False)
    
    anonymous = fields.Boolean(required=False)
    

