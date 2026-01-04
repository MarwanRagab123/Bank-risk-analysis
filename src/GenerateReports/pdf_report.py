import os
from datetime import datetime
import matplotlib.pyplot as plt
import matplotlib
from reportlab.lib.pagesizes import letter, A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, PageBreak, Table, TableStyle
from reportlab.lib import colors
from io import BytesIO
import pandas as pd

matplotlib.use('Agg')  


class PDFReportGenerator:
    """Generate comprehensive PDF reports with visualizations for transaction analysis."""
    
    def __init__(self, output_dir="Reports"):
        self.output_dir = output_dir
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir, exist_ok=True)
        self.pdf_path = os.path.join(self.output_dir, "Transaction_Risk_Analysis_Report.pdf")
        self.charts_dir = os.path.join(self.output_dir, "charts_temp")
        if not os.path.exists(self.charts_dir):
            os.makedirs(self.charts_dir, exist_ok=True)
    
    def create_risk_distribution_chart(self, data):
        """Create risk band distribution pie chart."""
        fig, ax = plt.subplots(figsize=(8, 6))
        risk_dist = data['risk_band'].value_counts()
        colors_map = {'Low': '#2ecc71', 'Medium': '#f39c12', 'High': '#e74c3c'}
        chart_colors = [colors_map.get(band, '#95a5a6') for band in risk_dist.index]
        
        ax.pie(risk_dist.values, labels=risk_dist.index, autopct='%1.1f%%',
               colors=chart_colors, startangle=90, textprops={'fontsize': 11, 'weight': 'bold'})
        ax.set_title('Risk Band Distribution', fontsize=14, weight='bold', pad=20)
        
        chart_path = os.path.join(self.charts_dir, "risk_distribution.png")
        plt.savefig(chart_path, dpi=300, bbox_inches='tight')
        plt.close()
        return chart_path
    
    def create_flagged_transactions_chart(self, data):
        """Create flagged vs normal transactions bar chart."""
        fig, ax = plt.subplots(figsize=(8, 6))
        flagged_count = len(data[data['is_suspicious'] == True])
        normal_count = len(data[data['is_suspicious'] == False])
        
        categories = ['Normal', 'Flagged']
        counts = [normal_count, flagged_count]
        bar_colors = ['#2ecc71', '#e74c3c']
        
        bars = ax.bar(categories, counts, color=bar_colors, edgecolor='black', linewidth=1.5)
        ax.set_ylabel('Transaction Count', fontsize=12, weight='bold')
        ax.set_title('Normal vs Flagged Transactions', fontsize=14, weight='bold', pad=20)
        
       
        for bar in bars:
            height = bar.get_height()
            ax.text(bar.get_x() + bar.get_width()/2., height,
                   f'{int(height):,}',
                   ha='center', va='bottom', fontsize=11, weight='bold')
        
        chart_path = os.path.join(self.charts_dir, "flagged_transactions.png")
        plt.savefig(chart_path, dpi=300, bbox_inches='tight')
        plt.close()
        return chart_path
    
    def create_top_customers_chart(self, data):
        """Create top 10 customers by risk score bar chart."""
        fig, ax = plt.subplots(figsize=(10, 6))
        top_customers = data.nlargest(10, 'final_risk_score')[['nameOrig', 'final_risk_score']]
        
        ax.barh(range(len(top_customers)), top_customers['final_risk_score'].values, 
               color='#e74c3c', edgecolor='black', linewidth=1)
        ax.set_yticks(range(len(top_customers)))
        ax.set_yticklabels(top_customers['nameOrig'].values, fontsize=9)
        ax.set_xlabel('Risk Score', fontsize=12, weight='bold')
        ax.set_title('Top 10 Customers by Risk Score', fontsize=14, weight='bold', pad=20)
        ax.invert_yaxis()
        
       
        for i, v in enumerate(top_customers['final_risk_score'].values):
            ax.text(v + 0.1, i, f'{v:.2f}', va='center', fontsize=9, weight='bold')
        
        chart_path = os.path.join(self.charts_dir, "top_customers.png")
        plt.savefig(chart_path, dpi=300, bbox_inches='tight')
        plt.close()
        return chart_path
    
    def create_transaction_amount_chart(self, data):
        """Create transaction amount distribution chart."""
        fig, ax = plt.subplots(figsize=(8, 6))
        
        flagged = data[data['is_suspicious'] == True]['amount']
        normal = data[data['is_suspicious'] == False]['amount']
        
        ax.hist([normal, flagged], bins=30, label=['Normal', 'Flagged'], 
               color=['#2ecc71', '#e74c3c'], edgecolor='black', alpha=0.7)
        ax.set_xlabel('Transaction Amount', fontsize=12, weight='bold')
        ax.set_ylabel('Frequency', fontsize=12, weight='bold')
        ax.set_title('Transaction Amount Distribution', fontsize=14, weight='bold', pad=20)
        ax.legend(fontsize=11)
        ax.grid(True, alpha=0.3)
        
        chart_path = os.path.join(self.charts_dir, "transaction_amount.png")
        plt.savefig(chart_path, dpi=300, bbox_inches='tight')
        plt.close()
        return chart_path
    
    def generate_pdf(self, data):
        """Generate comprehensive PDF report with all visualizations."""
        if data is None or len(data) == 0:
            print("❌ No data available for PDF generation!")
            return None
        
      
        doc = SimpleDocTemplate(self.pdf_path, pagesize=letter,
                               rightMargin=0.5*inch, leftMargin=0.5*inch,
                               topMargin=0.5*inch, bottomMargin=0.5*inch)
        
        story = []
        styles = getSampleStyleSheet()
        
       
        title_style = ParagraphStyle(
            'CustomTitle',
            parent=styles['Heading1'],
            fontSize=24,
            textColor=colors.HexColor('#2c3e50'),
            spaceAfter=30,
            alignment=1,  
            weight='bold'
        )
        
        heading_style = ParagraphStyle(
            'CustomHeading',
            parent=styles['Heading2'],
            fontSize=14,
            textColor=colors.HexColor('#34495e'),
            spaceAfter=12,
            spaceBefore=12,
            weight='bold'
        )
        
      
        title = Paragraph("Transaction Risk Analysis Report", title_style)
        story.append(title)
        
        
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        meta_text = f"<b>Generated On:</b> {timestamp} | <b>Total Transactions:</b> {len(data):,}"
        story.append(Paragraph(meta_text, styles['Normal']))
        story.append(Spacer(1, 0.2*inch))
        
     
        flagged = data[data['is_suspicious'] == True]
        total_flagged = len(flagged)
        flagged_pct = (total_flagged / len(data) * 100) if len(data) else 0
        
        story.append(Paragraph("Executive Summary", heading_style))
        
        summary_text = f"""
        This report analyzes <b>{len(data):,} transactions</b> for potential fraudulent behavior 
        using risk scoring and classification.<br/><br/>
        <b>Key Findings:</b><br/>
        • Total Flagged Transactions: <b>{total_flagged:,}</b> ({flagged_pct:.2f}%)<br/>
        • Average Risk Score: <b>{data['final_risk_score'].mean():.2f}</b><br/>
        • Highest Risk Score: <b>{data['final_risk_score'].max():.2f}</b><br/>
        • Risk Status: <b>{'HIGH' if flagged_pct > 5 else 'MEDIUM' if flagged_pct > 2 else 'LOW'}</b>
        """
        story.append(Paragraph(summary_text, styles['Normal']))
        story.append(Spacer(1, 0.3*inch))
        
       
        story.append(Paragraph("Risk Band Distribution", heading_style))
        risk_chart = self.create_risk_distribution_chart(data)
        story.append(Image(risk_chart, width=5*inch, height=3.75*inch))
        story.append(Spacer(1, 0.2*inch))
        
        
        story.append(PageBreak())
        
     
        story.append(Paragraph("Transaction Classification", heading_style))
        flagged_chart = self.create_flagged_transactions_chart(data)
        story.append(Image(flagged_chart, width=5*inch, height=3.75*inch))
        story.append(Spacer(1, 0.3*inch))
        
      
        story.append(Paragraph("Transaction Amount Distribution", heading_style))
        amount_chart = self.create_transaction_amount_chart(data)
        story.append(Image(amount_chart, width=5*inch, height=3.75*inch))
        
    
        story.append(PageBreak())
        
       
        story.append(Paragraph("High-Risk Customers", heading_style))
        customers_chart = self.create_top_customers_chart(data)
        story.append(Image(customers_chart, width=6*inch, height=4.5*inch))
        story.append(Spacer(1, 0.3*inch))
        
      
        story.append(Paragraph("Risk Band Summary", heading_style))
        risk_summary = data['risk_band'].value_counts().to_frame()
        risk_summary['Percentage'] = (risk_summary['count'] / len(data) * 100).round(2)
        
        table_data = [['Risk Band', 'Count', 'Percentage']]
        for idx, row in risk_summary.iterrows():
            table_data.append([str(idx), str(int(row['count'])), f"{row['Percentage']:.2f}%"])
        
        table = Table(table_data, colWidths=[2*inch, 1.5*inch, 1.5*inch])
        table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#34495e')),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, 0), 12),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
            ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
            ('GRID', (0, 0), (-1, -1), 1, colors.black),
            ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
            ('FONTSIZE', (0, 1), (-1, -1), 10),
        ]))
        story.append(table)
        
    
        doc.build(story)
        
        

        self._cleanup_charts()
        return self.pdf_path
    
    def _cleanup_charts(self):
        """Remove temporary chart files."""
        import shutil
        if os.path.exists(self.charts_dir):
            shutil.rmtree(self.charts_dir)
