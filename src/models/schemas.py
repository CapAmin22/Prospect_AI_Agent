from pydantic import BaseModel, Field
from typing import List, Optional

class BrandProfile(BaseModel):
    company_name: str
    who_we_are: str
    what_we_do: str
    why_us: str
    how_we_do_it: str
    manually_edited: bool = False

class Competitor(BaseModel):
    name: str
    tier: str  # Direct, Adjacent, Indirect
    description: str

class Prospect(BaseModel):
    first_name: str
    last_name: str
    email: str
    linkedin_url: Optional[str] = None
    job_title: str
    company_name: str
    confidence_score: float
    source: str  # Apollo, Hunter, SMTP

class PitchSequence(BaseModel):
    prospect_id: int
    touch_1: str
    touch_2: str
    touch_3: str
