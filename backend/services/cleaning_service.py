import re

def clean_text(text):

    text = re.sub(r'\n+', '\n', text)

    text = re.sub(r'\b\d{10}\b', '', text)

    text = re.sub(r'Page \d+', '', text)

    return text.strip()