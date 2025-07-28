# src/main.py (Updated to use a single processing step)
import pprint
import os
from pathlib import Path
# Local module imports for the processing pipeline
from config import INPUT_JSON_PATH, OUTPUT_JSON_PATH, PDF_FOLDER
from utils import load_configuration, create_output_json
from analyzer import analyze_persona_job
from process_pdfs import process_pdfs # We no longer need parser.py
from ranker import rank_sections


def execute_document_analysis():
    """
    Primary function to execute the complete PDF analysis and ranking workflow.
    """
    print("--- Initiating Document Intelligence Pipeline ---")

    # Phase 1: Load configuration data (persona, job, etc.) from the input JSON file
    print(f"Loading configuration from: {INPUT_JSON_PATH}")
    try:
        config_data = load_configuration(INPUT_JSON_PATH)
        user_persona = config_data["persona"]
        user_task = config_data["job_to_be_done"]
        challenge_metadata = config_data["challenge_info"]
        print("✅ Configuration loaded successfully.")
    except FileNotFoundError:
        print(f"❌ ERROR: Configuration file not found at {INPUT_JSON_PATH}. Please ensure the file exists.")
        return
    except KeyError as e:
        print(f"❌ ERROR: Missing required key {e} in {INPUT_JSON_PATH}.")
        return


    # Phase 2: Process all PDFs to extract titles, outlines, and full text in a SINGLE PASS.
    print("\n--- Phase 1: Document Processing (Single Pass) ---")
    processed_document_data = process_pdfs() # This now contains titles, outlines, and parsed_text
    if not processed_document_data:
        print("❌ ERROR: No PDF data was processed. Please check your PDF folder and configuration.")
        return
    print(f"✅ Successfully processed {len(processed_document_data)} documents in a single pass.")


    # Phase 3: Prepare the exact inputs for the analyzer from the processed data.
    # The separate call to parse_documents is now removed.
    print("\n--- Phase 2: Data Preparation for Analysis ---")

    # Create the 'parsed_docs' dictionary in the format the analyzer expects.
    # This uses the 'parsed_text' key from our single-pass result.
    parsed_documents = {filename: data['parsed_text'] for filename, data in processed_document_data.items() if 'parsed_text' in data}

    # The 'all_outlines_data' is the same rich dictionary, as it contains the 'outline' and 'title' for each file.
    document_outlines = processed_document_data
    print("✅ Data prepared for analyzer.")


    # Phase 4: Analyze the documents to find sections relevant to the persona and task.
    print("\n--- Phase 3: Relevance Analysis ---")
    relevant_sections = analyze_persona_job(
        parsed_documents,
        user_persona,
        user_task,
        challenge_metadata,
        document_outlines, # Pass the full structure
        max_results=10
    )
    print(f"✅ Analysis complete. Found {len(relevant_sections)} potentially relevant sections.")


    # Phase 5: Rank the matched sections and generate the final output JSON.
    print("\n--- Phase 4: Section Ranking and Output Generation ---")
    ranked_sections, subsections = rank_sections(relevant_sections, user_persona, user_task)
    create_output_json(config_data, ranked_sections, subsections, OUTPUT_JSON_PATH)
    print(f"✅ Final output generated at: {OUTPUT_JSON_PATH}")
    print("\n--- Document Intelligence Pipeline Completed ---")


if __name__ == "__main__":
    execute_document_analysis()