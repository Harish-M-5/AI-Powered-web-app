from flask import Flask, render_template, request
import pdfplumber
import spacy
import os

app = Flask(__name__)

# Load spacy model
nlp = spacy.load("en_core_web_sm")

# Folder to save uploaded resumes
UPLOAD_FOLDER = 'resumes'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Required skills to match
required_skills = ['python', 'html', 'css', 'javascript', 'cloud', 'ai', 'devops', 'mysql']

# Home page route
@app.route('/')
def index():
    return render_template('index.html')

# Resume Upload and Screening route
@app.route('/upload', methods=['POST'])
def upload_resume():
    if 'resume' not in request.files:
        return 'No file part'
    
    file = request.files['resume']
    if file.filename == '':
        return 'No selected file'

    # Save uploaded file
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(filepath)

    # Extract text from PDF
    text = ""
    with pdfplumber.open(filepath) as pdf:
        for page in pdf.pages:
            text += page.extract_text()

    # Initialize Name as None
    name = None

    # Extract Name from resume text
    for line in text.split('\n'):
        if line.lower().startswith("name:"):
            name = line.split(":")[1].strip()
            break

    # If Name not found — Invalid resume
    if not name:
        result = "This Resume is not considered ❌"
        role = "-"
        salary = "-"
        interview_date = "-"
        workplace = "-"
        match_percentage = 0
        matched_keywords = []
    else:
        # NLP Process to find skill matches
        doc = nlp(text.lower())
        matched_keywords = []
        for token in doc:
            if token.text in required_skills and token.text not in matched_keywords:
                matched_keywords.append(token.text)

        match_count = len(matched_keywords)
        total_keywords = len(required_skills)
        match_percentage = int((match_count / total_keywords) * 100)

        # Selection Decision
        if match_count >= 5:
            result = "Selected ✅"
            role = "Junior AI Engineer"
            salary = "₹ 6,00,000 per annum"
            interview_date = "25 July 2025"
            workplace = "Bangalore"
        else:
            result = "Not Selected ❌"
            role = "-"
            salary = "-"
            interview_date = "-"
            workplace = "-"

    # Send result to result.html template
    return render_template(
        'result.html',
        name=name if name else "Not Mentioned",
        result=result,
        matched=matched_keywords,
        percentage=match_percentage,
        role=role,
        salary=salary,
        interview_date=interview_date,
        workplace=workplace
    )

# Run server
if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8000)