from collections.abc import Iterable
from typing import Any

from django.core.management.base import BaseCommand
from django.db.backends.base.base import BaseDatabaseWrapper

class Command(BaseCommand):
    stealth_options: tuple[str]
    db_module: str
    def handle_inspection(self, options: dict[str, Any]) -> Iterable[str]: ...
    def normalize_col_name(
        self, col_name: str, used_column_names: list[str], is_relation: bool
    ) -> tuple[str, dict[str, str], list[str]]: ...
    def get_field_type(
        self, connection: BaseDatabaseWrapper, table_name: str, row: Any
    ) -> tuple[str, dict[str, Any], list[str]]: ...
    def get_meta(
        self, table_name: str, constraints: Any, column_to_field_name: Any, is_view: Any, is_partition: Any
    ) -> list[str]: ...
