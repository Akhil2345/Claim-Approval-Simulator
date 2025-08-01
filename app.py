import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

# Load dataset
st.header("📤 Upload Claim CSV File")
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
 

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.success("✅ File uploaded successfully!")
else:
    st.warning("⚠️ Please upload a `claims.csv` file to continue.")
    st.stop()


# Apply rules
def validate_claim(row):
    if row['Age'] > 65:
        return "Rejected - Age Limit"
    elif row['PolicyStatus'] != "Active":
        return "Rejected - Inactive Policy"
    elif row['ClaimAmount'] > 1000000:
        return "Rejected - Amount Too High"
    else:
        return "Approved"

df["Status"] = df.apply(validate_claim, axis=1)

# Streamlit UI
st.title("🛡️ Reinsurance Claim Approval Simulator")
st.markdown("📂 Loaded data from `claims.csv`")


st.dataframe(df)

# Dashboard
st.subheader("📊 Approval Status Overview")
status_counts = df["Status"].value_counts()
st.bar_chart(status_counts)

# Individual claim checker
st.subheader("🔍 Check Individual Claim")

claim_id = st.selectbox("Choose Claim ID:", df["ClaimID"].unique())
selected = df[df["ClaimID"] == claim_id].iloc[0]

st.write(f"**Name**: {selected['Name']}")
st.write(f"**Age**: {selected['Age']}")
st.write(f"**Policy Type**: {selected['PolicyType']}")
st.write(f"**Claim Amount**: {selected['ClaimAmount']}")
st.write(f"**Policy Status**: {selected['PolicyStatus']}")
st.write(f"### ✅ Result: {selected['Status']}")

# ---------------------------
# 🧪 Test Cases Section
# ---------------------------
st.subheader("🧪 Validation Test Cases")

test_data = [
    {"TestCase": "Valid Claim", "Age": 45, "PolicyStatus": "Active", "Amount": 500000, "Expected": "Approved"},
    {"TestCase": "Age > 65", "Age": 70, "PolicyStatus": "Active", "Amount": 500000, "Expected": "Rejected - Age Limit"},
    {"TestCase": "Inactive Policy", "Age": 50, "PolicyStatus": "Inactive", "Amount": 400000, "Expected": "Rejected - Inactive Policy"},
    {"TestCase": "High Amount", "Age": 40, "PolicyStatus": "Active", "Amount": 1500000, "Expected": "Rejected - Amount Too High"},
    {"TestCase": "Edge Case: Age = 65", "Age": 65, "PolicyStatus": "Active", "Amount": 500000, "Expected": "Approved"},
    {"TestCase": "Edge Case: Amount = 10L", "Age": 50, "PolicyStatus": "Active", "Amount": 1000000, "Expected": "Approved"},
]

test_df = pd.DataFrame(test_data)

# Reuse validation function
def check(row):
    if row["Age"] > 65:
        return "Rejected - Age Limit"
    elif row["PolicyStatus"] != "Active":
        return "Rejected - Inactive Policy"
    elif row["Amount"] > 1000000:
        return "Rejected - Amount Too High"
    else:
        return "Approved"

test_df["Result"] = test_df.apply(check, axis=1)
test_df["Pass/Fail"] = test_df["Expected"] == test_df["Result"]

st.dataframe(test_df)
