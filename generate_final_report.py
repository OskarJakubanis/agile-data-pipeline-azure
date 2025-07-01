from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib import colors
import pandas as pd
import datetime

# Wczytaj dane KPI
kpi_df = pd.read_csv("outputs/kpis.csv")

# Przygotuj dokument PDF
now = datetime.datetime.now().strftime("%Y-%m-%d")
doc = SimpleDocTemplate(f"outputs/final_report_{now}.pdf", pagesize=A4)
styles = getSampleStyleSheet()
elements = []

# Tytuł
title = Paragraph("📊 Final Business Report – E-commerce Pipeline (Azure)", styles['Title'])
elements.append(title)
elements.append(Spacer(1, 20))

# Wstęp
intro = """
This report presents key business insights generated from the full-stack e-commerce pipeline project.
The analysis includes order behavior, customer support load, product return trends, and customer segments.
KPIs were generated using automated scripts and stored in Azure-compatible CSV format.
"""
elements.append(Paragraph(intro, styles['BodyText']))
elements.append(Spacer(1, 20))

# Tabela z KPI
kpi_table_data = [kpi_df.columns.tolist()] + kpi_df.values.tolist()
kpi_table = Table(kpi_table_data)
kpi_table.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor("#003366")),
    ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
    ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
    ('GRID', (0, 0), (-1, -1), 0.5, colors.grey),
    ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.whitesmoke, colors.lightgrey])
]))
elements.append(kpi_table)
elements.append(Spacer(1, 30))

# Podsumowanie
summary = Paragraph("This report concludes the automated Azure-based pipeline simulation. The generated KPIs can support business decisions regarding support staffing, product management, and customer segmentation.", styles['Normal'])
elements.append(summary)

# Zapisz PDF
doc.build(elements)

print("✅ Final report generated successfully.")
