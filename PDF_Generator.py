import os
import pandas as pd
import matplotlib.pyplot as plt
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, Image, PageBreak
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from datetime import datetime

def generate_combined_emotion_report(csv_folder, output_pdf, employee_name="John Doe", company_name="EmotionTech Solutions"):
    # Collect all Day-*.csv files
    csv_files = sorted([f for f in os.listdir(csv_folder) if f.startswith('Day-') and f.endswith('.csv')])
    
    # Combine data
    combined_df = pd.DataFrame()
    for file in csv_files:
        path = os.path.join(csv_folder, file)
        df = pd.read_csv(path)
        df['Confidence'] = df['Confidence'].str.replace('%', '').astype(int)
        df['Day'] = file.replace('.csv', '')
        combined_df = pd.concat([combined_df, df], ignore_index=True)

    # Setup report
    doc = SimpleDocTemplate(output_pdf, pagesize=A4)
    styles = getSampleStyleSheet()
    title_style = ParagraphStyle(name='TitleStyle', parent=styles['Title'], alignment=1)
    normal_centered = ParagraphStyle(name='NormalCentered', parent=styles['Normal'], alignment=1)
    elements = []

    # Header
    elements.append(Paragraph("<b>Combined Employee Emotion Report</b>", title_style))
    elements.append(Spacer(1, 12))
    elements.append(Paragraph(f"<b>Employee Name:</b> {employee_name}", styles['Normal']))
    elements.append(Paragraph(f"<b>Company Name:</b> {company_name}", styles['Normal']))
    elements.append(Paragraph(f"<b>Report Generated:</b> {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}", styles['Normal']))
    elements.append(Spacer(1, 12))

    # Summary
    emotion_counts = combined_df['Emotion'].value_counts().to_dict()
    dominant_emotion = max(emotion_counts, key=emotion_counts.get)
    average_confidence = combined_df['Confidence'].mean()

    readable_days = ", ".join([f.replace('.csv', '') for f in csv_files])
    summary_text = f"""
    <b>Summary:</b><br/>
    Days Covered: {len(csv_files)} ({readable_days})<br/>
    Total Entries: {len(combined_df)}<br/>
    Dominant Emotion: <b>{dominant_emotion}</b><br/>
    Emotion Distribution: {emotion_counts}<br/>
    Average Confidence: {average_confidence:.2f}%
    """
    elements.append(Paragraph(summary_text, styles['BodyText']))
    elements.append(Spacer(1, 12))

    # Pie Chart
    plt.figure(figsize=(4, 4))
    combined_df['Emotion'].value_counts().plot.pie(autopct='%1.0f%%', startangle=90)
    plt.title("Overall Emotion Distribution")
    plt.ylabel('')
    pie_chart_path = os.path.join(csv_folder, 'combined_pie.png')
    plt.savefig(pie_chart_path)
    plt.close()
    elements.append(Image(pie_chart_path, width=200, height=200))
    elements.append(Spacer(1, 12))

    # Line Chart - Confidence Over Time
    plt.figure(figsize=(6, 3))
    combined_df['Timestamp'] = pd.to_datetime(combined_df['Timestamp (IST)'])
    combined_df = combined_df.sort_values(by='Timestamp')
    plt.plot(combined_df['Timestamp'], combined_df['Confidence'], marker='o', linestyle='-', color='green')
    plt.title("Confidence Over Time")
    plt.xticks(rotation=45, fontsize=6)
    plt.tight_layout()
    line_chart_path = os.path.join(csv_folder, 'combined_confidence.png')
    plt.savefig(line_chart_path)
    plt.close()
    elements.append(Image(line_chart_path, width=400, height=150))
    elements.append(Spacer(1, 12))

    # New Page for Table
    elements.append(PageBreak())
    elements.append(Paragraph("<i><b>Last 10 Entries</b></i>", styles['Heading3']))
    elements.append(Spacer(1, 8))

    # Table - Last 10 Entries
    table_data = [['Timestamp', 'Emotion', 'Confidence', 'Day']] + combined_df[['Timestamp (IST)', 'Emotion', 'Confidence', 'Day']].tail(10).values.tolist()
    table = Table(table_data, colWidths=[120, 80, 70, 70])
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('GRID', (0, 0), (-1, -1), 0.25, colors.black),
        ('FONTSIZE', (0, 0), (-1, -1), 8),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE')
    ]))
    elements.append(table)

    # Build PDF
    doc.build(elements)
    print(f"✅ Combined report generated: {output_pdf}")

# Example usage
generate_combined_emotion_report("emotion_data", "Combined_Emotion_Report.pdf", employee_name="John Doe", company_name="EmotionTech Solutions")
