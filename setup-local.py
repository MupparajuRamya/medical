#!/usr/bin/env python3
"""
Healthcare Portal - Local Development Setup Script

This script helps set up the healthcare portal for local development.
Run this after cloning the repository to your local machine.
"""

import os
import sys
import subprocess
import sqlite3
from pathlib import Path

def run_command(command, description):
    """Run a shell command and handle errors."""
    print(f"\n{description}...")
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        print(f"✓ {description} completed successfully")
        return True
    except subprocess.CalledProcessError as e:
        print(f"✗ Error during {description.lower()}: {e.stderr}")
        return False

def create_env_file():
    """Create .env file from template if it doesn't exist."""
    env_file = Path('.env')
    env_example = Path('.env.example')
    
    if not env_file.exists() and env_example.exists():
        print("\nCreating .env file from template...")
        with open(env_example, 'r') as source:
            content = source.read()
        
        # Update with local SQLite database for development
        content = content.replace(
            'DATABASE_URL=postgresql://username:password@localhost:5432/healthcare_portal',
            'DATABASE_URL=sqlite:///healthcare_portal.db'
        )
        
        with open(env_file, 'w') as dest:
            dest.write(content)
        
        print("✓ .env file created with SQLite database configuration")
        print("  Note: Edit .env to use PostgreSQL if preferred")
    else:
        print("✓ .env file already exists")

def setup_virtual_environment():
    """Set up Python virtual environment."""
    venv_path = Path('venv')
    
    if not venv_path.exists():
        print("\nCreating virtual environment...")
        if run_command(f"{sys.executable} -m venv venv", "Virtual environment creation"):
            print("✓ Virtual environment created")
        else:
            return False
    else:
        print("✓ Virtual environment already exists")
    
    return True

def install_dependencies():
    """Install Python dependencies."""
    # Determine the correct pip path
    if os.name == 'nt':  # Windows
        pip_path = 'venv\\Scripts\\pip'
        python_path = 'venv\\Scripts\\python'
    else:  # Unix/Linux/macOS
        pip_path = 'venv/bin/pip'
        python_path = 'venv/bin/python'
    
    print(f"\nInstalling dependencies using {pip_path}...")
    
    # Install from requirements-local.txt
    if Path('requirements-local.txt').exists():
        return run_command(f"{pip_path} install -r requirements-local.txt", "Dependency installation")
    else:
        print("✗ requirements-local.txt not found")
        return False

def setup_database():
    """Initialize the database."""
    print("\nSetting up database...")
    
    # Create a simple database setup script
    db_setup_script = '''
import os
import sys
sys.path.append('.')

from app import app, db

with app.app_context():
    try:
        db.create_all()
        print("✓ Database tables created successfully")
    except Exception as e:
        print(f"✗ Database setup failed: {e}")
        sys.exit(1)
'''
    
    # Write temporary setup script
    with open('temp_db_setup.py', 'w') as f:
        f.write(db_setup_script)
    
    # Run database setup
    if os.name == 'nt':  # Windows
        python_path = 'venv\\Scripts\\python'
    else:  # Unix/Linux/macOS
        python_path = 'venv/bin/python'
    
    success = run_command(f"{python_path} temp_db_setup.py", "Database initialization")
    
    # Clean up temporary file
    try:
        os.remove('temp_db_setup.py')
    except:
        pass
    
    return success

def print_next_steps():
    """Print instructions for next steps."""
    print("\n" + "="*60)
    print("🎉 Healthcare Portal setup complete!")
    print("="*60)
    
    print("\nNext steps:")
    print("1. Activate the virtual environment:")
    if os.name == 'nt':  # Windows
        print("   venv\\Scripts\\activate")
    else:  # Unix/Linux/macOS
        print("   source venv/bin/activate")
    
    print("\n2. Start the development server:")
    print("   python main.py")
    
    print("\n3. Open your browser and go to:")
    print("   http://localhost:5000")
    
    print("\n4. For VS Code development:")
    print("   - Open this folder in VS Code")
    print("   - Install recommended extensions")
    print("   - Use F5 to start debugging")
    
    print("\nEnvironment files:")
    print("- .env: Environment variables (edit as needed)")
    print("- requirements-local.txt: Python dependencies")
    print("- .vscode/: VS Code configuration")
    
    print("\nFor more information, see README.md")

def main():
    """Main setup function."""
    print("Healthcare Portal - Local Development Setup")
    print("="*50)
    
    # Check Python version
    if sys.version_info < (3, 11):
        print("✗ Python 3.11 or higher is required")
        print(f"  Current version: {sys.version}")
        sys.exit(1)
    
    print(f"✓ Python {sys.version.split()[0]} detected")
    
    # Setup steps
    steps = [
        ("Environment file setup", create_env_file),
        ("Virtual environment setup", setup_virtual_environment),
        ("Dependency installation", install_dependencies),
        ("Database initialization", setup_database),
    ]
    
    for step_name, step_function in steps:
        try:
            if not step_function():
                print(f"\n✗ Setup failed at: {step_name}")
                print("Please check the error messages above and try again.")
                sys.exit(1)
        except KeyboardInterrupt:
            print("\n\nSetup interrupted by user.")
            sys.exit(1)
        except Exception as e:
            print(f"\n✗ Unexpected error during {step_name}: {e}")
            sys.exit(1)
    
    print_next_steps()

if __name__ == "__main__":
    main()