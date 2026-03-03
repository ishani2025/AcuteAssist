def extract_medical_features(text):

    features = {}

    if "chest pain" in text.lower():
        features["symptom"] = "chest pain"

    if "sweating" in text.lower():
        features["symptom2"] = "sweating"

    if "slurred speech" in text.lower():
        features["symptom"] = "possible stroke"

    if "troponin" in text.lower():
        features["test"] = "troponin present"

    return features