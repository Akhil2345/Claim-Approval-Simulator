# 📘 Business Requirements Document (BRD)

## 🛡️ Project: Claim Approval Process Simulator

**Objective:**  
To automate the validation and approval of structured life insurance claim data using clearly defined business rules, reducing manual effort and improving accuracy in reinsurance workflows.

---

## 👥 Stakeholders

| Role               | Responsibility                                         |
|--------------------|--------------------------------------------------------|
| Business Analyst   | Gathers requirements, defines rules, validates output |
| Claims Officer     | Submits claims data for processing                    |
| QA / UAT Analyst   | Tests scenarios and validates outcomes                |
| Developer          | Implements business rules in code                     |

---

## 🧩 Functional Requirements

| FR ID | Requirement Description                                           |
|-------|-------------------------------------------------------------------|
| FR1   | System must accept CSV uploads containing structured claim data   |
| FR2   | System must apply rule-based validation to each claim             |
| FR3   | System must display a decision (Approved/Rejected + Reason)      |
| FR4   | User must be able to drill down into an individual claim          |
| FR5   | System must show a visual summary (dashboard) of status counts    |
| FR6   | A test case table must validate all business rules                |

---

## 📏 Business Rules

| Rule ID | Description                                      |
|---------|--------------------------------------------------|
| R1      | Reject if `Age > 65`                             |
| R2      | Reject if `PolicyStatus != Active`              |
| R3      | Reject if `ClaimAmount > ₹10,00,000`             |
| R4      | Approve if none of the above apply               |

---

## 📁 Input Data Format

Accepted as `.csv` with the following fields:

- `ClaimID` (string)
- `Name` (string)
- `Age` (int)
- `PolicyType` (string)
- `ClaimAmount` (float)
- `PolicyStatus` (string)
- `ClaimDate` (YYYY-MM-DD)

---

## ✅ Acceptance Criteria

- Claims are correctly flagged based on defined rules
- Rule violations are visible with appropriate labels
- UAT test cases pass 100% (see `UAT_Test_Plan.md`)
- Dashboard shows accurate summary of decision outcomes

---

## 📌 Notes

- This is a simulated system meant for demonstration purposes
- It can be extended to include fraud detection, audit logging, or integration with external claim systems

---

> Prepared by: Akhil Kumar  
> Last updated: August 2025
