# MediCare+ Smart Medicine Reminder & Health Tracker

A healthcare management web application developed to help users manage medicines, receive timely medication reminders, monitor hydration levels, and maintain healthier daily routines through a simple and accessible digital platform.

MediCare+ focuses on improving medication adherence by providing reminder alerts before scheduled medicine timings. The application also includes features such as water intake tracking, BMI calculation, medicine stock monitoring, and activity history management.

---

# Project Overview

Managing medicines regularly can become difficult for elderly individuals, patients with chronic illnesses, and users with busy daily schedules. Missing medications or maintaining inconsistent health routines may lead to serious health complications.

MediCare+ was developed to simplify healthcare management through a lightweight and user-friendly solution that combines medicine reminders, health tracking, and personalized monitoring into a single platform.

The system is designed with a clean interface and responsive layout to ensure accessibility across different devices and user groups.

---

# Features

## Authentication Module

- User Registration
- User Login
- Secure Session Management
- Authentication Validation

## Dashboard Module

- Dynamic Greeting System
- Real-Time Digital Clock
- Daily Health Tips
- Medicine Statistics Overview
- Water Intake Tracker

## Medicine Management

- Add Medicine Details
- Edit Medicine Information
- Delete Medicines
- Track Medicine Stock Quantity

## Smart Reminder System

- Reminder Popup Notifications
- Audio Alarm Alerts
- JavaScript Timer-Based Scheduling
- Reminder Trigger Before Medicine Time
- Stop Alarm Functionality

## Health Monitoring

- BMI Calculation
- User Health Analysis
- Water Intake Monitoring

## History Management

- Medicine Activity Tracking
- Add/Edit/Delete Activity Records

---

# Technologies Used

## Frontend

- HTML5
- CSS3
- JavaScript
- Jinja Templates

## Backend

- Python
- Flask Framework

## Database

- SQLite

## Design & Documentation Tools

- Figma
- Canva

---

# Project Structure

```bash
MEDICINE_REMAINDER_SYSTEM/

├── backups/
├── controllers/
├── database/
├── docs/
├── models/
├── presentation/
├── routes/
├── static/
├── templates/
├── tests/
├── utils/
├── app.py
├── database.db
├── README.md
└── requirements.txt
```

---

# Installation & Setup

## Clone the Repository

```bash
git clone <repository-link>
```

---

## Navigate to Project Directory

```bash
cd MEDICINE_REMAINDER_SYSTEM
```

---

## Create Virtual Environment

```bash
python -m venv venv
```

---

## Activate Virtual Environment

### Windows

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
source venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Run the Application

```bash
python app.py
```

---

## Open in Browser

```bash
http://127.0.0.1:5000
```

---

# System Workflow

1. User logs into the system
2. Dashboard loads personalized health information
3. Medicines are added with schedule timings
4. Reminder timers monitor medicine schedules
5. Popup alerts and alarm notifications are triggered before medicine time
6. Water intake and BMI information are tracked dynamically
7. Medicine activity history is maintained automatically

---

# Reminder System

The reminder module uses JavaScript timers and audio alerts to notify users before scheduled medicine timings. Popup notifications are displayed along with alarm sounds to improve medication adherence and reduce missed medicines.

---

# Security Features

- Password Protection
- Session Authentication
- Input Validation
- Secure User Management

---

# Main Highlights

- Simple and responsive user interface
- Elderly-friendly healthcare design
- Lightweight SQLite database system
- Smart reminder notifications
- Water intake tracking
- BMI analysis
- Medicine stock monitoring
- Modular Flask architecture

---

# Future Enhancements

- Voice Assistant Integration
- Multi-language Support
- Mobile Application
- AI-Based Health Recommendations
- Cloud Data Backup
- Online Doctor Consultation
- Prescription Upload Feature
- Family Health Profiles

---

# Team Details

## Team Name

Code Crushers

## Team Members

- K V SAI RAHUL – Full Stack Developer
- SHAGUN MANGAL – UI/UX Designer & CSS Developer
- U SAI DINESH – Documentation Specialist

---

# Hackathon

Developed for the SkillGlider Hackathon.

---

# Screenshots

Project screenshots are added inside the `docs/screenshots/` directory.

screenshots:

- Login Page
- Dashboard
- Add Medicine Page
- Reminder Notifications
- Water Tracker
- BMI Analysis
- Notifications Page

---

# Conclusion

MediCare+ is a practical healthcare management solution developed to help users maintain medicine schedules and healthier daily routines through a simple and accessible platform.

The project combines medication reminders, health monitoring, and personalized healthcare tracking into a lightweight web application designed for real-world usability.

---
