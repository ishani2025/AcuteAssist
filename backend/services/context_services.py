def build_context(symptoms, history, knowledge):

    context = f"""
Symptoms:
{symptoms}

Patient History:
{history}

Relevant Medical Knowledge:
{knowledge}
"""

    return context