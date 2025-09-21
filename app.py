import streamlit as st
import pandas as pd
import hashlib

# -------------------------------
# Helper Functions
# -------------------------------
def hash_pin(pin):
    """Hash the PIN using SHA-256"""
    return hashlib.sha256(pin.encode()).hexdigest()

def validate_email(email):
    return "@" in email and "." in email

# -------------------------------
# Bank Class
# -------------------------------
class MyBank:
    def __init__(self, name, email, phone, pan, bal, pin):
        self.name = name
        self.email = email
        self.phone = phone
        self.pan = pan
        self.balance = bal
        self.transactions = []
        self.pin = hash_pin(pin)

    def check_pin(self, pin):
        return self.pin == hash_pin(pin)

    def deposit(self, amt):
        if amt > 0:
            self.balance += amt
            self.transactions.append(f"Deposited ₹{amt}")
            return True
        return False

    def withdraw(self, amt, pin):
        if self.check_pin(pin):
            if amt <= self.balance:
                self.balance -= amt
                self.transactions.append(f"Withdrew ₹{amt}")
                return True
            return False
        return None  # wrong PIN

    def get_balance(self, pin):
        if self.check_pin(pin):
            return self.balance
        return None

    def change_pin(self, old_pin, new_pin):
        if self.check_pin(old_pin):
            self.pin = hash_pin(new_pin)
            return True
        return False

    def add_transaction(self, message):
        self.transactions.append(message)

# -------------------------------
# Initialize Session State
# -------------------------------
if "accounts" not in st.session_state:
    st.session_state.accounts = {}  # key=email, value=MyBank object
if "current_user" not in st.session_state:
    st.session_state.current_user = None

# -------------------------------
# Sidebar Menu
# -------------------------------
st.sidebar.title("🏦 Bank System Menu")
menu_options = ["Create Account", "Login", "Deposit", "Withdraw", 
                "Balance Enquiry", "Statements", "Change PIN", "Fund Transfer"]
menu = st.sidebar.radio("Select an option", menu_options)

# -------------------------------
# Create Account
# -------------------------------
if menu == "Create Account":
    st.subheader("📝 Create New Bank Account")
    with st.form("create_form"):
        name = st.text_input("Name")
        email = st.text_input("Email")
        phone = st.text_input("Phone")
        pan = st.text_input("PAN")
        bal = st.number_input("Initial Balance", min_value=0, step=100)
        pin = st.text_input("Set 4-digit PIN", type="password")
        submitted = st.form_submit_button("Create Account")

        if submitted:
            if email in st.session_state.accounts:
                st.error("An account with this email already exists!")
            elif len(phone) != 10 or not phone.isdigit():
                st.error("Enter a valid 10-digit phone number.")
            elif len(pin) != 4 or not pin.isdigit():
                st.error("PIN must be 4 digits.")
            elif not validate_email(email):
                st.error("Enter a valid email address.")
            else:
                account = MyBank(name, email, phone, pan, bal, pin)
                st.session_state.accounts[email] = account
                st.success(f"Account created for {name} with ₹{bal} balance!")

# -------------------------------
# Login
# -------------------------------
elif menu == "Login":
    st.subheader("🔑 Login")
    email = st.text_input("Enter Email")
    pin = st.text_input("Enter PIN", type="password")
    if st.button("Login"):
        if email in st.session_state.accounts:
            account = st.session_state.accounts[email]
            if account.check_pin(pin):
                st.session_state.current_user = email
                st.success(f"Welcome {account.name}!")
            else:
                st.error("Invalid PIN!")
        else:
            st.error("No account found with this email.")

# -------------------------------
# Operations Require Login
# -------------------------------
if menu in ["Deposit", "Withdraw", "Balance Enquiry", "Statements", "Change PIN", "Fund Transfer"]:
    if st.session_state.current_user:
        user = st.session_state.accounts[st.session_state.current_user]

        # Deposit
        if menu == "Deposit":
            st.subheader("💰 Deposit Money")
            amt = st.number_input("Enter deposit amount", min_value=1, step=100)
            if st.button("Deposit"):
                if user.deposit(amt):
                    st.success(f"Deposited ₹{amt} successfully! New Balance: ₹{user.balance}")

        # Withdraw
        elif menu == "Withdraw":
            st.subheader("💸 Withdraw Money")
            amt = st.number_input("Enter withdrawal amount", min_value=1, step=100)
            pin = st.text_input("Enter PIN", type="password", key="withdraw_pin")
            if st.button("Withdraw"):
                result = user.withdraw(amt, pin)
                if result is True:
                    st.success(f"Withdrew ₹{amt} successfully! New Balance: ₹{user.balance}")
                elif result is False:
                    st.error("Insufficient balance!")
                else:
                    st.error("Invalid PIN!")

        # Balance Enquiry
        elif menu == "Balance Enquiry":
            st.subheader("💳 Balance Enquiry")
            pin = st.text_input("Enter PIN", type="password", key="balance_pin")
            if st.button("Check Balance"):
                bal = user.get_balance(pin)
                if bal is not None:
                    st.metric("Available Balance", f"₹{bal}")
                else:
                    st.error("Invalid PIN!")

        # Statements
        elif menu == "Statements":
            st.subheader("📜 Transaction History")
            txns = user.transactions
            if txns:
                df = pd.DataFrame(txns, columns=["Transaction"])
                st.table(df)
                st.download_button("Download Transactions as CSV", df.to_csv(index=False), file_name="transactions.csv")
            else:
                st.info("No transactions yet.")

        # Change PIN
        elif menu == "Change PIN":
            st.subheader("🔑 Change PIN")
            old_pin = st.text_input("Enter Old PIN", type="password", key="old_pin")
            new_pin = st.text_input("Enter New PIN", type="password", key="new_pin")
            if st.button("Update PIN"):
                if len(new_pin) != 4 or not new_pin.isdigit():
                    st.error("PIN must be 4 digits.")
                elif user.change_pin(old_pin, new_pin):
                    st.success("PIN updated successfully!")
                else:
                    st.error("Invalid old PIN!")

        # Fund Transfer
        elif menu == "Fund Transfer":
            st.subheader("🔁 Transfer Funds")
            recipient_email = st.text_input("Recipient Email")
            amt = st.number_input("Amount to Transfer", min_value=1, step=100)
            pin = st.text_input("Enter Your PIN", type="password", key="transfer_pin")
            if st.button("Transfer"):
                if recipient_email not in st.session_state.accounts:
                    st.error("Recipient account not found!")
                elif not user.check_pin(pin):
                    st.error("Invalid PIN!")
                elif amt > user.balance:
                    st.error("Insufficient balance!")
                else:
                    recipient = st.session_state.accounts[recipient_email]
                    user.withdraw(amt, pin)
                    recipient.deposit(amt)
                    user.add_transaction(f"Transferred ₹{amt} to {recipient_email}")
                    recipient.add_transaction(f"Received ₹{amt} from {user.email}")
                    st.success(f"₹{amt} transferred to {recipient_email} successfully! New Balance: ₹{user.balance}")

    else:
        st.warning("Please login first.")
