## Permissions & Groups Setup

This application uses Django's built-in permissions and groups system.

### Custom Permissions
Defined in `Article` model:
- can_view
- can_create
- can_edit
- can_delete

### Groups
- Viewers: can_view
- Editors: can_view, can_create, can_edit
- Admins: all permissions

### Enforcement
Permissions are enforced in views using `@permission_required`
with `raise_exception=True`.

### Testing
Users are assigned to groups via Django admin
and tested by logging in and accessing views.
