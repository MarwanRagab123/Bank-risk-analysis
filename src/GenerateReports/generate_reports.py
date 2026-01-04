import os
from model.reports.report import Report
from .pdf_report import PDFReportGenerator


class GenerateReports:
    def __init__(self, output_dir="Reports"):
        self.output_dir = output_dir
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)
        self.re=Report(output_dir=self.output_dir)
        self.pdf_generator = PDFReportGenerator(output_dir=self.output_dir)



    def generate_reports(self, data):
        if data is not None:
            flagged_path = os.path.join(self.output_dir, 'flagged_transactions.csv')
            customer_summary_path = os.path.join(self.output_dir, 'customer_risk_summary.csv')

            flagged = data[data["is_suspicious"] == True]
            flagged.to_csv(flagged_path, index=False)

            customer_summary = data.groupby("nameOrig").agg({
                "final_risk_score": "max",
                "risk_band": "last"
            }).reset_index()
            customer_summary.to_csv(customer_summary_path, index=False)


            self.re.report_txt(data)
            
            
            self.pdf_generator.generate_pdf(data)


            print(f"✅ Reports saved in folder: {self.output_dir}")
        else:
            print("❌ Not exist Data please Load the data first!\n")