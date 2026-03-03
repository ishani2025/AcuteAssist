import re

INPUT_FILE = "data/stroke.txt" #oour raw source file
OUTPUT_FILE = "data/stroke_india.txt"


def clean_text(text):
    text = re.sub(r'\ ', '', text)
    text = re.sub(r'\n+', '\n', text)
    return text.strip()
def get_semantic_header(text):
    """Assigns a Markdown header based on content to improve RAG 'findability'."""
    text = text.lower()
    if "thrombolysis" in text or "rtpa" in text or "alteplase" in text:
        return "## TREATMENT: Intravenous Thrombolysis (IV tPA)"
    if "thrombectomy" in text or "catheter" in text:
        return "## TREATMENT: Mechanical Thrombectomy"
    if "fast" in text or "symptom" in text or "onset" in text:
        return "## DIAGNOSIS: Acute Symptoms & FAST Protocol"
    if "risk factor" in text or "hypertension" in text or "diabetes" in text:
        return "## PREVENTION: Risk Factors & Lifestyle"
    if "physiotherapy" in text or "rehabilitation" in text:
        return "## RECOVERY: Physiotherapy & Rehabilitation"
    if "secondary prevention" in text or "statins" in text:
        return "## PREVENTION: Secondary Stroke Prevention"
    return "## CLINICAL CONTEXT: General Stroke Information"
def get_targeted_steps(text):
    """Returns ONLY context-specific steps to avoid redundant noise."""
    text = text.lower()  
    if "thrombolysis" in text:
        return [
            "Verify symptom onset is within 4.5 hours.",
            "Confirm BP is below 185/110 mmHg.",
            "Rule out intracranial hemorrhage via CT scan.",
            "Check for recent surgery or bleeding contraindications."
        ]
    elif "thrombectomy" in text:
        return[
            "Confirm large vessel occlusion via Angiography.",
            "Assess eligibility within the 6-24 hour window.",
            "Prepare for femoral or radial artery catheter access.",
            "Monitor neurological status post-recanalization."
        ]
    elif "physiotherapy" in text:
        return[
            "Assess motor deficits and limb strength.",
            "Implement passive range-of-motion exercises.",
            "Evaluate swallowing safety (dysphagia screen).",
            "Coordinate with speech and occupational therapists."
        ]
    elif "risk" in text or "prevention" in text:
        return [
            "Target BP < 140/90 mmHg for secondary prevention.",
            "Initiate high-dose statin therapy (LDL goal < 70 mg/dL).",
            "Screen for Atrial Fibrillation via ECG/Holter.",
            "Counsel on smoking cessation and salt reduction."
        ]
    else:
        return [
            "Perform immediate FAST neurological assessment.",
            "Establish 'Time Last Seen Normal'.",
            "Check blood glucose to rule out hypoglycemia.",
            "Maintain oxygen saturation > 94%."
        ]
def create_semantic_chunks(text):
    raw_paragraphs = text.split('\n\n')
    optimized_chunks = []

    for para in raw_paragraphs:
        if len(para) < 100: continue
        header = get_semantic_header(para)
        steps = get_targeted_steps(para)
        
        chunk = f"{header}\n\n"
        chunk += f"**Context:** {para.strip()}\n\n"
        chunk += "**Critical Doctor Actions:**\n"
        for i, step in enumerate(steps, 1):
            chunk += f"{i}. {step}\n"
        
        optimized_chunks.append(chunk)
        
    return optimized_chunks

def main():
    try:
        with open(INPUT_FILE, "r", encoding="utf-8") as f:
            content = f.read()

        clean_content = clean_text(content)
        final_chunks = create_semantic_chunks(clean_content)

        with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
            for i, chunk in enumerate(final_chunks):
                f.write(f"--- CHUNK ID: {i+1} ---\n")
                f.write(chunk)
                f.write("\n\n")

        print(f"Success! Created {len(final_chunks)} semantic chunks in {OUTPUT_FILE}")
        print("Tip: Your RAG will now find 'Treatment' vs 'Prevention' much faster.")

    except FileNotFoundError:
        print(f"Error: Could not find {INPUT_FILE}. Please check the file path.")

if __name__ == "__main__":
    main()