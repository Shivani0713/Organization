**Organization Management System API**
A Django REST API project for managing organizations and their members with JWT-based authentication and role-based permissions.

**Objective**
Build a secure and fully functional **Organization Management System** with:
- Secure password handling
- JWT-based authentication
- Full CRUD for organizations and members
- Role-based access control

**Features**
1. User Authentication
- Signup API (Register with email & password)
- Login API (Returns JWT access and refresh tokens)
- Logout API (Token blacklist)
- Django's password hashing for secure password storage

2. JWT Token Handling
- JWT (access/refresh) using `djangorestframework-simplejwt`
- All APIs protected with JWT
- Custom permissions for role-based access

3. Models
- User: Custom user model using email as the username
- Organization: Represents an organization entity
- Member: A user associated with an organization

4. Permissions
- Authenticated users only
- Organization Admins can:
   - Add/update/delete organizations
   - Add/remove members
- Members can:
  - View only their own organization


## Tech Stack
- Python 3.x
- Django 5.x
- Django REST Framework
- SimpleJWT (Token-based Authentication)
- SQLite / PostgreSQL (default: SQLite)

