from pydantic import BaseModel, Field


class CampaignPerformance(BaseModel):
    client_id: str
    impressions: int = Field(ge=0)
    clicks: int = Field(ge=0)
    donations: int = Field(ge=0)
    revenue: float = Field(ge=0)


class DonorRetention(BaseModel):
    client_id: str
    retention_rate: float = Field(ge=0.0, le=1.0)


class RagResponse(BaseModel):
    question: str
    answer: str


class ErrorResponse(BaseModel):
    client_id: str
    error: str
