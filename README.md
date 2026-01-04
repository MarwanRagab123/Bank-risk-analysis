# Bank Analysis

**Bank Analysis** is a comprehensive end-to-end pipeline for analyzing bank transaction data and detecting fraudulent activity. It loads transaction data, performs data cleaning, builds advanced analytical features, computes customer risk scores using statistical methods, flags suspicious transactions, and exports professional reports in multiple formats (CSV, TXT, PDF).

---

## Project Overview

The pipeline follows a structured workflow:

1. **Load** - Import transaction data from CSV files
2. **Clean** - Remove null values and duplicates
3. **Build** - Engineer features for fraud detection analysis
4. **Score** - Calculate customer risk scores using statistical normalization
5. **Flag** - Identify and flag suspicious transactions
6. **Export** - Generate comprehensive reports

All steps are accessible through an intuitive interactive console menu with real-time feedback.

---

## Key Features

### Core Functionality
- **Data Management** - Load and validate transaction data with error handling
- **Data Cleaning** - Remove duplicates and null values for data quality
- **Feature Engineering** - Build 6+ analytical features including transaction velocity, amount patterns, and balance anomalies
- **Risk Scoring** - Advanced statistical risk calculation with z-score normalization
  - Low Risk (< 40)
  - Medium Risk (40-70)
  - High Risk (70-90)
  - Critical Risk (≥ 90)
- **Transaction Flagging** - Detect and flag suspicious transactions based on risk thresholds
- **Report Generation**
  - CSV export for data analysis
  - TXT summary reports
  - PDF formatted reports with charts and visualizations
- **Interactive Console Interface** - Rich, user-friendly CLI with real-time status updates

### Technologies Used
- **pandas** - Data manipulation and analysis
- **numpy** - Numerical computations
- **scipy** - Statistical analysis and distributions
- **matplotlib** - Data visualization
- **reportlab** - PDF report generation
- **rich** - Beautiful console output and formatting

---

## Project Structure

```
Bank_AnalysisV2/
├── main.py                          # Entry point
├── requirements.txt                 # Project dependencies
├── constant/
│   └── shape.py                     # Project constants and configuration
├── src/
│   ├── Console_App.py               # Main console application
│   ├── DataManager/
│   │   └── data_manger.py           # Data loading and cleaning
│   ├── FeatureBuilder/
│   │   └── feature_builder.py       # Feature engineering
│   ├── RiskScore/
│   │   └── risk_score.py            # Risk scoring engine
│   ├── TransactionFlagger/
│   │   └── transaction_flagger.py   # Transaction flagging logic
│   ├── GenerateReports/
│   │   ├── generate_reports.py      # Report generation
│   │   └── pdf_report.py            # PDF report formatting
│   └── ConsoleSummary/
│       └── console_summary.py       # Console output formatting
├── model/
│   └── reports/
│       └── report.py                # Report models
├── Reports/                         # Output directory for generated reports
└── bank_analysis/                   # Pre-configured Python virtual environment
```

---

## Prerequisites

- Python 3.9+
- pip (Python package manager)

---

## Setup (Quick Start)

### Option 1: Using Pre-configured Virtual Environment

A pre-configured virtual environment is included at `bank_analysis/`:

**PowerShell:**
```powershell
.\bank_analysis\Scripts\Activate.ps1
```

**Command Prompt:**
```cmd
.\bank_analysis\Scripts\activate.bat
```

### Option 2: Create a New Virtual Environment

1. Navigate to the project root:
```powershell
cd "<path-to-Bank_AnalysisV2>"
```

2. Create a virtual environment:
```powershell
python -m venv venv
```

3. Activate it:
   - **PowerShell:** `.\.venv\Scripts\Activate.ps1`
   - **Command Prompt:** `.\.venv\Scripts\activate`

4. Install dependencies:
```powershell
pip install -r requirements.txt
```

---

## Run the Application

From the project root, execute:

```powershell
python main.py
```

Follow the interactive menu prompts to execute each step of the pipeline:

```
┌─────────────────────────┐
│ 1. Load Data            │
│ 2. Clean Data           │
│ 3. Build Features       │
│ 4. Calculate Risk Score │
│ 5. Flag Transactions    │
│ 6. Generate Reports     │
│ 7. Exit                 │
└─────────────────────────┘
```

Execute steps in order for optimal results: **Load → Clean → Build → Score → Flag → Export**

---

## Reports / Outputs

All generated outputs are automatically saved in the `Reports/` folder.

### Typical Outputs
- `customer_risk_summary.csv` - Customer risk scores by category
- `flagged_transactions.csv` - Details of flagged suspicious transactions
- `Report_Summary.txt` - Text summary of analysis results
- `charts_temp/` - Temporary chart files for visualizations
- PDF reports with charts and summaries

---

## Dependencies

| Package | Version | Purpose |
|---------|---------|---------|
| pandas | 2.3.3 | Data manipulation |
| numpy | 2.4.0 | Numerical computing |
| scipy | 1.16.3 | Statistical analysis |
| rich | ≥13.0.0 | Beautiful CLI output |
| matplotlib | ≥3.8.0 | Data visualization |
| reportlab | ≥4.0.0 | PDF generation |

---

## Quick Commands

```powershell
# Activate pre-configured virtual environment
.\bank_analysis\Scripts\Activate.ps1

# Or create and activate a new virtual environment
python -m venv venv
.\venv\Scripts\Activate.ps1

# Install dependencies
pip install -r requirements.txt

# Run the application
python main.py
```

---

## Notes

- Always execute pipeline steps in order: **Load → Clean → Build → Score → Flag → Export**
- Ensure your CSV input file contains appropriate transaction columns for feature engineering
- All reports are timestamped and saved automatically in the `Reports/` directory
- The console interface provides step-by-step guidance and error messages
- Risk scores are normalized using z-score methodology for accuracy
- If you encounter missing package errors, reinstall dependencies inside the activated virtual environment

---

## Author

ITI Project - Bank Analysis V2
