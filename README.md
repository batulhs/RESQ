# RESQ 🤝

## Women’s Safety & Support Chatbot

RESQ is an AI-powered safety and support system designed to assist users in emergency situations, provide mental health support, and offer access to legal and helpline resources. It includes features like AI chatbot assistance, panic alert system, geolocation-based safety suggestions, and a calming user interface.

---

## 📌 Features

- 🤖 AI-powered chatbot for real-time assistance  
- 🚨 Panic button for emergency alerts  
- 📍 Geolocation-based safe place suggestions  
- 📞 Quick access to helpline numbers  
- 🎧 Alarm/sound feature for emergencies  
- 💬 Mental health and emotional support responses  
- 🔐 Secure login system  
- 🎨 Calm and user-friendly interface  

---

## 🛠️ Tech Stack

- Frontend: HTML, CSS, JavaScript  
- Backend: Python (Flask / FastAPI)  
- AI Integration: OpenAI API  
- Maps Integration: Google Maps API  
- Data Handling: JSON, REST APIs  

---

## 📂 Project Structure

RESQ/
│── static/              # CSS, JS, images  
│── templates/           # HTML files  
│── app.py               # Main backend file  
│── open.env             # Environment variables (NOT pushed to GitHub)  
│── requirements.txt     # Dependencies  
│── .gitignore           # Ignored files  
│── README.md            # Project documentation  

---

## ⚙️ Setup Instructions

### 1. Clone the repository
git clone https://github.com/batulhs/RESQ.git  
cd RESQ  

---

### 2. Create virtual environment
python -m venv venv  
venv\Scripts\activate   # Windows  

---

### 3. Install dependencies
pip install -r requirements.txt  

---

### 4. Add environment variables
Create a file named `.env` or `open.env` and add:

OPENAI_API_KEY=your_api_key_here  

---

### 5. Run the application
python app.py  

---

## 🔐 Security Note

- API keys and sensitive data are stored in environment files.
- These files are ignored using `.gitignore`.
- Never upload secrets to GitHub.

---

## 🎯 Future Improvements

- Mobile app version  
- SMS-based emergency alerts  
- Live location sharing with trusted contacts  
- Multilingual support  
- Advanced AI safety classification  

---

## 👩‍💻 Author

Batul S  
BMS College of Engineering  
MLOps / AI Project  

---

## 📜 License

This project is for academic and learning purposes only.
