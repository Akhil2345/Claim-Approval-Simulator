# Claim Approval Simulator

A Streamlit-based tool to automate and simulate reinsurance claim approvals using business logic and structured CSV data.

## Features

- 📤 Upload claim CSV files
- ✅ Auto-validate based on business rules:
  - Reject if age > 65
  - Reject if policy is inactive
  - Reject if claim > ₹10,00,000
- 📊 Approval dashboard
- 🔍 Individual claim analysis
- 🧪 Test cases to verify rule logic

## Run the App

```bash
pip install -r requirements.txt
streamlit run app.py
