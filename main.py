from recorder import record_audio
from transcriber import transcribe_audio
from clinical_ai import analyze_clinical_text
from soap_formatter import create_soap_notes
from emr_writer import save_to_emr

def run():

    audio = record_audio()

    text = transcribe_audio(audio)

    print("Transcript:", text)

    clinical_data = analyze_clinical_text(text)

    soap_notes = create_soap_notes(clinical_data)

    print(soap_notes)

    save_to_emr("patient_001", soap_notes)


if __name__ == "__main__":
    run()