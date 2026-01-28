# Bookshelf Permissions & Groups

This app implements custom permissions and groups for the Book model.

## Permissions
- can_view
- can_create
- can_edit
- can_delete

## Groups
- Viewers → can_view
- Editors → can_view, can_create, can_edit
- Admins → all permissions

## Enforcement
Views are protected using @permission_required decorators with raise_exception=True.
