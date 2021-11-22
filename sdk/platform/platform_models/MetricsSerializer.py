"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *

from .DocumentsObj import DocumentsObj





from .DocumentsObj import DocumentsObj

from .DocumentsObj import DocumentsObj

from .DocumentsObj import DocumentsObj

from .DocumentsObj import DocumentsObj


class MetricsSerializer(Schema):

    
    store = fields.Nested(DocumentsObj, required=False)
    
    uid = fields.Int(required=False)
    
    stage = fields.Str(required=False)
    
    product = fields.Nested(DocumentsObj, required=False)
    
    company_documents = fields.Nested(DocumentsObj, required=False)
    
    store_documents = fields.Nested(DocumentsObj, required=False)
    
    brand = fields.Nested(DocumentsObj, required=False)
    

