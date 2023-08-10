from typing import Any, TypeVar

from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import AnonymousUser, Permission
from django.db.models import QuerySet
from django.db.models.base import Model
from django.http.request import HttpRequest
from typing_extensions import TypeAlias

_AnyUser: TypeAlias = AbstractBaseUser | AnonymousUser

UserModel: Any

class BaseBackend:
    def authenticate(self, request: HttpRequest | None, **kwargs: Any) -> AbstractBaseUser | None: ...
    def get_user(self, user_id: int) -> AbstractBaseUser | None: ...
    def get_user_permissions(self, user_obj: _AnyUser, obj: Model | None = ...) -> set[str]: ...
    def get_group_permissions(self, user_obj: _AnyUser, obj: Model | None = ...) -> set[str]: ...
    def get_all_permissions(self, user_obj: _AnyUser, obj: Model | None = ...) -> set[str]: ...
    def has_perm(self, user_obj: _AnyUser, perm: str, obj: Model | None = ...) -> bool: ...

class ModelBackend(BaseBackend):
    def authenticate(
        self, request: HttpRequest | None, username: str | None = ..., password: str | None = ..., **kwargs: Any
    ) -> AbstractBaseUser | None: ...
    def has_module_perms(self, user_obj: _AnyUser, app_label: str) -> bool: ...
    def user_can_authenticate(self, user: _AnyUser | None) -> bool: ...
    def with_perm(
        self,
        perm: str | Permission,
        is_active: bool = ...,
        include_superusers: bool = ...,
        obj: Model | None = ...,
    ) -> QuerySet[AbstractBaseUser]: ...

class AllowAllUsersModelBackend(ModelBackend): ...

_U = TypeVar("_U", bound=AbstractBaseUser)

class RemoteUserBackend(ModelBackend):
    create_unknown_user: bool
    def clean_username(self, username: str) -> str: ...
    def configure_user(self, request: HttpRequest, user: _U) -> _U: ...

class AllowAllUsersRemoteUserBackend(RemoteUserBackend): ...
