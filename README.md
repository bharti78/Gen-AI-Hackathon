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
![Signup Page](image/signup-page.png)
*User registration interface with form validation*

### Home Page
![Home Page](image/home-page.png)
*Main dashboard with navigation and key features*

### Chats Page
![Chats Page](image/chats-page.png)
*AI medical chat interface and conversation history*

### Diagnosis Page
![Diagnosis Page](image/diagnosis-page.png)
*Disease prediction and analysis interface*

### Forms Page
![Forms Page](image/forms-page.png)
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
