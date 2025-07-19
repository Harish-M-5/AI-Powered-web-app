# AI-Powered-web-app


## Overview:
This web application allows users to upload their resume in PDF format and uses Natural Language Processing (NLP) to extract key skills from the content. It then compares those skills with predefined job requirements and displays whether the candidate is selected or not, along with a match percentage.


## Features:
- Upload resume as PDF
- Extract text using pdfplumber
- NLP skill extraction using spaCy
- Match with required job skills
- Calculate match percentage
- Display result (Selected / Not Selected)
- Shows matched skills
- Custom Interview Role, Salary,City and Date suggestions
- Extract candidate name from resume



## Technology Used:

-Frontend-HTML,CSS,JAVASCRIPT

 -Backend-Python,Flask,pdfplumber,spaCy (en_core_web_sm model)


### Deployment (Optional)
Localhost-website link
http://127.0.0.1:8000/


##  Demo:
<img width="1920" height="1080" alt="Screenshot 2025-07-19 095854" src="https://github.com/user-attachments/assets/471ce079-fd5f-4320-9eed-b552c40bfed3" />
<img width="1920" height="1080" alt="Screenshot 2025-07-19 095957" src="https://github.com/user-attachments/assets/5384785e-a68b-4fa6-8cc3-b28d424cd81a" />
<img width="1920" height="1080" alt="Screenshot 2025-07-19 100045" src="https://github.com/user-attachments/assets/89412b20-c70b-44ed-9121-e30018f5cdc6" />
website-http://127.0.0.1:8000/


## Output Images:
<img width="1920" height="1080" alt="Screenshot 2025-07-19 100045" src="https://github.com/user-attachments/assets/676f1b4d-1305-4baf-8857-121e5d307c11" />


## Folder Structur:
AI-Powered-web-app/
├── app.py
├── requirements.txt
├── README.md
├── templates/
│   ├── index.html
│   └── result.html
├── static/
│   ├── style.css
│   └── images/
│       └── screenshot.png
├── resumes/       <-- (optional, for uploaded resumes)
