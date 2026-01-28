# ALX Django Project: LibraryProject

This project contains multiple apps including:

- **bookshelf**: Manages books with CRUD operations, permissions, and groups.
- **accounts**: Manages user authentication and profiles (Task 0).

## Task 1: Managing Permissions and Groups

- Book model has custom permissions: can_view, can_create, can_edit, can_delete.
- Groups configured in Django admin: Viewers, Editors, Admins.
- CRUD views are protected with @permission_required decorators.
- Documentation is included in `bookshelf/README.md`.

## How to Run

1. Install dependencies:
