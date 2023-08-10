from django.db.models import Transform
from django.db.models.lookups import PostgresOperatorLookup

from .search import SearchVectorExact

class DataContains(PostgresOperatorLookup): ...
class ContainedBy(PostgresOperatorLookup): ...
class Overlap(PostgresOperatorLookup): ...
class HasKey(PostgresOperatorLookup): ...
class HasKeys(PostgresOperatorLookup): ...
class HasAnyKeys(HasKeys): ...
class Unaccent(Transform): ...
class SearchLookup(SearchVectorExact): ...
class TrigramSimilar(PostgresOperatorLookup): ...
class TrigramWordSimilar(PostgresOperatorLookup): ...
class TrigramStrictWordSimilar(PostgresOperatorLookup): ...
