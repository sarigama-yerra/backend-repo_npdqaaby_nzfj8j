"""
Database Schemas

Define your MongoDB collection schemas here using Pydantic models.
These schemas are used for data validation in your application.

Each Pydantic model represents a collection in your database.
Model name is converted to lowercase for the collection name:
- User -> "user" collection
- Product -> "product" collection
- BlogPost -> "blogs" collection
"""

from pydantic import BaseModel, Field, EmailStr
from typing import Optional, Literal

# Example schemas (replace with your own):

class User(BaseModel):
    """
    Users collection schema
    Collection name: "user" (lowercase of class name)
    """
    name: str = Field(..., description="Full name")
    email: str = Field(..., description="Email address")
    address: str = Field(..., description="Address")
    age: Optional[int] = Field(None, ge=0, le=120, description="Age in years")
    is_active: bool = Field(True, description="Whether user is active")

class Product(BaseModel):
    """
    Products collection schema
    Collection name: "product" (lowercase of class name)
    """
    title: str = Field(..., description="Product title")
    description: Optional[str] = Field(None, description="Product description")
    price: float = Field(..., ge=0, description="Price in dollars")
    category: str = Field(..., description="Product category")
    in_stock: bool = Field(True, description="Whether product is in stock")

# Add your own schemas here:
# --------------------------------------------------

class DemoRequest(BaseModel):
    """
    Demo requests from the landing page
    Collection name: "demorequest"
    """
    full_name: str = Field(..., min_length=2, description="Visitor's full name")
    work_email: EmailStr = Field(..., description="Work email address")
    company_name: str = Field(..., min_length=2, description="Company or organization")
    role_title: Optional[str] = Field(None, description="Role or title")
    industry: Literal['Banking','Law Firm','Fintech','Corporate','Other'] = Field(..., description="Industry selection")
    primary_use_case: Optional[str] = Field(None, max_length=1000, description="Short description of use case")
    preferred_time_zone: Optional[str] = Field(None, description="Time zone preference")
    message: Optional[str] = Field(None, max_length=2000, description="Additional notes")
    consent: bool = Field(..., description="Consent to be contacted")

    class Config:
        json_schema_extra = {
            "example": {
                "full_name": "Alex Morgan",
                "work_email": "alex@bank.com",
                "company_name": "Global Bank",
                "role_title": "Product Manager",
                "industry": "Banking",
                "primary_use_case": "Verifiable Proof-of-Funds for onboarding",
                "preferred_time_zone": "UTC-5 (EST)",
                "message": "Looking to pilot with our private banking team.",
                "consent": True
            }
        }

# Note: The Flames database viewer will automatically:
# 1. Read these schemas from GET /schema endpoint
# 2. Use them for document validation when creating/editing
# 3. Handle all database operations (CRUD) directly
# 4. You don't need to create any database endpoints!
