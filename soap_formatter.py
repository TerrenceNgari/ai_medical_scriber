def create_soap_notes(clinical_data):

    soap = f"""
    SUBJECTIVE:
    {clinical_data}

    OBJECTIVE:
    Physical exam pending.

    ASSESSMENT:
    Possible diagnosis based on symptoms.

    PLAN:
    Medication and follow-up.
    """

    return soap