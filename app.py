from flask import Flask,render_template_string

app = Flask(__name__)

# --- THE CONTENT (Your Study Material)--- 
STUDY_DATA = { "subject": "ICSE Computer Applications","chapters": ["OOP Concepts","User-Defined Methods","Constructors","Library Classes","Encapsulation","Arrays","String Handling"],"pyqs": [{"year": "2025 Specimen (Must Read!)","link": "https://static.collegedekho.com/media/uploads/2024/09/06/com-app.pdf"},{"year": "2024","link": "https://static.collegedekho.com/media/uploads/2024/09/09/icse-2024-861-cta.pdf"},{"year": "2023","link": "https://www.oswaal360.com/pluginfile.php/10939/mod_folder/content/0/Latest%20Board%20Papers%20Files/CISCE%20Class%2010/ICSE%20X%20Computer%20Paper-2023.pdf"},{"year": "2022 (Sem 1)","link": "https://static.collegedekho.com/media/django-summernote/2021-12-08/644acda1-c3b8-40a6-9d9a-33d0b298f556.pdf"}]}
HTML_TEMPLATE =  ''' 
<!DOCTYPE html>
<html>
<head>
    <title>ICSE Class 10 - Computer Portal</title>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css">
    <style>
        body
{ background-color:#f8f9fa; }
                           .hero
{ background: #004085;color: white; padding: 40px 0; }
                                                    .card {border: none; shadow: 0 4px 8px rgba(0,0,0,0.1); }
    </style>
</head>
<body>
    <div class="hero text-center">
    <h1> ICSE Class 10: Computer Applications</h1>
    <p>Your 2026 Board Exam Reasource Hub</p>
</div>

<div class="container mt-5">

<div class="row">
<div class"col-md-6">
  <div class="card p-4 mb-4">

  <h3>Core Syllabus</h3>
  <ul class="list-group">

{% for chapter in data.chapters %}

<li class="list-group-item"> {{ chapter }}</li>

{% endfor %}
               </ul> 
            </div>
            </div>

            <div class="col-md-6">
            <div class="card p-4">

<h3>Previous Year Papers</h3>
<div class="list-group">

{% for paper in data.pyqs %}

<a href="{{paper.link}}" class="list-group-item list-group-item-action">

ICSE Board Paper - {{ paper.year}}

</a>

{% endfor %}

</div>

<p class="text-muted mt-2 small text-center">*Links can be updated to school server PDFs</p>
                         </div>
                        </div>
                    </div>
                </div>
            </body>
    </html>
                       '''

@app.route('/')
def home():
    return render_template_string(HTML_TEMPLATE,data=STUDY_DATA)

if __name__ =="__main__":
    # '0.0.0.0' makes the server publicly available
    app.run(host='0.0.0.0',port=5000, debug=True)