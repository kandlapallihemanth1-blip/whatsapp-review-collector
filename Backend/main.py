from fastapi import FastAPI, Request, Depends
from fastapi.responses import PlainTextResponse
from sqlalchemy.orm import Session
from twilio.twiml.messaging_response import MessagingResponse
from database import SessionLocal, engine
from models import Base, Review
from schemas import ReviewSchema

Base.metadata.create_all(bind=engine)
app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

sessions = {}

@app.post("/whatsapp-webhook")
async def whatsapp_webhook(request: Request, db: Session = Depends(get_db)):
    form = await request.form()
    msg = form.get("Body")
    from_number = form.get("From")
    response = MessagingResponse()

    if from_number not in sessions:
        sessions[from_number] = {"step": 1}
        response.message("Which product is this review for?")
        return PlainTextResponse(str(response))

    step = sessions[from_number]["step"]

    if step == 1:
        sessions[from_number]["product"] = msg
        sessions[from_number]["step"] = 2
        response.message("What is your name?")
        return PlainTextResponse(str(response))

    if step == 2:
        sessions[from_number]["name"] = msg
        sessions[from_number]["step"] = 3
        response.message(f"Please send your review for {sessions[from_number]['product']}.")
        return PlainTextResponse(str(response))

    if step == 3:
        review = Review(
            contact_number=from_number,
            user_name=sessions[from_number]["name"],
            product_name=sessions[from_number]["product"],
            product_review=msg
        )
        db.add(review)
        db.commit()
        response.message(f"Thanks {sessions[from_number]['name']} — your review for {sessions[from_number]['product']} has been recorded.")
        del sessions[from_number]
        return PlainTextResponse(str(response))

@app.get("/api/reviews", response_model=list[ReviewSchema])
def get_reviews(db: Session = Depends(get_db)):
    return db.query(Review).all()