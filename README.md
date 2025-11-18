# 🚀 WhatsApp Product Review Collector

Full-stack application for collecting product reviews over WhatsApp.

- Backend: **FastAPI (Python)**
- Frontend: **React (JavaScript)**
- Database: **PostgreSQL**
- Integration: **WhatsApp (Twilio Sandbox)**

---

## 🔁 Flow Overview

1. User sends a WhatsApp message to the Twilio sandbox number.
2. Twilio forwards the message to the backend `/whatsapp-webhook`.
3. Backend runs a small conversation flow to collect:
   - Product name  
   - User name  
   - Product review
4. The review is stored in a Postgres table with:
   - id  
   - contact_number  
   - user_name  
   - product_name  
   - product_review  
   - created_at
5. Frontend calls `GET /api/reviews` and displays all reviews in a table.

---

## 📂 Project Structure

```text
Backend/
    main.py             # FastAPI app + Twilio webhook + /api/reviews
    database.py         # SQLAlchemy engine & session
    models.py           # Review model / table
    schemas.py          # Pydantic response model
    requirements.txt    # Backend dependencies

frontend/
    App.js              # Root React component
    api.js              # Function to call /api/reviews
    ReviewList.js       # Table listing all reviews
