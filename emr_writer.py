import json

def save_to_emr(patient_id, soap_note):

    record = {
        "patient_id": patient_id,
        "soap_note": soap_note
    }

    with open("emr_records.json", "a") as f:
        json.dump(record, f)
        f.write("\n")

    print("Saved to EMR.")