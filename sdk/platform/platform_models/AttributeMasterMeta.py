"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *

from .AttributeMasterMandatoryDetails import AttributeMasterMandatoryDetails




class AttributeMasterMeta(Schema):

    
    mandatory_details = fields.Nested(AttributeMasterMandatoryDetails, required=False)
    
    enriched = fields.Boolean(required=False)
    

