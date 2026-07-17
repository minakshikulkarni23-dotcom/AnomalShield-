from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field
from ml_engine import TransactionGuard

app = FastAPI(title="AnomalShield Middleware API")
guard = TransactionGuard()

class Transaction(BaseModel):
    user_id: int
    amount: float = Field(..., gt=0)
    hour: int = Field(..., ge=0, le=23)
    recipient_id: int
    daily_frequency: int
    phone_number: str

@app.post("/api/v1/transact")
async def process_transaction(tx: Transaction):
    # 1. Map inputs to ML features
    features = [tx.amount, tx.hour, tx.recipient_id, tx.daily_frequency]
    
    # 2. Check model prediction score
    prediction = guard.evaluate_transaction(features)
    
    if prediction == -1:
        # Anomaly detected: Block transaction and simulate MFA trigger
        raise HTTPException(
            status_code=status.HTTP_402_PAYMENT_REQUIRED,
            detail={
                "status": "HOLD_PENDING_MFA",
                "message": f"ALERT: Suspicious transaction flagged! An SMS MFA code has been dispatched to {tx.phone_number}."
            }
        )
        
    return {
        "status": "APPROVED",
        "message": "Transaction cleared safety parameters successfully."
    }