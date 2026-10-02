# ESSA Certificate Sub-Branch Module

This module implements the Workshop Certificate allocation sub-branch for the Electronics Engineering Students Association (ESSA) website, Terna College of Engineering.

## Folder Structure
```text
essa_certificate_module/
├── backend/
│   ├── main.py              # FastAPI application entry point
│   ├── requirements.txt     # Python dependencies
│   ├── routers/
│   │   └── certificates.py  # Certificate generation endpoint
│   ├── utils/
│   │   └── certificate_gen.py # ReportLab PDF generator script
│   └── static/
│       └── images/          # Place terna_logo.jpg and essa_logo.jpg here
└── frontend/
    ├── templates/
    │   └── certificates.html # Student certificates dashboard view
    └── static/
        └── css/
            └── style.css    # Portal stylesheet
```

## Setup & Execution

### 1. Backend Setup
1. Navigate to the `backend/` folder:
   ```bash
   cd backend
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Place your Terna College logo and ESSA logo as `terna_logo.jpg` and `essa_logo.jpg` inside `backend/static/images/`.
4. Run the FastAPI server:
   ```bash
   uvicorn main:app --reload --port 8000
   ```

### 2. Frontend Setup
1. Open `frontend/templates/certificates.html` directly in your browser or serve it via a local static server.
2. The frontend connects to `http://localhost:8000` to fetch and download individual certificates as dynamic PDFs.
