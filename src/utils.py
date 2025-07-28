# src/utils.py
from datetime import datetime
import json

def load_configuration(path):
    with open(path) as f:
        return json.load(f)

def create_output_json(config_data, sections, subsections, output_path):
    output = {
        "metadata": {
            "input_documents": [doc['filename'] for doc in config_data['documents']],
            "persona": config_data['persona']['role'],
            "job_to_be_done": config_data['job_to_be_done']['task'],
            "processing_timestamp": datetime.now().isoformat()
        },
        "extracted_sections": sections,
        "subsection_analysis": subsections
    }
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(output, f, indent=4, ensure_ascii=False)