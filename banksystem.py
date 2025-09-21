import streamlit as st

# --- Your Bank Class ---
class My_bank:
    bname = "SBI"
    mbl = "BBSR"
    ceo = "Mukesh"
    ifsc = "sbi123456"
    
    def __init__(self, name, email, pho, pan, bal):
        self.__name = name
        self.__email = email
        self.__pho = pho
        self.__pan = pan
        self.__bal = bal
        self.__transactions = []
        self.__pin = None  

    def display(self, upin):
        if upin == self.__pin:
            return {
                "Name": self.__name,
                "Phone": self.__pho,
                "Email": self.__email,
                "PAN": self.__pan,
                "Balance": self.__bal
            }
        else:
            return "❌ Wrong Pin"

    def deposit(self, amount, upan=None):
        if amount > 0:
            if amount >= 50000:
                if upan == self.__pan:
                    self.__bal += amount
                    self.__transactions.append(f"Credited {amount}")
                    return "✅ Transaction Successful"
                else:
                    return "❌ Wrong PAN"
            else:
                self.__bal += amount
                self.__transactions.append(f"Credited {amount}")
                return "✅ Transaction Successful"
        else:
            return "❌ Invalid amount"

    def withdrawal(self, amount):
        if amount > 0:
            if self.__bal >= amount:
                self.__bal -= amount
                self.__transactions.append(f"Debited {amount}")
                return "✅ Transaction Successful"
            else:
                return f"❌ Insufficient Balance ({self.__bal} only)"
        else:
            return "❌ Invalid amount"

    def create_pin(self, new_pin, cnew_pin):
        if self.__pin is None:
            if new_pin == cnew_pin:
                self.__pin = new_pin
                return "✅ Pin Created Successfully"
            else:
                return "❌ Pin not matched"
        else:
            return "⚠️ Pin already exists"

    def ch_pin(self, old_pin, new_pin, cnew_pin):
        if self.__pin:
            if old_pin == self.__pin:
                if new_pin == cnew_pin:
                    self.__pin = new_pin
                    return "✅ Pin Changed Successfully"
                else:
                    return "❌ Pin not matched"
            else:
                return "❌ Wrong pin"
        else:
            return "⚠️ Pin does not exist. Create one first."

    def statements(self):
        return self.__transactions


# --- Streamlit App ---
st.title("🏦 My Bank System")

# Create a customer object (for now, static)
c1 = My_bank("Yosho", "yosho@gmail.com", 7894561320, "yoshopan", 7899)

menu = st.sidebar.selectbox("Choose Action", 
                            ["Create PIN", "Deposit", "Withdraw", "Display Details", "Change PIN", "Statements"])

if menu == "Create PIN":
    np = st.number_input("Enter new PIN", step=1, format="%d")
    cp = st.number_input("Re-enter new PIN", step=1, format="%d")
    if st.button("Set PIN"):
        st.success(c1.create_pin(np, cp))

elif menu == "Deposit":
    amt = st.number_input("Enter deposit amount", step=100, format="%d")
    if amt >= 50000:
        pan = st.text_input("Enter PAN")
    else:
        pan = None
    if st.button("Deposit"):
        st.info(c1.deposit(amt, pan))

elif menu == "Withdraw":
    amt = st.number_input("Enter withdrawal amount", step=100, format="%d")
    if st.button("Withdraw"):
        st.warning(c1.withdrawal(amt))

elif menu == "Display Details":
    pin = st.number_input("Enter PIN", step=1, format="%d")
    if st.button("Show Details"):
        details = c1.display(pin)
        st.json(details)

elif menu == "Change PIN":
    old = st.number_input("Old PIN", step=1, format="%d")
    np = st.number_input("New PIN", step=1, format="%d")
    cp = st.number_input("Confirm New PIN", step=1, format="%d")
    if st.button("Change"):
        st.success(c1.ch_pin(old, np, cp))

elif menu == "Statements":
    st.write("📜 Transaction History:")
    st.write(c1.statements())
