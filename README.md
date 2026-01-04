
````markdown
# Bank Analysis

**Bank Analysis** is a compact, end-to-end pipeline for analyzing bank transaction data.  
It loads transactions, builds features, computes customer risk scores, flags suspicious
transactions, and exports clean, formatted reports (CSV / TXT / PDF).

---

## Project Overview

The pipeline follows these steps:

1. Load transaction data  
2. Clean and preprocess data  
3. Build analytical features  
4. Compute customer risk scores  
5. Flag suspicious transactions  
6. Export reports  

All steps are accessible through an interactive console menu.

---

## Key Features

- Transaction data loading and cleaning  
- Feature engineering for fraud detection  
- Customer risk scoring  
- Suspicious transaction flagging  
- Report generation:
  - CSV
  - TXT
  - PDF  
- Simple interactive console interface  

---

## Prerequisites

- Python 3.9+  
- pip  

---

## Setup (Quick Start)

1. Open a terminal and navigate to the project root (the folder containing `main.py`):

```powershell
cd "<path-to-repo-root>"
````

2. Create and activate a virtual environment (recommended):

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1   # PowerShell
# or
.\.venv\Scripts\activate      # cmd.exe
```

3. Install dependencies:

```powershell
pip install -r requirements.txt
```

> **Note:** An optional pre-configured virtual environment may exist at
> `bank_analysis/`. You can activate it if you prefer.

---

## Run the Application

From the project root, run:

```powershell
python main.py
```

Use the interactive menu to execute the pipeline in order:

```
load -> clean -> build -> score -> flag -> export
```

---

## Reports / Outputs

All generated outputs are saved in the `Reports/` folder.

Typical outputs include:

* `customer_risk_summary.csv`
* `flagged_transactions.csv`
* `Report_Summary.txt`
* PDF summary report

---

## Project Structure

```
.
├─ main.py
├─ README.md
├─ requirements.txt
├─ data/
│  └─ test_data.csv
├─ model/
│  └─ reports/
├─ Reports/
│  ├─ customer_risk_summary.csv
│  ├─ flagged_transactions.csv
│  └─ Report_Summary.txt
├─ src/
│  ├─ Console_App.py
│  ├─ ConsoleSummary/
│  │  └─ console_summary.py
│  ├─ DataManager/
│  │  └─ data_manger.py
│  ├─ FeatureBuilder/
│  │  └─ feature_builder.py
│  ├─ GenerateReports/
│  │  ├─ generate_reports.py
│  │  └─ pdf_report.py
│  ├─ RiskScore/
│  │  └─ risk_score.py
│  ├─ TransactionFlagger/
│  │  └─ transaction_flagger.py
│  └─ __pycache__/
└─ bank_analysis/   # optional virtual environment
```

---

## Quick Commands

```powershell
# activate venv (PowerShell)
.\.venv\Scripts\Activate.ps1

# install dependencies
pip install -r requirements.txt

# run application
python main.py
```

---

## Notes

* Always run pipeline steps in order:
  **load → clean → build → score → flag → export**
* If you encounter missing package errors, re-run:

  ```powershell
  pip install -r requirements.txt
  ```

  inside the activated virtual environment.
