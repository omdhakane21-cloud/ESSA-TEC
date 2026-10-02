import os
from reportlab.lib.pagesizes import landscape, letter
from reportlab.lib import colors
from reportlab.pdfgen import canvas
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle

def generate_certificate(student_name, workshop_name, date_str, output_path):
    doc = SimpleDocTemplate(
        output_path,
        pagesize=landscape(letter),
        rightMargin=40,
        leftMargin=40,
        topMargin=40,
        bottomMargin=40
    )
    
    story = []
    styles = getSampleStyleSheet()
    
    title_style = ParagraphStyle(
        'CertTitle',
        parent=styles['Heading1'],
        fontSize=28,
        alignment=1, # Center
        textColor=colors.HexColor("#1a237e"),
        spaceAfter=15
    )
    
    body_style = ParagraphStyle(
        'CertBody',
        parent=styles['Normal'],
        fontSize=14,
        alignment=1,
        leading=22,
        textColor=colors.HexColor("#333333"),
        spaceAfter=20
    )

    name_style = ParagraphStyle(
        'StudentName',
        parent=styles['Normal'],
        fontSize=24,
        alignment=1,
        textColor=colors.HexColor("#b71c1c"),
        spaceAfter=15
    )

    def draw_decorations(canvas_obj, document):
        canvas_obj.saveState()
        # Outer border
        canvas_obj.setStrokeColor(colors.HexColor("#1a237e"))
        canvas_obj.setLineWidth(3)
        canvas_obj.rect(20, 20, document.pagesize[0] - 40, document.pagesize[1] - 40)
        
        # Inner fine border
        canvas_obj.setStrokeColor(colors.HexColor("#ffb300"))
        canvas_obj.setLineWidth(1)
        canvas_obj.rect(25, 25, document.pagesize[0] - 50, document.pagesize[1] - 50)
        
        # Logos
        terna_logo_path = "backend/static/images/terna_logo.jpg"
        if os.path.exists(terna_logo_path):
            canvas_obj.drawImage(terna_logo_path, 50, document.pagesize[1] - 90, width=70, height=50, preserveAspectRatio=True)
            
        essa_logo_path = "backend/static/images/essa_logo.jpg"
        if os.path.exists(essa_logo_path):
            canvas_obj.drawImage(essa_logo_path, document.pagesize[0] - 120, document.pagesize[1] - 90, width=60, height=60, preserveAspectRatio=True)

        # Signature lines
        canvas_obj.setStrokeColor(colors.HexColor("#555555"))
        canvas_obj.setLineWidth(1)
        
        # Faculty Advisor
        canvas_obj.line(100, 70, 250, 70)
        canvas_obj.drawString(130, 55, "Faculty Advisor")
        
        # ESSA President
        canvas_obj.line(document.pagesize[0] - 250, 70, document.pagesize[0] - 100, 70)
        canvas_obj.drawString(document.pagesize[0] - 210, 55, "ESSA President")
        
        canvas_obj.restoreState()

    story.append(Spacer(1, 20))
    story.append(Paragraph("<b>Terna College of Engineering</b>", ParagraphStyle('SubHeader', parent=styles['Normal'], fontSize=14, alignment=1, textColor=colors.HexColor("#555555"))))
    story.append(Paragraph("<b>Electronics Engineering Students Association (ESSA)</b>", ParagraphStyle('SubHeader2', parent=styles['Normal'], fontSize=12, alignment=1, textColor=colors.HexColor("#777777"), spaceAfter=30)))
    
    story.append(Paragraph("CERTIFICATE OF PARTICIPATION", title_style))
    story.append(Paragraph("This is proudly presented to", body_style))
    
    story.append(Paragraph(f"<b>{student_name}</b>", name_style))
    
    workshop_text = f"for successfully participating and completing the hands-on workshop on <br/><b>{workshop_name}</b> organized by ESSA, held on {date_str}."
    story.append(Paragraph(workshop_text, body_style))

    doc.build(story, onFirstPage=draw_decorations)
