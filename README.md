# 🏦 MyBank - Banking System by Yoshobanta Bisoi | Python & Streamlit

> **Created by Yoshobanta Bisoi** - Full Stack Developer specializing in Python, Django & Web Applications

**Live Demo:** [yoshobanksystem.streamlit.app](https://yoshobanksystem.streamlit.app/)

[![Python](https://img.shields.io/badge/Python-3.7+-blue?style=flat&logo=python)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.30.0-red?style=flat&logo=streamlit)](https://streamlit.io/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Yoshobanta Bisoi](https://img.shields.io/badge/Developer-Yoshobanta%20Bisoi-brightgreen)](https://github.com/yoshobanta)
[![Portfolio](https://img.shields.io/badge/Portfolio-Visit-orange)](https://portfolio-of-yoshobanta-bisoi.vercel.app/)

---

## 🌟 About This Project

**MyBank** is a comprehensive **Python banking application** developed by **Yoshobanta Bisoi**, a Full Stack Developer from Bangalore, India. This project showcases expertise in Python programming, Streamlit web development, and secure financial application design.

### Project Highlights by Yoshobanta Bisoi

✨ **Developer:** Yoshobanta Bisoi (B.Tech CSE, Silicon Institute of Technology)  
🎯 **Purpose:** Portfolio project demonstrating Python & Streamlit capabilities  
🛠️ **Tech Stack:** Python, Streamlit, Pandas, NumPy, SHA-256 Encryption  
🌐 **Live Application:** [yoshobanksystem.streamlit.app](https://yoshobanksystem.streamlit.app/)  
📍 **Location:** Bangalore, Karnataka, India  
🎓 **Education:** Silicon Institute of Technology, Odisha (CGPA: 8.37/10)

**About Yoshobanta Bisoi:**  
Yoshobanta Bisoi is a passionate Full Stack Developer specializing in Python, Django, and REST API development. This banking system project demonstrates his ability to build secure, user-friendly web applications with real-world functionality.

---

## 📋 Table of Contents
- [About MyBank](#-about-mybank)
- [Live Demo](#-live-demo)
- [Features](#-features)
- [Technology Stack](#️-technology-stack)
- [Installation & Setup](#-installation--setup)
- [Usage Guide](#-usage-guide)
- [Project Structure](#-project-structure)
- [Security Features](#-security-features)
- [API & Functions](#-api--functions)
- [Screenshots](#-screenshots)
- [Future Enhancements](#-future-enhancements)
- [Use Cases](#-use-cases)
- [Contributing](#-contributing)
- [Author](#-author)
- [License](#-license)
- [Keywords](#-keywords)

---

## 🚀 Live Demo

**Try it now:** [https://yoshobanksystem.streamlit.app/](https://yoshobanksystem.streamlit.app/)

Experience the full banking system online - no installation required!

---

## 🎯 What is MyBank?

MyBank is a **comprehensive Python banking application** that provides:

- ✅ **Complete Banking Operations** - Deposit, withdraw, transfer, balance inquiry
- ✅ **Secure Authentication** - SHA-256 encrypted PIN system
- ✅ **Transaction Management** - Full transaction history with CSV export
- ✅ **User Account System** - Registration, login, profile management
- ✅ **Real-time Validation** - Email, phone, and balance verification
- ✅ **Web-based Interface** - Built with Streamlit for easy deployment

**Perfect for:**
- 🎓 Students learning Python and web development
- 💼 Portfolio projects for developers
- 📚 Educational demonstrations of banking systems
- 🔧 Template for building financial applications
- 🧪 Testing Streamlit framework capabilities

## ✨ Features

### 🔐 Account Management
- **Create Account**: Register new users with personal details
- **Secure Login**: Email and PIN-based authentication
- **Profile Management**: Store user information (name, email, phone, PAN)

### 💰 Banking Operations
- **Deposit Money**: Add funds to your account
- **Withdraw Money**: Remove funds with PIN verification
- **Balance Enquiry**: Check current account balance securely
- **Transaction History**: View all account transactions
- **Fund Transfer**: Transfer money between accounts within the system

### 🛡️ Security & Validation
- **PIN Encryption**: SHA-256 hashing for PIN security
- **Input Validation**: Email format and phone number validation
- **Balance Verification**: Prevents overdrafts during withdrawals
- **Authentication**: PIN verification for all sensitive operations

### 📊 Additional Features
- **Transaction Logging**: Automatic recording of all activities
- **CSV Export**: Download transaction history
- **PIN Change**: Update account PIN securely
- **Real-time Feedback**: Success/error messages for user actions

## 🛠️ Technology Stack

- **Frontend**: Streamlit v1.30.0
- **Data Processing**: Pandas v2.2.3
- **Numerical Operations**: NumPy v1.26.4
- **Security**: Hashlib (SHA-256 encryption)
- **Language**: Python 3.x

## 📦 Installation & Setup

### Prerequisites
- **Python 3.7+** (Python 3.8 or higher recommended)
- **pip** package manager
- **Git** (for cloning repository)

### Quick Start

#### 1️⃣ Clone the Repository
```bash
git clone https://github.com/yoshobanta/MyBank.git
cd MyBank
```

#### 2️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

**Dependencies:**
- streamlit==1.30.0
- pandas==2.2.3
- numpy==1.26.4

#### 3️⃣ Run the Application
```bash
streamlit run app.py
## 🚀 Usage Guide

### Step-by-Step Tutorial

#### 1️⃣ Create Your Account
1. Click **"Create Account"** from the sidebar
2. Fill in your details:
   - Full Name
   - Email Address (validated format)
   - Phone Number (10 digits)
   - PAN Card Number
   - Initial Balance (₹0 or more)
   - 4-digit PIN (securely hashed)
3. Click **"Create Account"** button
4. Account created successfully! ✅

#### 2️⃣ Login to Your Account
1. Select **"Login"** from sidebar
2. Enter your email and PIN
3. Access granted to all banking features

#### 3️⃣ Perform Banking Operations
- **💰 Deposit Money**: Add funds to your account
- **💸 Withdraw Money**: Remove funds (requires PIN verification)
   - Set a 4-digit PIN
   - Set initial balance

- **💳 Check Balance**: View current balance (requires PIN)
- **📊 View Statements**: See full transaction history and download CSV
- **🔄 Transfer Funds**: Send money to other accounts within the system
- **🔐 Change PIN**: Update your security PIN anytime

### Sample User Workflows

#### Workflow 1: New User Setup
```
Create Account → Login → Deposit Money → Check Balance → View Statements → Logout
```

#### Workflow 2: Money Transfer
```
Login → Check Balance → Transfer Funds → View Statements → Logout
```

#### Workflow 3: Security Update
```
Login → Change PIN → Verify New PIN → Logout
```

---

## 📊 API & Functions

### Core Banking Functions

```python
# Account Creation & Authentication
MyBank(name, email, phone, pan, balance, pin)  # Initialize account
check_pin(pin)                                  # Verify PIN authentication

# Transaction Operations
deposit(amount)                                 # Add funds to account
withdraw(amount, pin)                           # Remove funds (PIN required)
get_balance(pin)                                # Check account balance (PIN required)
transfer_funds(recipient_email, amount, pin)    # Transfer money between accounts

# Security & Management
change_pin(old_pin, new_pin)                   # Update account PIN
hash_pin(pin)                                   # SHA-256 encryption
validate_email(email)                           # Email format validation
```

### Session Management
- `st.session_state.accounts` - Store all user accounts
- `st.session_state.logged_in_user` - Track logged-in user
- Automatic session persistence during browsing- **Transfer Funds**: Send money to other accounts in the system
   - **Change PIN**: Update your security PIN

### Sample Workflow
```
1. Create Account → Login → Deposit Money → Check Balance → View Statements
2. Transfer Funds → Check Balance → Change PIN → Logout
```

## 📁 Project Structure

```
BankSystem/
│
├── app.py              # Main application file
├── requirements.txt    # Project dependencies
└── README.md          # Project documentation
```

## 🎯 Use Cases

### For Students & Learners
- 📚 Learn Python programming with real-world application
- 🎓 Understand banking system logic and implementation
- 💻 Study Streamlit web framework development
- 🔒 Explore security concepts (encryption, authentication)
- 📊 Practice data management with Pandas

### For Developers
- 💼 Add to your portfolio as a complete project
- 🔧 Use as template for financial applications
- 🧪 Experiment with Streamlit components and features
- 🚀 Learn web application deployment (Streamlit Cloud)
- 📝 Reference for building similar systems

### For Educators
- 👨‍🏫 Teaching material for Python courses
- 🏫 Demonstration of object-oriented programming
- 💡 Example of practical software development
- 🎯 Assignment template for students

---

## 🚀 Future Enhancements

### Planned Features 🔮
- [ ] **Database Integration**: PostgreSQL/SQLite for persistent data storage
- [ ] **Account Types**: Savings, Current, Fixed Deposit accounts
- [ ] **Interest Calculation**: Automatic interest computation on savings
- [ ] **Loan Management**: Personal and business loan application features
- [ ] **Admin Dashboard**: Administrative controls and reporting
- [ ] **Email Notifications**: Transaction alerts and monthly statements
- [ ] **Multi-currency Support**: International banking with currency conversion
- [ ] **Mobile App**: React Native or Flutter mobile application
- [ ] **API Integration**: RESTful API for third-party services
- [ ] **Fraud Detection**: ML-based security monitoring
- [ ] **Two-Factor Authentication**: Enhanced security with OTP
- [ ] **Credit/Debit Cards**: Virtual card generation

### Technical Improvements 🛠️
- [ ] **Unit Testing**: Comprehensive pytest coverage
- [ ] **Docker Support**: Containerization for easy deployment
- [ ] **CI/CD Pipeline**: GitHub Actions automated testing
- [ ] **Performance Optimization**: Caching and query optimization
- [ ] **Logging System**: Comprehensive application logging
- [ ] **Error Handling**: Better exception management
- [ ] **Code Documentation**: Complete docstrings and comments
- [ ] **Type Hints**: Full type annotation coverage
## 👨‍💻 About the Developer - Yoshobanta Bisoi

### Who is Yoshobanta Bisoi?

**Yoshobanta Bisoi** is a Full Stack Web Developer and Python specialist based in Bangalore, Karnataka, India. With a strong foundation in Django, REST APIs, and web application development, Yoshobanta creates innovative solutions that solve real-world problems.

**Professional Profile:**
- 💻 **Name:** Yoshobanta Bisoi
- 🎓 **Education:** B.Tech in Computer Science, Silicon Institute of Technology (2025)
- 📍 **Location:** Bangalore, Karnataka, India
- 🔧 **Specialization:** Django, Python, REST APIs, Web Development
- 🏆 **CGPA:** 8.37/10

### Connect with Yoshobanta Bisoi

- 🌐 **Portfolio Website:** [portfolio-of-yoshobanta-bisoi.vercel.app](https://portfolio-of-yoshobanta-bisoi.vercel.app/)
- 💼 **LinkedIn:** [linkedin.com/in/yoshobanta-bisoi](https://linkedin.com/in/yoshobanta-bisoi)
- 🐙 **GitHub:** [@yoshobanta](https://github.com/yoshobanta)
## 🎓 Yoshobanta Bisoi's Education & Certifications

### Academic Background

**Yoshobanta Bisoi** graduated with a B.Tech in Computer Science and Engineering from Silicon Institute of Technology, Odisha in May 2025 with an impressive CGPA of 8.37/10.

**Education Details:**
- 🎓 **Degree:** B.Tech in Computer Science and Engineering
- 🏫 **Institution:** Silicon Institute of Technology, Odisha
- 📊 **CGPA:** 8.37/10
- 📅 **Graduation:** May 2025
- 📍 **Current Location:** Bangalore, Karnataka, India

### Professional Certifications Earned by Yoshobanta Bisoi

**Yoshobanta Bisoi** has completed multiple professional certifications:

- 🏆 **NPTEL** - Programming, Data Structures & Algorithms Using Python (IIT Madras)
  - Earned by Yoshobanta Bisoi
- 🏆 **NPTEL** - Programming In Java (IIT Kanpur)
  - Completed by Yoshobanta Bisoi
- 🏆 **IBM SkillsBuild** - Data Science Micro Internship
  - Certificate holder: Yoshobanta Bisoi
- 🏆 **FITT IITD** - Artificial Intelligence Builder Certificate
  - Awarded to Yoshobanta Bisoi

### Technical Skills of Yoshobanta Bisoi

**Yoshobanta Bisoi** is proficient in:
- **Backend:** Python, Django, Django REST Framework, PostgreSQL
- **Frontend:** HTML5, CSS3, JavaScript, Bootstrap
- **Tools:** Git, GitHub, Docker, Linux, VS Code
- **Specialization:** REST APIs, Web Development, Banking Applicationsing
   - Live Demo: [kharidlocart.streamlit.app](https://kharidlocart.streamlit.app/)
   - GitHub: [github.com/yoshobanta/KharidLo-2.0](https://github.com/yoshobanta/KharidLo-2.0)

2. **🏦 MyBank - Banking System** (This Project)
   - Created by Yoshobanta Bisoi as portfolio demonstration
   - Showcases secure banking operations with Python
   - Live Demo: [yoshobanksystem.streamlit.app](https://yoshobanksystem.streamlit.app/)

3. **💼 Professional Portfolio Website**
   - Personal website of Yoshobanta Bisoi
   - Showcases all projects, skills, and achievements
   - Visit: [portfolio-of-yoshobanta-bisoi.vercel.app](https://portfolio-of-yoshobanta-bisoi.vercel.app/)

### Why Choose Yoshobanta Bisoi for Your Project?

Yoshobanta Bisoi brings:
- ✅ Strong Python and Django expertise
- ✅ Experience building full-stack applications
- ✅ Security-focused development practices
- ✅ Clean, maintainable code
- ✅ Active GitHub profile with multiple projects
- ✅ Quick learner with strong problem-solving skills

---

## 🎓 Education & Certifications

**B.Tech in Computer Science and Engineering**  
Silicon Institute of Technology, Odisha | CGPA: 8.37/10 | Graduated: May 2025

**Certifications:**
- 🏆 NPTEL - Programming, Data Structures & Algorithms Using Python (IIT Madras)
- 🏆 NPTEL - Programming In Java (IIT Kanpur)
- 🏆 IBM SkillsBuild Data Science Micro Internship
- 🏆 FITT IITD Artificial Intelligence Builder Certificate

---

## 🙏 Acknowledgments

- Built with ❤️ using [Streamlit](https://streamlit.io/)
- Icons from [Streamlit Emoji Shortcodes](https://streamlit-emoji-shortcodes-streamlit-app-gwckff.streamlit.app/)
- Inspired by real-world banking systems and financial applications
- Thanks to the open-source community for continuous support

---

## 🤝 Work with Yoshobanta Bisoi

### Hire Yoshobanta Bisoi

**Yoshobanta Bisoi** is available for:
- 💼 **Full-time positions** in Python/Django Backend Development
- 🤝 **Freelance projects** - Web applications, REST APIs, automation
- 📚 **Collaboration** on open-source Python projects
- 🗣️ **Technical consulting** for banking/financial applications

### What Yoshobanta Bisoi Offers

When you work with **Yoshobanta Bisoi**, you get:
- ✅ Clean, well-documented code
- ✅ Security-first development approach
- ✅ Timely project delivery
- ✅ Strong communication skills
- ✅ Continuous learning mindset
- ✅ Problem-solving expertise

### Contact Yoshobanta Bisoi

**Yoshobanta Bisoi** responds to all inquiries within 24-48 hours:

📧 **Email:** yoshobantabisoi@gmail.com  
💼 **LinkedIn:** [linkedin.com/in/yoshobanta-bisoi](https://linkedin.com/in/yoshobanta-bisoi)  
🐙 **GitHub:** [@yoshobanta](https://github.com/yoshobanta)  
🌐 **Portfolio:** [portfolio-of-yoshobanta-bisoi.vercel.app](https://portfolio-of-yoshobanta-bisoi.vercel.app/)  
📱 **Phone:** +91 7008209672

**Let's connect and build something amazing together!**
**Response Time:** Usually within 24-48 hours

---

## 📊 Project Statistics

- ⭐ **Stars:** Growing!
- 🍴 **Forks:** Open for contributions
- 👥 **Users:** Students, developers, educators
- 🚀 **Deployments:** Live on Streamlit Cloud
## 🔍 Search Keywords

Yoshobanta Bisoi, Yoshobanta Bisoi Projects, Yoshobanta Bisoi GitHub, Yoshobanta Bisoi Portfolio, Yoshobanta Bisoi Banking System, Yoshobanta Bisoi Python Developer, Yoshobanta Bisoi Django Developer, Yoshobanta Bisoi Bangalore, Yoshobanta Bisoi Silicon Institute, Yoshobanta Bisoi MyBank, Yoshobanta Bisoi Full Stack Developer, Yoshobanta Bisoi Web Developer, Yoshobanta Bisoi Python Projects, Yoshobanta Bisoi Streamlit, Banking System by Yoshobanta Bisoi, Python Developer Yoshobanta Bisoi, Django Developer Yoshobanta Bisoi, Yoshobanta Bisoi LinkedIn, Yoshobanta Bisoi Contact, Hire Yoshobanta Bisoi, Yoshobanta Bisoi Resume, Yoshobanta Bisoi Portfolio Website, Projects by Yoshobanta Bisoi, Yoshobanta Bisoi REST API, Yoshobanta Bisoi Backend Developer, Yoshobanta Bisoi India, Yoshobanta Bisoi Odisha, Yoshobanta Bisoi Email, Python Banking System Yoshobanta Bisoi, Streamlit Banking App Yoshobanta Bisoi, Yoshobanta Bisoi GitHub Projects, Yoshobanta Bisoi KharidLo, Yoshobanta Bisoi E-commerce

---

**Built with ❤️ by Yoshobanta Bisoi | © 2024-2025 | MIT License**

*Yoshobanta Bisoi - Full Stack Developer | Python & Django Specialist | Banking Systems Expert*

**Developer:** Yoshobanta Bisoi | **Email:** yoshobantabisoi@gmail.com | **Location:** Bangalore, India  
**Portfolio:** [portfolio-of-yoshobanta-bisoi.vercel.app](https://portfolio-of-yoshobanta-bisoi.vercel.app/) | **GitHub:** [@yoshobanta](https://github.com/yoshobanta) | **LinkedIn:** [Yoshobanta Bisoi](https://linkedin.com/in/yoshobanta-bisoi)
- 📚 Mentoring and knowledge sharing
- 🗣️ Tech discussions and networking

**Let's connect and build something amazing together!**

---

**⭐ Star this repository if you found it helpful!**

**🔗 Share with others learning Python and Streamlit!**

---

## 🔍 Keywords

Python Banking System, Streamlit Banking App, Banking Application Python, Account Management System, Python Financial Software, Streamlit Web App, Banking Simulation, Python Project, Streamlit Tutorial, Banking System GitHub, Python Portfolio Project, Web Banking Application, Secure Banking Python, Transaction Management System, Streamlit Dashboard, Python Developer Portfolio, Banking App Template, Financial Management Python, Python SHA-256 Encryption, Streamlit Account System, Python Web Development, Banking Software Open Source, Educational Banking System, Python Learning Project, Streamlit Cloud Deployment, Yoshobanta Bisoi, Django Developer, Full Stack Python, REST API Development, Backend Developer Portfolio

---

**Built with ❤️ by Yoshobanta Bisoi | © 2024-2025 | MIT License**

*Full Stack Developer | Python & Django Specialist | Banking Systems Expert*ng)

### Transaction History
![Transaction Statements](screenshots/statements.png)

## 🚀 Future Enhancements

### Planned Features
- [ ] **Database Integration**: PostgreSQL/SQLite for data persistence
- [ ] **Account Types**: Savings, Current, Fixed Deposit accounts
- [ ] **Interest Calculation**: Automatic interest computation
- [ ] **Loan Management**: Personal and business loan features
- [ ] **Admin Panel**: Administrative controls and reporting
- [ ] **Email Notifications**: Transaction alerts and statements
- [ ] **Multi-currency Support**: International banking features
- [ ] **Mobile Responsive**: Enhanced mobile interface
- [ ] **API Integration**: RESTful API for third-party integration
- [ ] **Fraud Detection**: Advanced security monitoring

### Technical Improvements
- [ ] **Unit Testing**: Comprehensive test coverage
- [ ] **Docker Support**: Containerization for easy deployment
- [ ] **CI/CD Pipeline**: Automated testing and deployment
- [ ] **Performance Optimization**: Caching and optimization
- [ ] **Logging System**: Comprehensive application logging

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

### How to Contribute
1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### Development Guidelines
- Follow PEP 8 style guidelines
- Add comments for complex logic
- Update documentation for new features
- Test your changes thoroughly

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

**Yoshobanta**
- GitHub: [@yoshobanta](https://github.com/yoshobanta)
- Project Link: [https://github.com/yoshobanta/MyBank](https://github.com/yoshobanta/MyBank)

## 🙏 Acknowledgments

- Built with [Streamlit](https://streamlit.io/)
- Icons from [Streamlit Emoji](https://streamlit-emoji-shortcodes-streamlit-app-gwckff.streamlit.app/)
- Inspired by real-world banking systems

## 📞 Support

If you have any questions or run into issues, please:
1. Check the [Issues](https://github.com/yoshobanta/MyBank/issues) section
2. Create a new issue if your problem isn't already reported
3. Provide detailed information about the problem

---

**⭐ Star this repository if you found it helpful!**