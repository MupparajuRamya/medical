from datetime import datetime, date
from flask import render_template, request, redirect, url_for, flash, session, jsonify
from app import app, db
from models import Patient
from forms import RegistrationForm, LoginForm
import logging

# Configure session timeout
@app.before_request
def make_session_permanent():
    """Make session permanent and handle timeout."""
    session.permanent = True

@app.before_request
def check_session_timeout():
    """Check if session has timed out."""
    if 'patient_id' in session:
        if 'last_activity' in session:
            time_since_activity = datetime.utcnow() - datetime.fromisoformat(session['last_activity'])
            if time_since_activity.total_seconds() > 1800:  # 30 minutes
                session.clear()
                flash('Your session has expired. Please log in again.', 'warning')
                return redirect(url_for('login'))
        
        session['last_activity'] = datetime.utcnow().isoformat()

def login_required(f):
    """Decorator to require login for protected routes."""
    from functools import wraps
    
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'patient_id' not in session:
            flash('Please log in to access this page.', 'warning')
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

@app.route('/')
def index():
    """Home page - redirect to dashboard if logged in, otherwise show landing page."""
    if 'patient_id' in session:
        return redirect(url_for('dashboard'))
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    """Patient registration page."""
    if 'patient_id' in session:
        return redirect(url_for('dashboard'))
    
    if request.method == 'POST':
        form = RegistrationForm(request.form)
        
        if form.validate():
            # Check if email already exists
            existing_patient = Patient.query.filter_by(email=request.form['email']).first()
            if existing_patient:
                flash('An account with this email already exists. Please use a different email or log in.', 'danger')
                return render_template('register.html')
            
            try:
                # Create new patient
                patient = Patient(
                    first_name=request.form['first_name'].strip(),
                    last_name=request.form['last_name'].strip(),
                    email=request.form['email'].strip().lower(),
                    phone=request.form['phone'].strip(),
                    date_of_birth=datetime.strptime(request.form['date_of_birth'], '%Y-%m-%d').date(),
                    gender=request.form['gender'],
                    address=request.form['address'].strip(),
                    emergency_contact_name=request.form['emergency_contact_name'].strip(),
                    emergency_contact_phone=request.form['emergency_contact_phone'].strip()
                )
                
                patient.set_password(request.form['password'])
                
                db.session.add(patient)
                db.session.commit()
                
                logging.info(f"New patient registered: {patient.email}")
                flash('Registration successful! Please log in with your credentials.', 'success')
                return redirect(url_for('login'))
                
            except Exception as e:
                db.session.rollback()
                logging.error(f"Registration error: {str(e)}")
                flash('An error occurred during registration. Please try again.', 'danger')
        else:
            for error in form.get_errors():
                flash(error, 'danger')
    
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    """Patient login page."""
    if 'patient_id' in session:
        return redirect(url_for('dashboard'))
    
    if request.method == 'POST':
        form = LoginForm(request.form)
        
        if form.validate():
            email = request.form['email'].strip().lower()
            password = request.form['password']
            
            patient = Patient.query.filter_by(email=email).first()
            
            if patient and patient.check_password(password):
                if patient.is_active:
                    session['patient_id'] = patient.id
                    session['patient_name'] = patient.full_name
                    session['last_activity'] = datetime.utcnow().isoformat()
                    
                    # Update last login time
                    patient.last_login = datetime.utcnow()
                    db.session.commit()
                    
                    logging.info(f"Patient logged in: {patient.email}")
                    flash(f'Welcome back, {patient.first_name}!', 'success')
                    return redirect(url_for('dashboard'))
                else:
                    flash('Your account has been deactivated. Please contact support.', 'danger')
            else:
                flash('Invalid email or password. Please try again.', 'danger')
        else:
            for error in form.get_errors():
                flash(error, 'danger')
    
    return render_template('login.html')

@app.route('/logout')
def logout():
    """Log out the current patient."""
    if 'patient_id' in session:
        logging.info(f"Patient logged out: {session.get('patient_name', 'Unknown')}")
    
    session.clear()
    flash('You have been logged out successfully.', 'info')
    return redirect(url_for('index'))

@app.route('/dashboard')
@login_required
def dashboard():
    """Patient dashboard - main page after login."""
    patient = Patient.query.get(session['patient_id'])
    
    if not patient:
        session.clear()
        flash('Account not found. Please log in again.', 'danger')
        return redirect(url_for('login'))
    
    return render_template('dashboard.html', patient=patient)

@app.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():
    """Patient profile management."""
    patient = Patient.query.get(session['patient_id'])
    
    if not patient:
        session.clear()
        flash('Account not found. Please log in again.', 'danger')
        return redirect(url_for('login'))
    
    if request.method == 'POST':
        try:
            # Update patient information (excluding email and password)
            patient.first_name = request.form['first_name'].strip()
            patient.last_name = request.form['last_name'].strip()
            patient.phone = request.form['phone'].strip()
            patient.address = request.form['address'].strip()
            patient.emergency_contact_name = request.form['emergency_contact_name'].strip()
            patient.emergency_contact_phone = request.form['emergency_contact_phone'].strip()
            patient.updated_at = datetime.utcnow()
            
            db.session.commit()
            
            # Update session name if changed
            session['patient_name'] = patient.full_name
            
            flash('Profile updated successfully!', 'success')
            logging.info(f"Profile updated for patient: {patient.email}")
            
        except Exception as e:
            db.session.rollback()
            logging.error(f"Profile update error: {str(e)}")
            flash('An error occurred while updating your profile. Please try again.', 'danger')
    
    return render_template('profile.html', patient=patient)

@app.route('/change-password', methods=['POST'])
@login_required
def change_password():
    """Change patient password."""
    patient = Patient.query.get(session['patient_id'])
    
    if not patient:
        session.clear()
        flash('Account not found. Please log in again.', 'danger')
        return redirect(url_for('login'))
    
    current_password = request.form.get('current_password')
    new_password = request.form.get('new_password')
    confirm_password = request.form.get('confirm_password')
    
    # Validation
    if not current_password or not new_password or not confirm_password:
        flash('All password fields are required.', 'danger')
        return redirect(url_for('profile'))
    
    if not patient.check_password(current_password):
        flash('Current password is incorrect.', 'danger')
        return redirect(url_for('profile'))
    
    if new_password != confirm_password:
        flash('New passwords do not match.', 'danger')
        return redirect(url_for('profile'))
    
    # Validate new password strength
    is_valid, message = Patient.validate_password(new_password)
    if not is_valid:
        flash(message, 'danger')
        return redirect(url_for('profile'))
    
    try:
        patient.set_password(new_password)
        patient.updated_at = datetime.utcnow()
        db.session.commit()
        
        flash('Password changed successfully!', 'success')
        logging.info(f"Password changed for patient: {patient.email}")
        
    except Exception as e:
        db.session.rollback()
        logging.error(f"Password change error: {str(e)}")
        flash('An error occurred while changing your password. Please try again.', 'danger')
    
    return redirect(url_for('profile'))

@app.errorhandler(404)
def not_found_error(error):
    """Handle 404 errors."""
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(error):
    """Handle 500 errors."""
    db.session.rollback()
    return render_template('500.html'), 500

# Health check endpoint
@app.route('/health')
def health_check():
    """Simple health check endpoint."""
    return jsonify({'status': 'healthy', 'timestamp': datetime.utcnow().isoformat()})
