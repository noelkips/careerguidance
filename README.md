# 🎓 Career Guidance System

The **Career Guidance System** is a web-based application built using Django and Python to help students make informed decisions about their academic and career paths. It leverages a rule-based knowledge engine, user data, and intelligent recommendations to match students with courses that suit their interests, academic performance, and preferred subjects.

## 🚀 Features

- 🔍 **Course Recommendation Engine**  
  A rule-based AI system developed in Python that suggests the best career or course paths for students based on:
  - Academic performance  
  - Subject preferences  
  - Personal interests  

- 🔐 **Multi-User Authentication System**  
  Secure registration and login system allowing students, counselors, and admins to access personalized dashboards.

- 💳 **API Integration for Payments**  
  Seamless integration with payment gateways to facilitate premium features or consultation bookings.

- 📊 **Personalized Dashboards**  
  Each user gets a dashboard tailored to their role and activity history.

- 🌐 **Clean and Responsive UI**  
  Intuitive and responsive interface designed for ease of use across devices.

## 🛠️ Tech Stack

- **Backend:** Django, Python  
- **Frontend:** HTML, CSS, JavaScript (Django Templates)  
- **Database:** SQLite / PostgreSQL  
- **Authentication:** Django Allauth / Custom multi-auth  
- **Payments API:** Django Daraja for Mpesa Payments

## 📦 Installation & Setup

1. Clone the repository:  
   ```
   
   git clone  https://github.com/noelkips/careerguidance.git 
   cd careerguidance
   ```

2. Create and activate a virtual environment:  
   ```
   python -m venv venv  
   source venv/bin/activate   # For Linux/macOS  
   venv\Scripts\activate      # For Windows
   ```

3. Install dependencies:  
   ```
   pip install -r requirements.txt
   ```

4. Apply migrations:  
   ```
   python manage.py migrate
   ```

5. Run the development server:  
   ```
   python manage.py runserver
   ```


## 🙌 Contributions

Contributions are welcome! If you’d like to improve this project, feel free to fork the repo and submit a pull request.

## 📬 Contact

For inquiries or support, reach out via:  
Email: noellangat28@gmail.com  

