# Healthcare Portal - System Documentation

## Overview

This is a Flask-based healthcare patient portal application that allows patients to register, log in, and manage their healthcare information securely. The application follows a traditional MVC architecture with server-side rendering using Jinja2 templates and includes comprehensive security features for handling sensitive medical data.

## System Architecture

### Backend Architecture
- **Framework**: Flask (Python web framework)
- **Database**: SQLAlchemy ORM with SQLite (default) or PostgreSQL support
- **Authentication**: Session-based authentication with password hashing using Werkzeug
- **Security**: ProxyFix middleware, secure session configuration, CSRF protection considerations
- **Validation**: Server-side form validation with custom validation classes

### Frontend Architecture
- **Template Engine**: Jinja2 templates with Flask
- **CSS Framework**: Bootstrap 5.3.2 for responsive design
- **Icons**: Font Awesome and Bootstrap Icons
- **JavaScript**: Vanilla JavaScript for client-side validation and interactions
- **Design System**: Custom healthcare-themed CSS with CSS variables

### Database Schema
- **Patient Model**: Comprehensive patient information including personal details, contact information, emergency contacts, and authentication data
- **Security Features**: Password hashing, account status tracking, session management
- **Audit Fields**: Created/updated timestamps, last login tracking

## Key Components

### Models (`models.py`)
- **Patient**: Main entity with personal information, authentication, and audit fields
- **Password Security**: Built-in password hashing and validation with healthcare-grade requirements
- **Data Validation**: Email uniqueness, phone number formatting, required field enforcement

### Forms and Validation (`forms.py`)
- **FormValidator**: Utility class for server-side validation
- **Email Validation**: Regex-based email format checking
- **Phone Validation**: International phone number support with digit-only processing
- **Password Strength**: Healthcare-compliant password requirements

### Routes (`routes.py`)
- **Authentication Flow**: Registration, login, logout with session management
- **Session Security**: 30-minute timeout, permanent sessions, activity tracking
- **Protected Routes**: Login-required decorator for secure pages
- **Dashboard**: Patient portal with profile management

### Templates
- **Base Template**: Responsive layout with navigation and security features
- **Authentication Pages**: Login and registration with client-side validation
- **Dashboard**: Patient information overview and quick actions
- **Profile Management**: Personal information editing capabilities

## Data Flow

1. **User Registration**: 
   - Form validation (client and server-side)
   - Password hashing and storage
   - Account creation with audit timestamps

2. **Authentication**:
   - Email/password verification
   - Session creation with security headers
   - Activity tracking and timeout management

3. **Session Management**:
   - 30-minute sliding window timeout
   - Secure cookie configuration
   - Cross-site protection measures

4. **Data Access**:
   - Login-required routes protection
   - Patient-specific data isolation
   - Profile update capabilities

## External Dependencies

### Python Packages
- **Flask**: Web framework and extensions
- **SQLAlchemy**: Database ORM
- **Werkzeug**: WSGI utilities and password hashing
- **Logging**: Built-in Python logging for debugging

### Frontend Libraries
- **Bootstrap 5.3.2**: UI framework from CDN
- **Font Awesome 6.4.0**: Icon library from CDN
- **Bootstrap Icons**: Additional icon set

### Database Support
- **SQLite**: Default development database
- **PostgreSQL**: Production database (via DATABASE_URL environment variable)

## Deployment Strategy

### Environment Configuration
- **Development**: SQLite database, debug mode enabled
- **Production**: Environment-based configuration with secure secrets
- **Database**: Configurable via DATABASE_URL environment variable
- **Security**: Session secrets and security headers for production deployment

### Security Considerations
- **Session Security**: HTTPOnly, Secure, SameSite cookie attributes
- **Password Policy**: Healthcare-grade password requirements
- **Database Security**: Connection pooling and health checks
- **WSGI**: ProxyFix for proper header handling behind reverse proxies

### Application Structure
- **Entry Point**: `main.py` starts the Flask development server
- **Application Factory**: `app.py` contains Flask app configuration
- **Modular Design**: Separated routes, models, forms, and static assets

## Development Environment

### VS Code Configuration
- **Settings**: Configured for Python development with Flask support
- **Launch Configurations**: Flask development server and Gunicorn options
- **Extensions**: Recommended Python, Jinja, and web development extensions
- **Tasks**: Automated tasks for running server, database operations, and code formatting
- **Debugging**: Ready-to-use debug configurations for Flask applications

### Project Structure
- **Documentation**: Comprehensive README, CONTRIBUTING guidelines, and CHANGELOG
- **Environment**: Template .env file with all required variables
- **Git**: Proper .gitignore for Python/Flask projects
- **Code Quality**: Black formatting, Pylint linting, and type checking enabled

## Recent Changes

### July 01, 2025 - VS Code Development Setup
- Added comprehensive README.md with installation and usage instructions
- Created VS Code workspace configuration (.vscode/ folder)
- Set up launch.json for Flask debugging
- Added tasks.json for common development operations
- Created CONTRIBUTING.md with development guidelines
- Added CHANGELOG.md for version tracking
- Set up .env.example template for environment variables
- Created .gitignore for proper version control
- Added recommended VS Code extensions configuration

### Key Improvements
- **Developer Experience**: Full VS Code integration with debugging, tasks, and formatting
- **Documentation**: Professional-grade documentation for development and deployment
- **Code Quality**: Automated formatting and linting setup
- **Environment Management**: Clear separation of development and production configs
- **Accessibility**: Enhanced form validation and ARIA support

## Changelog

```
Changelog:
- July 01, 2025. Initial healthcare portal setup with patient registration and login
- July 01, 2025. Added comprehensive VS Code development environment and documentation
```

## User Preferences

```
Preferred communication style: Simple, everyday language.
Development Environment: VS Code with Python extensions
Code Style: Black formatting, 88-character line length
Documentation: Comprehensive README and contributing guidelines preferred
```