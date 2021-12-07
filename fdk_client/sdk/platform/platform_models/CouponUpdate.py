"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema

from .RuleDefinition import RuleDefinition



from .Validity import Validity

from .Ownership import Ownership

from .CouponSchedule import CouponSchedule

from .Rule import Rule

from .State import State

from .Identifier import Identifier

from .CouponAction import CouponAction



from .CouponAuthor import CouponAuthor

from .CouponDateMeta import CouponDateMeta

from .DisplayMeta import DisplayMeta

from .Restrictions import Restrictions

from .Validation import Validation




class CouponUpdate(BaseSchema):

    
    rule_definition = fields.Nested(RuleDefinition, required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    validity = fields.Nested(Validity, required=False)
    
    ownership = fields.Nested(Ownership, required=False)
    
    _schedule = fields.Nested(CouponSchedule, required=False)
    
    rule = fields.List(fields.Nested(Rule, required=False), required=False)
    
    state = fields.Nested(State, required=False)
    
    identifiers = fields.Nested(Identifier, required=False)
    
    action = fields.Nested(CouponAction, required=False)
    
    type_slug = fields.Str(required=False)
    
    author = fields.Nested(CouponAuthor, required=False)
    
    date_meta = fields.Nested(CouponDateMeta, required=False)
    
    display_meta = fields.Nested(DisplayMeta, required=False)
    
    restrictions = fields.Nested(Restrictions, required=False)
    
    validation = fields.Nested(Validation, required=False)
    
    code = fields.Str(required=False)
    

