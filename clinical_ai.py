from openai import OpenAI

client = OpenAI()

def analyze_clinical_text(text):

    prompt = f"""
    Extract medical information from this conversation.

    Return:
    - Chief Complaint
    - Symptoms
    - Possible Diagnosis
    - Suggested Treatment

    Text:
    {text}
    """

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content