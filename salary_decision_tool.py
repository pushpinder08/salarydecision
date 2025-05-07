import streamlit as st

# ----------------------------
# Helper Functions
# ----------------------------
def pv_factor(y, r): return (1 - (1 + r) ** (-y)) / r
def pv_base(y, r, x): return x * pv_factor(y, r)
def pv_a(y, r, x): return 0.10 * x + 1.10 * x * pv_factor(y, r)
def pv_b(y, t, r, x): return 0.08 * t * x + 1.08 * x * pv_factor(y, r)

# ----------------------------
# Title and Inputs
# ----------------------------
st.title("💰 Salary Decision Tool")

x = st.number_input("Current annual salary (x)", value=100000.0, step=1000.0)
y = st.number_input("Years you plan to stay (y)", value=10.0, step=1.0)
t = st.number_input("t = How many years ago did you join the university?", value=2.0, step=1.0)
r = 0.04  # Fixed inflation-adjusted discount rate

# ----------------------------
# Calculations
# ----------------------------
base = pv_base(y, r, x)
a = pv_a(y, r, x)
b = pv_b(y, t, r, x)

# ----------------------------
# Output
# ----------------------------
st.markdown("### 🧾 What Are the Options?")
st.write("**Option A:** Get a **10% raise** from today and a **10% bonus** based on your current salary now.")
st.write("**Option B:** Get an **8% raise** from today and a **(8% × t)** bonus — where `t` is how long ago you joined.")

st.markdown("### 📊 Present Value (in today's $)")
st.write(f"**Baseline (no raise):** ${base:,.2f}")
st.write(f"**Option A (10% raise + 10% bonus):** ${a:,.2f}")
st.write(f"**Option B (8% raise + 8%×{t:.0f}% bonus):** ${b:,.2f}")

st.markdown("### 🔍 Additional Earnings Over Baseline")
st.write(f"**Option A:** ${a - base:,.2f}")
st.write(f"**Option B:** ${b - base:,.2f}")

if b > a:
    st.success("👉 Option B gives more additional value.")
elif a > b:
    st.success("👉 Option A gives more additional value.")
else:
    st.info("👉 Both options provide equal value.")
