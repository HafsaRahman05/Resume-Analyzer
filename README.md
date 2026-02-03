# Resume Analyzer - AI Resume Scoring & ATS Optimization

🚀 **Resume Analyzer** is an AI-powered platform that analyzes your resume, optimizes it for ATS (Applicant Tracking Systems), scores it based on industry standards, and recommends matching job opportunities.

## Features

✨ **Key Features:**
- 📄 **Resume Analysis** - Extract and analyze resume content
- 📊 **Resume Scoring** - Get instant feedback on your resume quality
- ✅ **ATS Optimization** - Optimize your resume for ATS systems
- 💼 **Job Recommendations** - Get matched with relevant job opportunities
- 🔐 **User Management** - Secure user authentication and profile management

## Tech Stack

**Frontend:**
- HTML5, CSS3, JavaScript
- Chart.js for data visualization

**Backend:**
- Flask (Web Server)
- FastAPI (API Backend)
- MongoDB (Database)
- pdfplumber & python-docx (Document Processing)

**Deployment:**
- Railway.app (Easy deployment)
- Docker Ready

---

## 🛠 Tech Stack

### Frontend
- HTML5  
- CSS3  
- JavaScript (Vanilla JS)  
- Chart.js  
- Font Awesome  

### Backend
- FastAPI (Python)
- Pydantic
- MongoDB
- PyMongo
- pdfplumber
- python-docx
- Requests


## Quick Start

### Local Development

1. **Clone Repository**
```bash
git clone <repository-url>
cd Resume-Analyzer
```

2. **Create Virtual Environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install Dependencies**
```bash
pip install -r requirements.txt
```

4. **Configure Environment**
```bash
cp .env.example .env
# Edit .env with your settings
```

5. **Run Application**

**Option A: Flask Server (Frontend + API Proxy)**
```bash
python app.py
# Visit http://localhost:5000
```

**Option B: FastAPI Backend (Separate)**
```bash
cd app
python -m fastapi run --port 8000
# Or: uvicorn main:app --reload --port 8000
```

## Folder Structure

```
Resume-Analyzer/
├── app.py                  ← Flask entry point
├── requirements.txt        ← Python dependencies
├── .env.example           ← Environment variables template
├── .gitignore             ← Git ignore rules
├── templates/
│   └── index.html         ← Main HTML
├── static/
│   ├── style.css          ← CSS styling
│   └── script.js          ← Frontend JavaScript
├── app/                   ← Backend modules
│   ├── database.py        ← MongoDB connection
│   ├── models/
│   │   └── user.py        ← Data models
│   ├── routes/
│   │   ├── resume.py      ← Resume endpoints
│   │   ├── jobs.py        ← Job endpoints
│   │   └── user.py        ← User endpoints
│   └── services/
│       ├── resume_parser.py    ← Parse resume files
│       ├── resume_scoring.py   ← Score resumes
│       ├── ats_optimizer.py    ← Optimize for ATS
│       └── job_fetcher.py      ← Fetch job listings
└── uploads/               ← Temporary file storage
```

## API Endpoints

### Resume Operations
- `POST /api/resume/upload` - Upload and extract resume text
- `POST /api/resume/score` - Score resume
- `POST /api/resume/optimize` - Optimize for ATS

### Job Operations
- `POST /api/jobs/recommend` - Get job recommendations

### User Operations
- `POST /api/user/register` - Register user

### Health
- `GET /api/health` - Health check

## Railway.app Deployment

### Automatic Deployment (Recommended)

1. **Connect GitHub Repository**
   - Push code to GitHub
   - Go to Railway.app
   - Create new project
   - Select "Deploy from GitHub"

2. **Environment Variables**
   - Add MONGO_URL: `mongodb+srv://user:pass@cluster.mongodb.net/`
   - Add FASTAPI_URL: (if separate backend)
   - Add FLASK_ENV: `production`

3. **Deploy**
   - Railway will automatically detect `requirements.txt`
   - Runs: `gunicorn app:app --bind 0.0.0.0:$PORT`

### Manual Deployment

```bash
# Install Railway CLI
npm install -g @railway/cli

# Login
railway login

# Link project
railway link

# Deploy
railway up
```

## Environment Variables

Create `.env` file:

```env
# Flask Configuration
FLASK_ENV=production
FLASK_APP=app.py
PORT=5000

# FastAPI Backend (if separate)
FASTAPI_URL=http://your-backend.railway.app

# MongoDB
MONGO_URL=mongodb+srv://user:pass@cluster.mongodb.net/resume_analyzer

# Debug
DEBUG=False
```

## Development

### Running Tests
```bash
pytest
```

### Code Formatting
```bash
black .
```

## Database Setup

### MongoDB Atlas (Free Tier)

1. Create account at mongodb.com
2. Create cluster (free tier available)
3. Get connection string
4. Add to `.env` as MONGO_URL

### Local MongoDB

```bash
# Install MongoDB
# Run MongoDB service
mongod
```

## Troubleshooting

### Port Already in Use
```bash
# Change PORT in .env
PORT=8080
```

### Module Import Errors
```bash
# Reinstall dependencies
pip install -r requirements.txt --force-reinstall
```

### PDF/DOCX Processing Issues
```bash
# Ensure dependencies installed
pip install pdfplumber python-docx
```

## Contributing

1. Fork repository
2. Create feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Open Pull Request

## License

This project is licensed under the MIT License - see LICENSE file for details.

## Support

- 📧 Email: support@resumeanalyzer.com
- 🐛 Issues: GitHub Issues
- 💬 Discussions: GitHub Discussions

## Roadmap

- [ ] Machine Learning resume scoring
- [ ] Multi-language support
- [ ] Resume templates
- [ ] Browser extension
- [ ] Mobile app
- [ ] LinkedIn integration

---

**Built with ❤️ using Flask, FastAPI, and MongoDB**


