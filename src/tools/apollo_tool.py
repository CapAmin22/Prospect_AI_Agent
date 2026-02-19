import httpx
from config.settings import settings

async def search_people(query, job_titles):
    """
    Search for people on Apollo.io.
    """
    url = "https://api.apollo.io/v1/mixed_people/search"
    headers = {
        "Cache-Control": "no-cache",
        "Content-Type": "application/json",
        "X-Api-Key": settings.APOLLO_API_KEY
    }
    data = {
        "q_organization_domains": query,
        "person_titles": job_titles
    }
    
    async with httpx.AsyncClient() as client:
        response = await client.post(url, headers=headers, json=data)
        response.raise_for_status()
        return response.json()
