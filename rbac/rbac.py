# rbac/rbac.py

class Permission:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"Permission({self.name})"


class Role:
    def __init__(self, name):
        self.name = name
        self.permissions = set()

    def add_permission(self, permission):
        self.permissions.add(permission)

    def remove_permission(self, permission):
        self.permissions.discard(permission)

    def has_permission(self, permission):
        return permission in self.permissions

    def __repr__(self):
        return f"Role({self.name}, permissions={list(self.permissions)})"


class User:
    def __init__(self, username):
        self.username = username
        self.roles = set()

    def assign_role(self, role):
        self.roles.add(role)

    def revoke_role(self, role):
        self.roles.discard(role)

    def has_permission(self, permission):
        for role in self.roles:
            if role.has_permission(permission):
                return True
        return False

    def __repr__(self):
        return f"User({self.username}, roles={list(self.roles)})"


class Resource:
    def __init__(self, name):
        self.name = name
        self.permissions = {}

    def set_permission(self, role, permission):
        if role not in self.permissions:
            self.permissions[role] = set()
        self.permissions[role].add(permission)

    def remove_permission(self, role, permission):
        if role in self.permissions:
            self.permissions[role].discard(permission)
            if not self.permissions[role]:
                del self.permissions[role]

    def is_accessible_by(self, user, permission):
        for role in user.roles:
            if role in self.permissions and permission in self.permissions[role]:
                return True
        return False

    def __repr__(self):
        return f"Resource({self.name}, permissions={self.permissions})"
