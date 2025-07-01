# Healthcare Portal

A secure patient registration and login system built with Flask and PostgreSQL, designed for healthcare providers to manage patient information safely and efficiently.

## Features

### 🔐 Security & Compliance
- **HIPAA-compliant** patient data handling
- **Secure password hashing** using Werkzeug
- **Session management** with 30-minute timeout
- **SSL-ready** configuration for production
- **Input validation** on both client and server side

### 👤 Patient Management
- **Patient Registration** with comprehensive form validation
- **Secure Login System** with account status tracking
- **Profile Management** with editable contact information
- **Emergency Contact** information storage
- **Password Change** functionality with strength validation

### 🎨 User Interface
- **Responsive Design** using Bootstrap 5.3.2
- **Healthcare-themed** custom CSS styling
- **Accessibility features** with ARIA labels and keyboard navigation
- **Mobile-friendly** design for all devices
- **Professional healthcare** color scheme and icons

### 🛠️ Technical Features
- **Flask** web framework with SQLAlchemy ORM
- **PostgreSQL** database with connection pooling
- **Real-time form validation** with JavaScript
- **Error handling** with user-friendly messages
- **Health check endpoint** for monitoring
- **Logging system** for debugging and audit trails

## Quick Start

### Prerequisites
- Python 3.11+
- PostgreSQL database
- Environment variables (see Configuration section)

### Installation

#### Option 1: Automated Setup (Recommended)

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd healthcare-portal
   ```

2. **Run the setup script**
   ```bash
   python setup-local.py
   ```

   This script will:
   - Create a virtual environment
   - Install all dependencies from `requirements-local.txt`
   - Set up environment variables
   - Initialize the database
   - Configure VS Code settings

3. **Activate virtual environment and start**
   ```bash
   # Windows
   venv\Scripts\activate
   
   # macOS/Linux
   source venv/bin/activate
   
   # Start the application
   python main.py
   ```

#### Option 2: Manual Setup

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd healthcare-portal
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   
   # Activate it
   # Windows: venv\Scripts\activate
   # macOS/Linux: source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements-local.txt
   ```

4. **Set up environment variables**
   ```bash
   # Copy the template
   cp .env.example .env
   
   # Edit .env with your settings
   # For quick start, SQLite is pre-configured
   ```

5. **Initialize the database**
   ```bash
   python -c "from app import app, db; app.app_context().push(); db.create_all()"
   ```

6. **Run the application**
   ```bash
   python main.py
   ```

The application will be available at `http://localhost:5000`

## Project Structure

```
healthcare-portal/
├── app.py                 # Flask app configuration
├── main.py               # Application entry point
├── models.py             # Database models (Patient)
├── routes.py             # Route handlers and business logic
├── forms.py              # Form validation classes
├── requirements.txt      # Python dependencies
├── replit.md            # Project documentation
├── templates/           # Jinja2 HTML templates
│   ├── base.html        # Base template with navigation
│   ├── index.html       # Landing page
│   ├── login.html       # Patient login form
│   ├── register.html    # Patient registration form
│   ├── dashboard.html   # Patient dashboard
│   └── profile.html     # Profile management
└── static/              # Static assets
    ├── css/
    │   └── healthcare.css  # Custom healthcare styling
    └── js/
        └── validation.js   # Client-side form validation
```

## Configuration

### Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `DATABASE_URL` | PostgreSQL connection string | Required |
| `SESSION_SECRET` | Secret key for session encryption | Required |
| `FLASK_ENV` | Environment (development/production) | development |

### Database Configuration

The application uses PostgreSQL with the following optimizations:
- Connection pooling with 5-minute recycle
- Pre-ping for connection health checks
- Automatic table creation on startup

## Development

### VS Code Setup

1. **Install recommended extensions:**
   - Python
   - Pylance
   - Flask Snippets
   - HTML CSS Support
   - Bootstrap 5 Quick Snippets

2. **Create `.vscode/settings.json`:**
   ```json
   {
     "python.defaultInterpreterPath": "./venv/bin/python",
     "python.linting.enabled": true,
     "python.linting.pylintEnabled": true,
     "python.formatting.provider": "black",
     "files.associations": {
       "*.html": "jinja-html"
     }
   }
   ```

3. **Create `.vscode/launch.json` for debugging:**
   ```json
   {
     "version": "0.2.0",
     "configurations": [
       {
         "name": "Flask App",
         "type": "python",
         "request": "launch",
         "program": "main.py",
         "env": {
           "FLASK_ENV": "development",
           "DATABASE_URL": "postgresql://localhost/healthcare_dev"
         },
         "console": "integratedTerminal"
       }
     ]
   }
   ```

### Running in Development

```bash
# Install dependencies
pip install -r requirements.txt

# Set environment variables
export DATABASE_URL="postgresql://localhost/healthcare_dev"
export SESSION_SECRET="dev-secret-key"

# Run with debug mode
python main.py
```

### Database Management

```bash
# Create all tables
python -c "from app import app, db; app.app_context().push(); db.create_all()"

# Drop all tables (CAUTION: This will delete all data)
python -c "from app import app, db; app.app_context().push(); db.drop_all()"

# Interactive Python shell with app context
python -c "from app import app; app.app_context().push(); import models"
```

## Security Features

### Password Requirements
- Minimum 8 characters
- At least one uppercase letter
- At least one lowercase letter
- At least one number
- At least one special character

### Session Security
- HTTPOnly cookies
- Secure flag in production
- SameSite protection
- 30-minute timeout with activity tracking

### Data Protection
- All passwords are hashed using Werkzeug's secure methods
- Email uniqueness enforcement
- SQL injection protection through SQLAlchemy ORM
- XSS protection through Jinja2 auto-escaping

## API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/` | GET | Landing page or redirect to dashboard |
| `/register` | GET, POST | Patient registration |
| `/login` | GET, POST | Patient login |
| `/logout` | GET | User logout |
| `/dashboard` | GET | Patient dashboard (protected) |
| `/profile` | GET, POST | Profile management (protected) |
| `/change-password` | POST | Password change (protected) |
| `/health` | GET | Health check endpoint |

## Testing

### Manual Testing Checklist

- [ ] Patient can register with valid information
- [ ] Registration form validates all required fields
- [ ] Password strength requirements are enforced
- [ ] Email uniqueness is validated
- [ ] Patient can log in with correct credentials
- [ ] Invalid login attempts are rejected
- [ ] Session timeout works after 30 minutes
- [ ] Profile information can be updated
- [ ] Password can be changed securely
- [ ] Emergency contact information is stored correctly

### Browser Testing
- [ ] Chrome/Chromium
- [ ] Firefox
- [ ] Safari
- [ ] Mobile browsers (responsive design)

## Deployment

### Production Checklist

1. **Environment Setup**
   - [ ] Set strong `SESSION_SECRET`
   - [ ] Configure production `DATABASE_URL`
   - [ ] Enable SSL/HTTPS
   - [ ] Set secure cookie flags

2. **Security Configuration**
   - [ ] Review CORS settings
   - [ ] Configure firewall rules
   - [ ] Set up database backups
   - [ ] Enable audit logging

3. **Performance**
   - [ ] Configure reverse proxy (nginx)
   - [ ] Set up database connection pooling
   - [ ] Enable gzip compression
   - [ ] Configure static file serving

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Code Style
- Follow PEP 8 for Python code
- Use meaningful variable and function names
- Add docstrings to all functions and classes
- Keep functions small and focused
- Write tests for new features

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Support

For support and questions:
- Create an issue in the GitHub repository
- Review the troubleshooting section below

## Troubleshooting

### Common Issues

**Database Connection Error**
```
Solution: Check DATABASE_URL environment variable and ensure PostgreSQL is running
```

**Session Secret Error**
```
Solution: Set SESSION_SECRET environment variable
```

**Port Already in Use**
```
Solution: Change port in main.py or kill process using port 5000
```

**CSS/JS Not Loading**
```
Solution: Check static file paths and ensure Flask static folder is configured
```

## Changelog

- **v1.0.0** - Initial release with patient registration and login
- See `replit.md` for detailed development history

---

**Note:** This application handles sensitive healthcare data. Always follow HIPAA compliance guidelines and your organization's security policies when deploying to production.