from services.pdf_extraction import extract_text_from_pdf
from services.cleaning_service import clean_text
from services.feature_extractor import extract_medical_features

async def process_local_history(pdf_paths):

    records = []

    for path in pdf_paths:

        text = extract_text_from_pdf(path)

        clean = clean_text(text)

        features = extract_medical_features(clean)

        records.append(features)

    return records