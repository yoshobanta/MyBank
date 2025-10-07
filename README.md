# 🏦 MyBank - Streamlit Banking System

A comprehensive web-based banking system built with Streamlit that simulates real-world banking operations through an intuitive user interface.

## 📋 Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Technology Stack](#technology-stack)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Security Features](#security-features)
- [Screenshots](#screenshots)
- [Future Enhancements](#future-enhancements)
- [Contributing](#contributing)
- [License](#license)

## 🌟 Overview

MyBank is an educational banking system that demonstrates core banking principles and Streamlit web development capabilities. The application provides a complete account management system with secure transactions, user authentication, and comprehensive banking operations.

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

## 📦 Installation

### Prerequisites
- Python 3.7 or higher
- pip package manager

### Steps

1. **Clone the repository**
   ```bash
   git clone https://github.com/yoshobanta/MyBank.git
   cd MyBank
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**
   ```bash
   streamlit run app.py
   ```

4. **Access the application**
   - Open your web browser
   - Navigate to `http://localhost:8501`

## 🚀 Usage

### Getting Started

1. **Create Account**
   - Navigate to "Create Account" from the sidebar
   - Fill in your personal details
   - Set a 4-digit PIN
   - Set initial balance

2. **Login**
   - Use your email and PIN to login
   - Access all banking features after successful authentication

3. **Banking Operations**
   - **Deposit**: Add money to your account
   - **Withdraw**: Remove money (requires PIN verification)
   - **Check Balance**: View current balance (requires PIN)
   - **View Statements**: See transaction history and download CSV
   - **Transfer Funds**: Send money to other accounts in the system
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

### Code Structure

```python
# Helper Functions
├── hash_pin()          # PIN encryption using SHA-256
└── validate_email()    # Email format validation

# MyBank Class
├── __init__()          # Initialize account
├── check_pin()         # PIN authentication
├── deposit()           # Add money to account
├── withdraw()          # Remove money from account
├── get_balance()       # Retrieve account balance
├── change_pin()        # Update account PIN
└── add_transaction()   # Log transactions

# Streamlit Interface
├── Session State Management
├── Sidebar Navigation
├── Account Creation Form
├── Login System
└── Banking Operations Interface
```

## 🔒 Security Features

- **PIN Encryption**: All PINs are hashed using SHA-256 before storage
- **Authentication Required**: PIN verification for sensitive operations
- **Input Validation**: 
  - Email format validation
  - 10-digit phone number validation
  - 4-digit PIN requirement
- **Balance Protection**: Prevents overdrafts and negative balances
- **Session Management**: Secure user session handling

## 📸 Screenshots

### Main Interface
![Banking System Interface](screenshots/main-interface.png)

### Account Creation
![Create Account Form](screenshots/create-account.png)

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