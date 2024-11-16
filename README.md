# Forum Application
A simple Forum Application built using Flask, featuring user login functionality, account management, and a user dashboard. The application uses MongoDB for database management and provides a clean, responsive user interface.

## Features
 - User registration and login
 - Secure password handling using Passlib
 - Account management with real-time data interactions
 - User dashboard displaying user-specific data
 - Error handling with user-friendly feedback

## Technologies Used
 - **Flask**: Backend framework
 - **MongoDB**: NoSQL database
 - **Passlib**: Password hashing library
 - **PyMongo**: MongoDB driver for Python
 - **jQuery**: Frontend interaction and AJAX requests
 - **HTML/CSS/JS**: Templates and static assets

## Installation Guide
Follow these steps to set up and run the application:

### 1. Create a New Virtual Environment
Create and activate a virtual environment to manage dependencies:
```bash
# Create a virtual environment named 'forumapp'
python -m venv forumapp

# Activate the virtual environment
# Windows
.\forumapp\Scripts\activate

# macOS/Linux
source forumapp/bin/activate
```

### 2. Install Required Libraries
Install necessary packages using pip:
```bash
pip install flask pymongo passlib
```

### 3. Set Up app.py
Ensure app.py includes your unique security key:
```bash
app.secret_key = 'add_your_unique_key_here'  # Replace with your unique key
```

### 4. Run the Application
Use the following command in the terminal to start the Flask server:
```bash
flask run
```
The application will be accessible at http://127.0.0.1:5000/.

## File Structure
### Main Code File
 - app.py: Contains the main application logic and route setup.

### Template Files
 - **base.htm**l: Base template with reusable HTML structure.
 - **home.html**: Homepage template with login and signup forms.
 - **dashboard.html**: Dashboard template showing user data.

### Static Assets
 - **static/css/styles.css**: Styling for the application.
 - **static/js/jquery.js**: jQuery library for form handling.

## Screenshot of Web APP
![image](https://github.com/user-attachments/assets/02ee7f22-edfe-4535-9e45-78c7bba58c93)
![image](https://github.com/user-attachments/assets/4d064e18-70c0-4dc1-b9cc-f9ffd35b281f)
