# GenAI Healthcare Hackathon Project

A comprehensive AI-powered healthcare application that combines disease diagnosis, medical chat assistance, and intelligent form processing.

## 🏥 Project Overview

This project is a full-stack healthcare application that leverages artificial intelligence to provide:
- **Disease Diagnosis**: AI-powered prediction for asthma, cancer, diabetes, and stroke
- **Medical Chat Assistant**: Intelligent chatbot for healthcare queries
- **Smart Forms**: Dynamic form generation and processing
- **User Management**: Secure authentication and user profiles

## 🚀 Features

### 🔐 Authentication System
- User signup and signin functionality
- Secure authentication with JWT tokens
- User profile management

### 💬 AI Chat Assistant
- Intelligent medical chatbot
- Chat history management
- Real-time conversation capabilities

### 🩺 Disease Diagnosis
- **Asthma Prediction**: AI model trained on medical data
- **Cancer Detection**: Machine learning-based cancer prediction
- **Diabetes Analysis**: Predictive diabetes risk assessment
- **Stroke Risk Assessment**: AI-powered stroke prediction

### 📋 Smart Forms
- Dynamic form generation based on disease type
- Intelligent data collection and validation
- Automated form processing

## 🖼️ Application Screenshots

### Signup Page
<img width="1912" height="926" alt="hack1 1" src="https://github.com/user-attachments/assets/0f8637a7-a625-48d2-8d50-df83258a9f33" />
*User registration interface with form validation*

### Home Page
<img width="1845" height="974" alt="hack2 1" src="https://github.com/user-attachments/assets/ef9fdbd1-a112-4643-a05a-c6a2af5373f4" />

*Main dashboard with navigation and key features*

### Chats Page
![WhatsApp Image 2025-08-22 at 00 16 27_0673e8b4](https://github.com/user-attachments/assets/6ff5de9f-57f0-4b7b-8890-59af0be15f48)

*AI medical chat interface and conversation history*

### Diagnosis Page
<img width="1914" height="920" alt="hack3 1" src="https://github.com/user-attachments/assets/a24e8c8c-ee20-4ba7-a940-394fda869989" />

*Disease prediction and analysis interface*

### Forms Page
<img width="1920" height="935" alt="hack4 1" src="https://github.com/user-attachments/assets/4ec8ff47-0af4-41e8-844f-332f19107524" />
*Dynamic form generation and data collection*

## 🛠️ Technology Stack

### Frontend
- **Next.js 14**: React framework with App Router
- **TypeScript**: Type-safe development
- **CSS Modules**: Scoped styling
- **Context API**: State management

### Backend
- **Django**: Python web framework
- **Django REST Framework**: API development
- **PostgreSQL**: Database (configurable)
- **JWT**: Authentication system

### AI/ML
- **Machine Learning Models**: Disease prediction algorithms
- **LLM Integration**: Medical chatbot capabilities
- **Data Processing**: Medical dataset handling

## 📁 Project Structure

```
gen-ai-hackathon/
├── frontend/                 # Next.js frontend application
│   ├── src/
│   │   ├── app/             # App Router pages
│   │   ├── components/      # Reusable UI components
│   │   ├── contexts/        # React contexts
│   │   ├── hooks/           # Custom React hooks
│   │   └── styles/          # CSS modules
├── backend/                  # Django backend application
│   ├── genaimechbackend/    # Django project
│   ├── genaimech/           # Main Django app
│   └── requirements.txt     # Python dependencies
├── diagnosis/               # Disease prediction notebooks
├── llm/                    # LLM integration files
└── image/                  # Project images and assets
```

## 🚀 Getting Started

### Prerequisites
- Node.js 18+ 
- Python 3.8+
- PostgreSQL (optional, can use SQLite)

### Frontend Setup
```bash
cd frontend
npm install
npm run dev
```

### Backend Setup
```bash
cd backend
pip install -r requirements.txt
cd genaimechbackend
python manage.py migrate
python manage.py runserver
```

## 🔧 Configuration

### Environment Variables
Create `.env` files based on the provided examples:
- `backend/genaimechbackend/env.example`
- Frontend environment variables as needed

### Database Setup
Refer to `backend/genaimechbackend/DATABASE_SETUP.md` for detailed database configuration.

## 📊 AI Models

The project includes pre-trained models for:
- **Asthma Prediction**: Based on medical symptoms and patient data
- **Cancer Detection**: Machine learning model for cancer risk assessment
- **Diabetes Analysis**: Predictive model for diabetes diagnosis
- **Stroke Risk**: AI model for stroke probability calculation

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## 📝 License

This project is part of the GenAI Healthcare Hackathon.

## 👥 Team

- **Frontend Developers**: Next.js, TypeScript, UI/UX
- **Backend Developers**: Django, Python, API Development
- **AI/ML Engineers**: Machine Learning, LLM Integration
- **DevOps**: Deployment, Infrastructure

## 📞 Contact

For questions or support, please reach out to the development team.

---

**Note**: This is a hackathon project. For production use, additional security measures, testing, and compliance requirements should be implemented.
