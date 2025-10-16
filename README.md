Phurhard HNG - Django REST API Project

🚀 Project Overview

This is a simple Django REST Framework API created for the Phurhard HNG Task. The API exposes a single endpoint that returns your profile information, the current timestamp, and a random cat fact fetched from an external API.

📂 Project Structure

phurhard_HNG/
│
├── phurhard_proj/              # Main Django project directory
│   ├── settings.py            
│   ├── urls.py                 
│
├── myprofile_api/              # Application directory
│   ├── views.py               
│   ├── urls.py                 
│
├── manage.py                   # Django management script
├── requirements.txt            # Python dependencies
└── README.md                   

⚙️ Setup Instructions

1. Clone the Repository

git clone https://github.com/GOODNEWS221/phurhard_HNG.git
cd phurhard_HNG

2. Created a Virtual Environment

python -m venv venv
venv\Scripts\activate   

3. Install Dependencies

pip install -r requirements.txt

4. Set Environment Variables

Created a .env file in the root directory and add the following:



5. Apply Migrations

python manage.py makemigrations
python manage.py migrate

6. Run the Server

python manage.py runserver

The project will run on:
👉 http://127.0.0.1:8000

🧠 API Endpoint

GET /api/me/

Description: Returns a JSON object with your personal details, timestamp, and a random cat fact.

Example Response

{
  "status": "success",
  "user": {
    "email": "goodnewsatekha@gmail.com",
    "name": "Goodnews Atekha",
    "stack": "Python/Django REST Framework"
  },
  "timestamp": "2025-10-15T18:30:00Z",
  "fact": "Cats sleep for 70% of their lives."
}

🧰 Features

Fetches a random cat fact from an external API.

Includes rate limiting to prevent abuse (5 requests per minute).

Handles API and network errors gracefully.

Includes proper CORS configuration.

Uses environment variables for sensitive settings.


🐾 Error Handling

Network errors and timeouts are safely handled.

Appropriate HTTP status codes are used.


🧪 Testing the Endpoint

I tested the API endpoint locally using:

browser: http://127.0.0.1:8000/api/me/



🧱 Dependencies

Django

djangorestframework

python-decouple

django-cors-headers

requests

Install all with:

pip install -r requirements.txt





