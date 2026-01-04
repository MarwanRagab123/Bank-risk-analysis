

PROJECT_TITLE = "Bank Transaction Fraud Detection System"
PROJECT_NAME = "Project ITI"
ORGANIZATION = "ITI - Information Technology Institute"


SECTIONS = {
    "executive_summary": "Executive Summary",
    "metrics_overview": "Key Metrics Overview",
    "risk_distribution": "Risk Band Distribution",
    "transaction_classification": "Transaction Classification",
    "transaction_amount": "Transaction Amount Distribution",
    "high_risk_customers": "High-Risk Customers",
    "risk_summary": "Risk Band Summary",
    "recommendations": "Recommendations & Actions"
}


RISK_MESSAGES = {
    "high": "HIGH PRIORITY – Immediate review and investigation recommended.",
    "medium": "MEDIUM PRIORITY – Continuous monitoring and regular reviews advised.",
    "low": "LOW PRIORITY – System operating within normal thresholds."
}


COLORS = {
    "low_risk": "#2ecc71",
    "medium_risk": "#f39c12",
    "high_risk": "#e74c3c",
    "normal": "#3498db",
    "flagged": "#c0392b"
}

def display_welcome_banner(self):
    banner = f"""
╔════════════════════════════════════════════════════════════════════════════╗
║                                                                            ║
║   ███████╗██████╗  █████╗ ██╗   ██╗██████╗     █████╗ ███╗   ██╗            ║
║   ██╔════╝██╔══██╗██╔══██╗██║   ██║██╔══██╗   ██╔══██╗████╗  ██║            ║
║   █████╗  ██████╔╝███████║██║   ██║██║  ██║   ███████║██╔██╗ ██║            ║
║   ██╔══╝  ██╔══██╗██╔══██║██║   ██║██║  ██║   ██╔══██║██║╚██╗██║            ║
║   ██║     ██║  ██║██║  ██║╚██████╔╝██████╔╝   ██║  ██║██║ ╚████║            ║
║   ╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝ ╚═════╝    ╚═╝  ╚═╝╚═╝  ╚═══╝            ║
║                                                                            ║
║                     {PROJECT_TITLE.center(44)}                     ║
║                                                                            ║
║                     {PROJECT_NAME.center(44)}                      ║
║                                                                            ║
║        Advanced Analytics  |  Machine Learning  |  Risk Intelligence        ║
║                                                                            ║
╚════════════════════════════════════════════════════════════════════════════╝
"""
    self.console.print(banner, style="bold bright_cyan")
