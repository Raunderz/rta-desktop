from fastapi import APIRouter

router = APIRouter(prefix="/billing", tags=["billing"])


@router.get("/subscription")
async def get_subscription():
    """Get user subscription details."""
    return {"message": "Subscription endpoint - to be implemented"}


@router.post("/checkout")
async def create_checkout_session():
    """Create a checkout session for premium features."""
    return {"message": "Checkout endpoint - to be implemented"}


@router.post("/webhook")
async def stripe_webhook():
    """Handle Stripe webhook events."""
    return {"message": "Stripe webhook endpoint - to be implemented"}
