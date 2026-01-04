from datetime import datetime
import  os


## Note: I used Claude to help generate a well-structured and professional report.


class Report:

    def __init__(self,output_dir="Reports"):
        self.output_dir=output_dir
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir,exist_ok=True)

    def report_txt(self,data):

        report_summary_path = os.path.join(self.output_dir, "Report_Summary.txt")
        flagged=data[data["is_suspicious"]==True]

        with open(report_summary_path, 'w', encoding='utf-8') as f:

            total_transactions = len(data)
            total_flagged = len(flagged)
            flagged_percentage = (total_flagged / total_transactions * 100) if total_transactions else 0
            risk_distribution = data['risk_band'].value_counts()
            top_5_flagged = flagged['nameOrig'].value_counts().head(5)
            top_5_risky = data.sort_values(by="final_risk_score", ascending=False).head(5)


            f.write("=" * 80 + "\n")
            f.write("TRANSACTION FRAUD & RISK ANALYSIS REPORT".center(80) + "\n")
            f.write("=" * 80 + "\n")
            f.write(f"Generated On : {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write(f"Prepared By : Fraud Detection System\n")
            f.write("=" * 80 + "\n\n")


            f.write("1. EXECUTIVE SUMMARY\n")
            f.write("-" * 80 + "\n")
            f.write(
                f"This report analyzes {total_transactions:,} transactions to detect\n"
                f"potential fraudulent behavior using risk scoring and classification.\n\n"
                f"A total of {total_flagged:,} transactions were flagged as suspicious,\n"
                f"representing {flagged_percentage:.2f}% of all processed transactions.\n"
            )

            if flagged_percentage > 5:
                f.write("\nRISK STATUS: HIGH – Immediate review recommended.\n")
            elif flagged_percentage > 2:
                f.write("\nRISK STATUS: MEDIUM – Continuous monitoring advised.\n")
            else:
                f.write("\nRISK STATUS: LOW – System operating within normal thresholds.\n")

            f.write("\n")


            f.write("2. KEY METRICS OVERVIEW\n")
            f.write("-" * 80 + "\n")
            f.write(f"{'Total Transactions':<30}: {total_transactions:>12,}\n")
            f.write(f"{'Flagged Transactions':<30}: {total_flagged:>12,}\n")
            f.write(f"{'Flagged Percentage':<30}: {flagged_percentage:>11.2f}%\n")
            f.write("\n")


            f.write("3. RISK BAND DISTRIBUTION\n")
            f.write("-" * 80 + "\n")
            for band, count in risk_distribution.items():
                percent = (count / total_transactions) * 100
                bar = "#" * int(percent // 2)
                f.write(f"{band:<12} | {bar:<30} {count:>8,} ({percent:>5.2f}%)\n")
            f.write("\n")


            f.write("4. TOP CUSTOMERS WITH REPEATED SUSPICIOUS ACTIVITY\n")
            f.write("-" * 80 + "\n")
            f.write(f"{'Rank':<6}{'Customer ID':<25}{'Flagged Transactions':>20}\n")
            f.write("-" * 80 + "\n")
            for idx, (cust, cnt) in enumerate(top_5_flagged.items(), 1):
                f.write(f"{idx:<6}{cust:<25}{cnt:>20}\n")
            f.write("\n")


            f.write("5. HIGHEST RISK TRANSACTIONS\n")
            f.write("-" * 80 + "\n")
            f.write(f"{'Rank':<6}{'Customer ID':<25}{'Risk Score':>15}{'Risk Band':>15}\n")
            f.write("-" * 80 + "\n")
            for idx, (_, row) in enumerate(top_5_risky.iterrows(), 1):
                f.write(
                    f"{idx:<6}{row['nameOrig']:<25}"
                    f"{row['final_risk_score']:>15.2f}"
                    f"{row['risk_band']:>15}\n"
                )
            f.write("\n")


            f.write("6. RECOMMENDATIONS\n")
            f.write("-" * 80 + "\n")
            f.write(
                "- Review high-risk customers immediately.\n"
                "- Apply enhanced monitoring on flagged accounts.\n"
                "- Re-evaluate transaction limits for repeated offenders.\n"
                "- Schedule periodic audits for model performance.\n"
            )

            f.write("\n" + "=" * 80 + "\n")
            f.write("END OF REPORT".center(80) + "\n")
            f.write("=" * 80 + "\n")
