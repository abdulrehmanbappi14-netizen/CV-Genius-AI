from __future__ import annotations

from pathlib import Path
from xml.sax.saxutils import escape

from reportlab.lib import colors
from reportlab.lib.pagesizes import LETTER
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer, KeepTogether

from cvgenius.models.cv_profile import CVProfile


def export_profile_text(profile: CVProfile, file_path: str | Path) -> None:
    path = Path(file_path)
    preview = profile.render_preview()
    path.write_text(preview, encoding="utf-8")


def export_profile_pdf(profile: CVProfile, file_path: str | Path) -> None:
    path = Path(file_path)
    template_name = (profile.template_name or "classic").lower()
    if template_name not in {"classic", "modern"}:
        template_name = "classic"

    doc = SimpleDocTemplate(
        str(path),
        pagesize=LETTER,
        leftMargin=0.6 * inch,
        rightMargin=0.6 * inch,
        topMargin=0.65 * inch,
        bottomMargin=0.65 * inch,
    )

    styles = getSampleStyleSheet()
    title_style = ParagraphStyle(
        "TitleStyle",
        parent=styles["Title"],
        fontName="Helvetica-Bold",
        fontSize=22,
        leading=26,
        textColor=colors.HexColor("#0f172a"),
        spaceAfter=4,
    )
    subtitle_style = ParagraphStyle(
        "SubtitleStyle",
        parent=styles["Normal"],
        fontName="Helvetica",
        fontSize=10,
        leading=12,
        textColor=colors.HexColor("#475569"),
        spaceAfter=10,
    )
    section_style = ParagraphStyle(
        "SectionStyle",
        parent=styles["Heading2"],
        fontName="Helvetica-Bold",
        fontSize=11,
        leading=13,
        textColor=colors.HexColor("#0f4c81" if template_name == "modern" else "#1f2937"),
        spaceBefore=8,
        spaceAfter=4,
    )
    body_style = ParagraphStyle(
        "BodyStyle",
        parent=styles["Normal"],
        fontName="Helvetica",
        fontSize=10,
        leading=12,
        textColor=colors.black,
        spaceAfter=3,
    )

    def _bullet_lines(lines: list[str]) -> str:
        return "<br/>".join(f"• {escape(line)}" for line in lines if line)

    story = []
    if template_name == "modern":
        story.append(Paragraph(f"<font name='Helvetica-Bold' size=24 color='#0f4c81'>{escape(profile.full_name or 'Unknown')}</font>", title_style))
        story.append(Paragraph(f"<font name='Helvetica' size=11 color='#334155'>{escape(profile.professional_title or 'Professional')}</font>", subtitle_style))
        story.append(Paragraph(
            f"<font name='Helvetica' size=9>{escape(profile.email or '')} | {escape(profile.phone or '')} | {escape(profile.location or '')}</font>",
            subtitle_style,
        ))
        story.append(Spacer(1, 8))
    else:
        story.append(Paragraph(f"<font name='Helvetica-Bold' size=24>{escape(profile.full_name or 'Unknown')}</font>", title_style))
        story.append(Paragraph(f"<font name='Helvetica' size=11>{escape(profile.professional_title or 'Professional')}</font>", subtitle_style))
        story.append(Paragraph(
            f"<font name='Helvetica' size=9>{escape(profile.email or '')} | {escape(profile.phone or '')} | {escape(profile.location or '')}</font>",
            subtitle_style,
        ))
        story.append(Spacer(1, 6))

    story.append(Paragraph("<b>Professional Summary</b>", section_style))
    story.append(Paragraph(escape(profile.summary or "No summary available"), body_style))

    story.append(Paragraph("<b>Skills</b>", section_style))
    story.append(Paragraph(_bullet_lines(profile.skills or ["No skills listed"]), body_style))

    story.append(Paragraph("<b>Languages</b>", section_style))
    story.append(Paragraph(_bullet_lines(profile.languages or ["No languages listed"]), body_style))

    if profile.experiences:
        story.append(Paragraph("<b>Experience</b>", section_style))
        for item in profile.experiences:
            story.append(Paragraph(
                f"<font name='Helvetica-Bold'>{escape(item.role or 'Role')}</font> — {escape(item.company or 'Company')} ({escape(item.years or 'Years')})",
                body_style,
            ))
            if item.details:
                story.append(Paragraph(escape(item.details), body_style))
            story.append(Spacer(1, 4))
    else:
        story.append(Paragraph("<b>Experience</b>", section_style))
        story.append(Paragraph("No experience listed", body_style))

    if profile.education:
        story.append(Paragraph("<b>Education</b>", section_style))
        for item in profile.education:
            story.append(Paragraph(
                f"<font name='Helvetica-Bold'>{escape(item.institution or 'Institution')}</font> — {escape(item.degree or 'Degree')} ({escape(item.years or 'Years')})",
                body_style,
            ))
            if item.details:
                story.append(Paragraph(escape(item.details), body_style))
            story.append(Spacer(1, 4))
    else:
        story.append(Paragraph("<b>Education</b>", section_style))
        story.append(Paragraph("No education listed", body_style))

    if profile.projects:
        story.append(Paragraph("<b>Projects</b>", section_style))
        for item in profile.projects:
            story.append(Paragraph(
                f"<font name='Helvetica-Bold'>{escape(item.name or 'Project')}</font>: {escape(item.description or '')}",
                body_style,
            ))
            if item.technologies:
                story.append(Paragraph(f"Technologies: {escape(', '.join(item.technologies))}", body_style))
            if item.link:
                story.append(Paragraph(f"Link: {escape(item.link)}", body_style))
            story.append(Spacer(1, 4))
    else:
        story.append(Paragraph("<b>Projects</b>", section_style))
        story.append(Paragraph("No projects listed", body_style))

    if profile.certifications:
        story.append(Paragraph("<b>Certifications</b>", section_style))
        for item in profile.certifications:
            story.append(Paragraph(
                f"<font name='Helvetica-Bold'>{escape(item.name or 'Certification')}</font> — {escape(item.issuer or '')} ({escape(item.year or '')})",
                body_style,
            ))
            story.append(Spacer(1, 3))
    else:
        story.append(Paragraph("<b>Certifications</b>", section_style))
        story.append(Paragraph("No certifications listed", body_style))

    story.append(Paragraph("<b>Achievements</b>", section_style))
    story.append(Paragraph(_bullet_lines(profile.achievements or ["No achievements listed"]), body_style))

    if template_name == "modern":
        story.append(Spacer(1, 4))
        story.append(Paragraph("<font name='Helvetica' size=8 color='#64748b'>ATS-friendly, print-ready resume export generated by CV Genius AI.</font>", subtitle_style))

    doc.build(story)
