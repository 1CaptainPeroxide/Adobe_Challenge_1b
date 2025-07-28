import os
from pathlib import Path

# --- Standard path inside the container ---
# The user/judge will mount their folder (e.g., "Collection_4") to this single location.
DOCKER_DATA_PATH = Path("/app/data")

# --- Logic to handle both Docker and local (VS Code) execution ---
# If the container path exists, use it. This will be TRUE inside Docker.
if DOCKER_DATA_PATH.is_dir():
    print(f"✅ Docker environment detected. Using mounted directory: {DOCKER_DATA_PATH}")
    WORKING_DIR = DOCKER_DATA_PATH
else:
    # If not in Docker, fall back to a local path for testing in VS Code.
    SRC_DIR = Path(__file__).resolve().parent
    BASE_DIR = SRC_DIR.parent
    LOCAL_COLLECTION = "Collection_2" #<-- Change this for local VS code testing
    print(f"⚠️ Docker environment not found. Falling back to local path for '{LOCAL_COLLECTION}'.")
    WORKING_DIR = BASE_DIR / LOCAL_COLLECTION

# --- Set all paths relative to the detected WORKING_DIR ---
# Find the input JSON file automatically
json_files = list(WORKING_DIR.glob('*.json'))
if not json_files:
    raise FileNotFoundError(f"No input JSON file found in '{WORKING_DIR}'")
INPUT_JSON_PATH = WORKING_DIR / "challenge1b_input.json"

# The output is saved in the SAME directory as the input
OUTPUT_JSON_PATH = WORKING_DIR / "challenge1b_output.json"

# The PDFs are in a subfolder named "PDFs" within the input directory
PDF_FOLDER = WORKING_DIR / "PDFs"

print(f"✅ Input path set to: {INPUT_JSON_PATH}")
print(f"✅ PDF path set to: {PDF_FOLDER}")
print(f"✅ Output path set to: {OUTPUT_JSON_PATH}")