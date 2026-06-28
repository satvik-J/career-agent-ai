from pypdf import PdfReader


def load_linkedin_profile(pdf_path: str) -> str:
    reader = PdfReader(pdf_path)
    linkedin_profile = ""

    for page in reader.pages:
        text = page.extract_text()

        if text:
            linkedin_profile += text

    return linkedin_profile


def load_summary(summary_path: str) -> str:
    with open(summary_path, "r", encoding="utf-8") as file:
        career_summary = file.read()

    return career_summary