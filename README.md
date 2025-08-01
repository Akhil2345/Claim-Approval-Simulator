# 🛡️ Claim Approval Simulator

A business process automation project simulating real-world reinsurance claim validation using structured data, rule-based logic, and test-driven development. Built with Streamlit for a simple interactive interface that supports CSV upload, real-time feedback, and QA test validation.

---

## 🔍 Project Summary

This tool demonstrates how manual claim approvals in a reinsurance context can be streamlined using automation. It reflects typical business analyst tasks like:

- Requirement gathering
- Rule definition and documentation
- Validation logic implementation
- Functional testing & UAT preparation
- Dashboard reporting

It is designed to highlight cross-functional skills across product thinking, QA processes, and lightweight technical delivery.

---

## 🧠 Features

- 📤 **CSV Upload** – Upload life reinsurance claim data for processing
- ✅ **Business Rule Engine** – Applies domain rules:
  - Reject if `Age > 65`
  - Reject if `PolicyStatus != Active`
  - Reject if `ClaimAmount > ₹10,00,000`
- 📊 **Dashboard View** – Visual breakdown of approved vs rejected claims
- 🔍 **Claim Drill-down** – Select any claim to view decision logic
- 🧪 **UAT Test Case Table** – Built-in test suite to verify validation logic

---

## 🚀 Tech Stack

- **Streamlit** – UI and dashboard
- **Python / Pandas** – Rule engine and data validation
- **CSV** – Input format for structured claims
- **Matplotlib** – Visualization (bar charts)
- **Test Logic** – Manual QA test case mapping

---

## 📁 Sample CSV Format

| ClaimID | Name       | Age | PolicyType | ClaimAmount | PolicyStatus | ClaimDate   |
|---------|------------|-----|------------|-------------|---------------|-------------|
| C001    | Anil Kumar | 45  | Term       | 500000      | Active        | 2025-07-01  |

---

## 💼 Relevance

This project aligns with:
- Technical Business Analyst workflows
- Insurance / Reinsurance / Fintech domains
- Agile QA test case design
- Low-code prototyping for stakeholder demos

It was built to demonstrate both process understanding and automation potential for operational tasks.

---

## 📦 Run It Locally

```bash
pip install -r requirements.txt
streamlit run app.py
