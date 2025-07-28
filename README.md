# 📄 Multi-Collection PDF Analysis (Challenge 1B)
---

## 🎯 Problem Statement: Persona-Driven Document Intelligence


### Challenge Overview
This system acts as an intelligent document analyst, extracting and prioritizing the most relevant sections from a collection of documents based on a specific persona and their job-to-be-done.

### Input Specification
- **Document Collection:** 3-10 related PDFs
- **Persona Definition:** Role description with specific expertise and focus areas
- **Job-to-be-Done:** Concrete task the persona needs to accomplish

The solution must be generic to handle diverse scenarios:
- **Documents:** Any domain (research papers, textbooks, financial reports, news articles, etc.)
- **Personas:** Diverse roles (researcher, student, salesperson, journalist, entrepreneur, etc.)
- **Jobs-to-be-Done:** Persona-specific tasks (literature reviews, exam preparation, financial analysis, etc.)

### Sample Test Cases

#### Test Case 1: Academic Research
- **Documents:** 4 research papers on "Graph Neural Networks for Drug Discovery"
- **Persona:** PhD Researcher in Computational Biology
- **Job:** "Prepare a comprehensive literature review focusing on methodologies, datasets, and performance benchmarks"

#### Test Case 2: Business Analysis
- **Documents:** 3 annual reports from competing tech companies (2022-2024)
- **Persona:** Investment Analyst
- **Job:** "Analyze revenue trends, R&D investments, and market positioning strategies"

#### Test Case 3: Educational Content
- **Documents:** 5 chapters from organic chemistry textbooks
- **Persona:** Undergraduate Chemistry Student
- **Job:** "Identify key concepts and mechanisms for exam preparation on reaction kinetics"

### Required Output Format
The system generates a JSON output containing:

1. **Metadata:**
   - Input documents
   - Persona
   - Job to be done
   - Processing timestamp

2. **Extracted Sections:**
   - Document source
   - Page number
   - Section title
   - Importance rank

3. **Sub-section Analysis:**
   - Document source
   - Refined text
   - Page number constraints

### Technical Constraints
- **Must run on CPU only**
- **Model size ≤ 1GB**
- **Processing time ≤ 60 seconds** for document collection (3-5 documents)
- **No internet access allowed** during execution

---

## 🏗️ Project Structure

```
Semantic-PDF-Analysis-Engine/
├── Collection_1/                    # Travel Planning
│   ├── PDFs/                       # South of France guides
│   ├── challenge1b_input.json      # Input configuration
│   └── challenge1b_output.json     # Analysis results
├── Collection_2/                    # Adobe Acrobat Learning
│   ├── PDFs/                       # Acrobat tutorials
│   ├── challenge1b_input.json      # Input configuration
│   └── challenge1b_output.json     # Analysis results
├── Collection_3/                    # Recipe Collection
│   ├── PDFs/                       # Cooking guides
│   ├── challenge1b_input.json      # Input configuration
│   └── challenge1b_output.json     # Analysis results
├── src/                            # Source code
│   ├── main.py                     # Main execution script
│   ├── analyzer.py                 # PDF analysis logic
│   ├── ranker.py                   # Content ranking
│   ├── process_pdfs.py             # PDF processing utilities
│   ├── config.py                   # Configuration settings
│   └── utils.py                    # Utility functions
├── Dockerfile                      # Container configuration
├── requirements.txt                 # Python dependencies
├── approach_explanation.md         # Methodology explanation
└── README.md                       # This file
```

## 📊 Collections Overview

### Collection 1: Travel Planning
- **Challenge ID:** round_1b_002
- **Persona:** Travel Planner
- **Task:** Plan a 4-day trip for 10 college friends to South of France
- **Documents:** 7 travel guides

### Collection 2: Adobe Acrobat Learning
- **Challenge ID:** round_1b_003
- **Persona:** HR Professional
- **Task:** Create and manage fillable forms for onboarding and compliance
- **Documents:** 15 Acrobat guides

### Collection 3: Recipe Collection
- **Challenge ID:** round_1b_001
- **Persona:** Food Contractor
- **Task:** Prepare vegetarian buffet-style dinner menu for corporate gathering
- **Documents:** 9 cooking guides

## 📋 Input/Output Format

### Input JSON Structure
```json
{
  "challenge_info": {
    "challenge_id": "round_1b_XXX",
    "test_case_name": "specific_test_case"
  },
  "documents": [{"filename": "doc.pdf", "title": "Title"}],
  "persona": {"role": "User Persona"},
  "job_to_be_done": {"task": "Use case description"}
}
```

### Output JSON Structure
```json
{
  "metadata": {
    "input_documents": ["list"],
    "persona": "User Persona",
    "job_to_be_done": "Task description",
    "processing_timestamp": "2024-01-01T00:00:00Z"
  },
  "extracted_sections": [
    {
      "document": "source.pdf",
      "section_title": "Title",
      "importance_rank": 1,
      "page_number": 1
    }
  ],
  "subsection_analysis": [
    {
      "document": "source.pdf",
      "refined_text": "Content",
      "page_number": 1
    }
  ]
}
```

## 🔧 Key Features
- **Persona-based content analysis** - Tailored extraction based on user role
- **Importance ranking** - Prioritized content based on relevance
- **Multi-collection document processing** - Handles diverse document types
- **Structured JSON output** - Consistent metadata and analysis format
- **CPU-optimized processing** - Efficient resource utilization
- **Offline operation** - No internet dependency during execution

---

## 🚀 How to Run with Docker
This project is containerized with Docker for easy and consistent execution.

### ⚙️ Prerequisites
- Docker Desktop must be installed and running.

### 🏗️ Step 1: Build the Docker Image

You can build the Docker image in two ways: from your local files or directly from a GitHub repository.

####  Build from Local Files

Open your terminal (PowerShell, Command Prompt, etc.),  
navigate to the  project directory,  
and run:

```bash
docker build -t challenge1b-solution .
```

#### 



### 🧪 Step 2: Run the Analysis

The command below runs the application.  
The `-v` flag maps your local folder to `/app/data` inside the container.

#### ▶️ Run with Sample Collections

To run analysis on a sample collection like `Collection_3`, run:

```bash
docker run --rm -v "$(pwd)/Collection_3:/app/data" challenge1b-solution
```

To run on `Collection_1` or `Collection_2`, just change the folder name in the command.

> Output: `challenge1b_output.json` will be saved in the same folder you provided.

### 🧾 Run with Your Own Custom Input (For Judges)

Follow these steps to run with a new custom set of documents.

#### 1️⃣ Prepare Your Input Folder

Create a folder (e.g., `testing_1b`) containing:

- A `challenge1b_input.json` file defining persona & task.
- A subfolder named `PDFs/` with all your PDF documents.

**Example Structure:**
```
testing_1b/
├── challenge1b_input.json
└── PDFs/
    ├── doc1.pdf
    └── doc2.pdf
```

#### 2️⃣ Run the Container with Your Folder

Use this command (replace with your folder name):

```bash
docker run --rm -v "$(pwd)/testing_1b:/app/data" challenge1b-solution
```

> The script will generate `challenge1b_output.json` inside your `testing_1b` folder.

---


