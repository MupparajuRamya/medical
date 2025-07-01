from datetime import datetime, date
import re

class FormValidator:
    """Utility class for form validation."""
    
    @staticmethod
    def validate_required_fields(data, required_fields):
        """Validate that all required fields are present and not empty."""
        errors = []
        for field in required_fields:
            if field not in data or not data[field] or str(data[field]).strip() == '':
                field_name = field.replace('_', ' ').title()
                errors.append(f"{field_name} is required")
        return errors
    
    @staticmethod
    def validate_email(email):
        """Validate email format."""
        if not email:
            return "Email is required"
        
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if not re.match(pattern, email):
            return "Please enter a valid email address"
        
        return None
    
    @staticmethod
    def validate_phone(phone):
        """Validate phone number."""
        if not phone:
            return "Phone number is required"
        
        # Remove any formatting characters
        digits_only = re.sub(r'\D', '', phone)
        
        if len(digits_only) < 10:
            return "Phone number must be at least 10 digits"
        
        if len(digits_only) > 15:
            return "Phone number is too long"
        
        return None
    
    @staticmethod
    def validate_password(password):
        """Validate password strength."""
        if not password:
            return "Password is required"
        
        if len(password) < 8:
            return "Password must be at least 8 characters long"
        
        if not re.search(r"[A-Z]", password):
            return "Password must contain at least one uppercase letter"
        
        if not re.search(r"[a-z]", password):
            return "Password must contain at least one lowercase letter"
        
        if not re.search(r"\d", password):
            return "Password must contain at least one number"
        
        if not re.search(r"[!@#$%^&*()_+\-=\[\]{};':\"\\|,.<>\/?]", password):
            return "Password must contain at least one special character (!@#$%^&*)"
        
        return None
    
    @staticmethod
    def validate_date_of_birth(dob_str):
        """Validate date of birth."""
        if not dob_str:
            return "Date of birth is required"
        
        try:
            dob = datetime.strptime(dob_str, '%Y-%m-%d').date()
            
            # Check if date is not in the future
            if dob > date.today():
                return "Date of birth cannot be in the future"
            
            # Check minimum age (13 years for privacy compliance)
            today = date.today()
            age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
            
            if age < 13:
                return "Patient must be at least 13 years old"
            
            if age > 120:
                return "Please enter a valid date of birth"
            
            return None
            
        except ValueError:
            return "Please enter a valid date in YYYY-MM-DD format"
    
    @staticmethod
    def validate_name(name, field_name):
        """Validate name fields."""
        if not name:
            return f"{field_name} is required"
        
        if len(name.strip()) < 2:
            return f"{field_name} must be at least 2 characters long"
        
        if len(name.strip()) > 50:
            return f"{field_name} must be less than 50 characters"
        
        # Only allow letters, spaces, hyphens, and apostrophes
        if not re.match(r"^[a-zA-Z\s\-']+$", name):
            return f"{field_name} can only contain letters, spaces, hyphens, and apostrophes"
        
        return None
    
    @staticmethod
    def validate_gender(gender):
        """Validate gender selection."""
        valid_genders = ['male', 'female', 'other', 'prefer_not_to_say']
        
        if not gender:
            return "Gender is required"
        
        if gender.lower() not in valid_genders:
            return "Please select a valid gender option"
        
        return None
    
    @staticmethod
    def validate_address(address):
        """Validate address."""
        if not address:
            return "Address is required"
        
        if len(address.strip()) < 10:
            return "Please enter a complete address"
        
        if len(address.strip()) > 200:
            return "Address is too long"
        
        return None

class RegistrationForm:
    """Handle patient registration form validation."""
    
    def __init__(self, form_data):
        self.data = form_data
        self.errors = []
    
    def validate(self):
        """Validate all registration form fields."""
        self.errors = []
        
        # Required fields validation
        required_fields = [
            'first_name', 'last_name', 'email', 'phone', 'date_of_birth',
            'gender', 'address', 'emergency_contact_name', 'emergency_contact_phone',
            'password', 'confirm_password'
        ]
        
        self.errors.extend(FormValidator.validate_required_fields(self.data, required_fields))
        
        # Individual field validations
        if 'first_name' in self.data:
            error = FormValidator.validate_name(self.data['first_name'], 'First name')
            if error:
                self.errors.append(error)
        
        if 'last_name' in self.data:
            error = FormValidator.validate_name(self.data['last_name'], 'Last name')
            if error:
                self.errors.append(error)
        
        if 'email' in self.data:
            error = FormValidator.validate_email(self.data['email'])
            if error:
                self.errors.append(error)
        
        if 'phone' in self.data:
            error = FormValidator.validate_phone(self.data['phone'])
            if error:
                self.errors.append(error)
        
        if 'date_of_birth' in self.data:
            error = FormValidator.validate_date_of_birth(self.data['date_of_birth'])
            if error:
                self.errors.append(error)
        
        if 'gender' in self.data:
            error = FormValidator.validate_gender(self.data['gender'])
            if error:
                self.errors.append(error)
        
        if 'address' in self.data:
            error = FormValidator.validate_address(self.data['address'])
            if error:
                self.errors.append(error)
        
        if 'emergency_contact_name' in self.data:
            error = FormValidator.validate_name(self.data['emergency_contact_name'], 'Emergency contact name')
            if error:
                self.errors.append(error)
        
        if 'emergency_contact_phone' in self.data:
            error = FormValidator.validate_phone(self.data['emergency_contact_phone'])
            if error:
                self.errors.append('Emergency contact ' + error.lower())
        
        if 'password' in self.data:
            error = FormValidator.validate_password(self.data['password'])
            if error:
                self.errors.append(error)
        
        # Password confirmation validation
        if 'password' in self.data and 'confirm_password' in self.data:
            if self.data['password'] != self.data['confirm_password']:
                self.errors.append("Passwords do not match")
        
        return len(self.errors) == 0
    
    def get_errors(self):
        """Get validation errors."""
        return self.errors

class LoginForm:
    """Handle login form validation."""
    
    def __init__(self, form_data):
        self.data = form_data
        self.errors = []
    
    def validate(self):
        """Validate login form fields."""
        self.errors = []
        
        if not self.data.get('email'):
            self.errors.append("Email is required")
        else:
            error = FormValidator.validate_email(self.data['email'])
            if error:
                self.errors.append(error)
        
        if not self.data.get('password'):
            self.errors.append("Password is required")
        
        return len(self.errors) == 0
    
    def get_errors(self):
        """Get validation errors."""
        return self.errors
