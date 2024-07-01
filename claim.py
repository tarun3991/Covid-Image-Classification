from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageTemplate, Frame
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch

# Function to get user input with default "No response provided"
def get_user_input(prompt):
    response = input(prompt + " (Provide a full answer or press Enter for default): ")
    return response.strip() if response.strip() else "No response provided"

# Define the sections and questions
sections = {
    "TITLE / ABSTRACT": [
        "Identification as a study of AI methodology, specifying the category of technology used (e.g., deep learning)",
        "Structured summary of study design, methods, results, and conclusions"
    ],
    "INTRODUCTION": [
        "Scientific and clinical background, including the intended use and clinical role of the AI approach",
        "Study objectives and hypotheses"
    ],
    "METHODS": {
        "Study Design": [
            "Prospective or retrospective study",
            "Study goal, such as model creation, exploratory study, feasibility study, non-inferiority trial"
        ],
        "Data": [
            "Data sources",
            "Eligibility criteria: how, where, and when potentially eligible participants or studies were identified (e.g., symptoms, results from previous tests, inclusion in registry, patient-care setting, location, dates)",
            "Data pre-processing steps",
            "Selection of data subsets, if applicable",
            "Definitions of data elements, with references to Common Data Elements",
            "De-identification methods",
            "How missing data were handled"
        ],
        "Ground Truth": [
            "Definition of ground truth reference standard, in sufficient detail to allow replication",
            "Rationale for choosing the reference standard (if alternatives exist)",
            "Source of ground-truth annotations; qualifications and preparation of annotators",
            "Annotation tools",
            "Measurement of inter- and intrarater variability; methods to mitigate variability and/or resolve discrepancies"
        ],
        "Data Partitions": [
            "Intended sample size and how it was determined",
            "How data were assigned to partitions; specify proportions",
            "Level at which partitions are disjoint (e.g., image, study, patient, institution)"
        ],
        "Model": [
            "Detailed description of model, including inputs, outputs, all intermediate layers and connections",
            "Software libraries, frameworks, and packages",
            "Initialization of model parameters (e.g., randomization, transfer learning)"
        ],
        "Training": [
            "Details of training approach, including data augmentation, hyperparameters, number of models trained",
            "Method of selecting the final model",
            "Ensembling techniques, if applicable"
        ],
        "Evaluation": [
            "Metrics of model performance",
            "Statistical measures of significance and uncertainty (e.g., confidence intervals)",
            "Robustness or sensitivity analysis",
            "Methods for explainability or interpretability (e.g., saliency maps), and how they were validated",
            "Validation or testing on external data"
        ]
    },
    "RESULTS": {
        "Data": [
            "Flow of participants or cases, using a diagram to indicate inclusion and exclusion",
            "Demographic and clinical characteristics of cases in each partition"
        ],
        "Model performance": [
            "Performance metrics for optimal model(s) on all data partitions",
            "Estimates of diagnostic accuracy and their precision (such as 95% confidence intervals)",
            "Failure analysis of incorrectly classified cases"
        ]
    },
    "DISCUSSION": [
        "Study limitations, including potential bias, statistical uncertainty, and generalizability",
        "Implications for practice, including the intended use and/or clinical role"
    ],
    "OTHER INFORMATION": [
        "Registration number and name of registry",
        "Where the full study protocol can be accessed",
        "Sources of funding and other support; role of funders"
    ]
}

# Get responses from the user
responses = []
question_number = 1
for section, content in sections.items():
    if isinstance(content, dict):
        for subsection, questions in content.items():
            for question in questions:
                response = get_user_input(f"{question_number}. {question}")
                responses.append((question_number, question, response, section, subsection))
                question_number += 1
    else:
        for question in content:
            response = get_user_input(f"{question_number}. {question}")
            responses.append((question_number, question, response, section, ""))
            question_number += 1

# Function to create PDF report
def create_pdf(filename, responses):
    # Prompt user for author name and affiliation
    author_name = get_user_input("Author's Name:")
    affiliation = get_user_input("Affiliation:")

    doc = SimpleDocTemplate(filename, pagesize=letter)

    # Elements to be added to the PDF
    elements = []

    styles = getSampleStyleSheet()
    title_style = ParagraphStyle(name='TitleStyle', fontSize=16, alignment=1, spaceAfter=20)
    section_style = ParagraphStyle(name='SectionStyle', fontSize=11, textColor='#2E4A7D', spaceBefore=10, spaceAfter=10)
    subsection_style = ParagraphStyle(name='SubSectionStyle', fontSize=10, textColor='#6A8DBF', spaceBefore=8, spaceAfter=10)
    normal_style = ParagraphStyle(name='NormalStyle', fontSize=10, leading=12)
    answer_style = ParagraphStyle(name='AnswerStyle', fontSize=10, textColor='#555555', leading=12)
    citation_style = ParagraphStyle(name='CitationStyle', fontSize=8, leading=10, spaceBefore=24, textColor='#000000')
    author_style = ParagraphStyle(name='AuthorStyle', fontSize=10, spaceBefore=24, spaceAfter=24)


    # Title
    title_paragraph = Paragraph("CLAIM Checklist Report", title_style)
    elements.append(title_paragraph)
    
    # Populate elements with content
    current_section = ""
    current_subsection = ""
    for question_number, question, response, section, subsection in responses:
        if section != current_section:
            current_section = section
            section_paragraph = Paragraph(current_section, section_style)
            elements.append(section_paragraph)
            elements.append(Spacer(1, 12))

        if subsection != current_subsection:
            current_subsection = subsection
            if current_subsection:
                subsection_paragraph = Paragraph(current_subsection, subsection_style)
                elements.append(subsection_paragraph)
                elements.append(Spacer(1, 8))

        question_paragraph = Paragraph(f"{question_number}. {question}", normal_style)
        elements.append(question_paragraph)
        elements.append(Spacer(1, 4))

        answer_paragraph = Paragraph(f"Answer: {response}", answer_style)
        elements.append(answer_paragraph)
        elements.append(Spacer(1, 12))

    # Add author name and affiliation
    author_info = f"Author: {author_name}\nAffiliation: {affiliation}"
    author_paragraph = Paragraph(author_info, author_style)
    elements.append(author_paragraph)

    # Add citation
    citation_text = "Mongan J, Moy L, Kahn CE Jr. Checklist for Artificial Intelligence in Medical Imaging (CLAIM): a guide for authors and reviewers. Radiol Artif Intell 2020; 2(2). https://doi.org/10.1148/ryai.2020200029"
    citation_paragraph = Paragraph(citation_text, citation_style)
    elements.append(citation_paragraph)

    # Build the PDF
    doc.build(elements)

# File name for the PDF
filename = "CLAIM_Report.pdf"

# Create the PDF with user responses
create_pdf(filename, responses)

print(f"CLAIM Report saved as {filename}")
