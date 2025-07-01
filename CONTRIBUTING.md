# Contributing to Healthcare Portal

Thank you for your interest in contributing to the Healthcare Portal project! This guide will help you get started with development and ensure your contributions align with our project standards.

## Getting Started

### Prerequisites
- Python 3.11 or higher
- PostgreSQL 12 or higher
- VS Code (recommended) with Python extension
- Git for version control

### Development Setup

1. **Fork and clone the repository**
   ```bash
   git clone https://github.com/your-username/healthcare-portal.git
   cd healthcare-portal
   ```

2. **Set up virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   ```bash
   cp .env.example .env
   # Edit .env with your database credentials
   ```

5. **Initialize database**
   ```bash
   python -c "from app import app, db; app.app_context().push(); db.create_all()"
   ```

## Development Guidelines

### Code Style

- **Python**: Follow PEP 8 guidelines
- **Line Length**: Maximum 88 characters (Black formatter standard)
- **Imports**: Use absolute imports, organize with isort
- **Docstrings**: Use Google-style docstrings for functions and classes
- **Type Hints**: Include type hints for function parameters and returns

### File Organization

```
healthcare-portal/
├── app.py              # Flask app configuration
├── main.py             # Application entry point
├── models.py           # Database models
├── routes.py           # Route handlers
├── forms.py            # Form validation
├── templates/          # HTML templates
├── static/             # CSS, JS, images
└── tests/              # Test files
```

### Database Guidelines

- Use SQLAlchemy ORM for all database operations
- Never write raw SQL queries
- Include proper foreign key relationships
- Add database indexes for frequently queried fields
- Use migrations for schema changes

### Security Requirements

- All user inputs must be validated server-side
- Use parameterized queries (SQLAlchemy handles this)
- Hash all passwords using Werkzeug's secure methods
- Validate CSRF tokens for state-changing operations
- Follow HIPAA compliance guidelines for patient data

## Making Changes

### Branch Naming Convention

- `feature/description` - New features
- `bugfix/description` - Bug fixes
- `hotfix/description` - Critical fixes
- `docs/description` - Documentation updates

### Commit Messages

Use conventional commit format:
```
type(scope): description

[optional body]

[optional footer]
```

Examples:
- `feat(auth): add password strength validation`
- `fix(profile): correct phone number formatting`
- `docs(readme): update installation instructions`

### Pull Request Process

1. **Create a feature branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. **Make your changes**
   - Write clean, documented code
   - Add tests for new functionality
   - Update documentation as needed

3. **Test your changes**
   ```bash
   # Run manual tests
   python main.py
   
   # Test all forms and functionality
   # Verify database operations
   # Check responsive design
   ```

4. **Commit and push**
   ```bash
   git add .
   git commit -m "feat(scope): description"
   git push origin feature/your-feature-name
   ```

5. **Create Pull Request**
   - Use the provided PR template
   - Include screenshots for UI changes
   - Reference any related issues

## Testing

### Manual Testing

Before submitting a PR, test these scenarios:

**Registration Flow**
- [ ] Valid registration with all fields
- [ ] Registration with invalid email
- [ ] Registration with weak password
- [ ] Registration with duplicate email
- [ ] Form validation messages display correctly

**Login Flow**
- [ ] Valid login credentials
- [ ] Invalid email/password combinations
- [ ] Account lockout (if implemented)
- [ ] Session timeout functionality

**Profile Management**
- [ ] Update personal information
- [ ] Change password
- [ ] Emergency contact updates
- [ ] Form validation on updates

**Responsive Design**
- [ ] Desktop browsers (Chrome, Firefox, Safari)
- [ ] Mobile devices (various screen sizes)
- [ ] Tablet devices

### Automated Testing

We encourage adding automated tests:

```python
# Example test structure
def test_patient_registration():
    """Test patient registration with valid data."""
    # Implementation here
    pass

def test_login_invalid_credentials():
    """Test login with invalid credentials."""
    # Implementation here
    pass
```

## Security Considerations

### HIPAA Compliance

- Never log sensitive patient information
- Encrypt data in transit and at rest
- Implement proper access controls
- Follow minimum necessary principle
- Document all security measures

### Data Handling

- Validate all inputs (client and server-side)
- Sanitize data before database storage
- Use secure session management
- Implement proper error handling
- Log security events appropriately

## Documentation

### Code Documentation

- Add docstrings to all functions and classes
- Comment complex business logic
- Update inline documentation for changes
- Keep README.md current

### User Documentation

- Update help text for form changes
- Document new features in user guides
- Provide clear error messages
- Include accessibility information

## Issue Reporting

### Bug Reports

Include the following information:
- Operating system and browser
- Python version
- Steps to reproduce
- Expected vs actual behavior
- Screenshots if applicable
- Console error messages

### Feature Requests

Include the following information:
- Use case description
- Proposed solution
- Alternative solutions considered
- Impact on existing functionality
- HIPAA compliance considerations

## Code Review Process

### What We Look For

- **Functionality**: Does the code work as intended?
- **Security**: Are there any security vulnerabilities?
- **Performance**: Is the code efficient?
- **Maintainability**: Is the code easy to understand and modify?
- **Compliance**: Does it meet healthcare data standards?

### Review Checklist

- [ ] Code follows style guidelines
- [ ] All tests pass
- [ ] Documentation is updated
- [ ] Security considerations addressed
- [ ] Performance impact assessed
- [ ] HIPAA compliance maintained

## Getting Help

### Resources

- [Flask Documentation](https://flask.palletsprojects.com/)
- [SQLAlchemy Documentation](https://docs.sqlalchemy.org/)
- [Bootstrap Documentation](https://getbootstrap.com/docs/)
- [HIPAA Guidelines](https://www.hhs.gov/hipaa/)

### Communication

- Create GitHub issues for bugs and features
- Use clear, descriptive titles
- Provide detailed descriptions
- Include relevant code snippets

## License

By contributing, you agree that your contributions will be licensed under the same license as the project.

## Recognition

Contributors will be recognized in the project documentation and release notes.

Thank you for helping make Healthcare Portal better!