from src.utils.database import init_db
from src.agent import ProspectAgent
import asyncio
import sys

async def main():
    print("Initializing B2B Prospect Intelligence Engine...")
    init_db()
    
    if len(sys.argv) < 2:
        print("Usage: python main.py <company_name>")
        return
        
    company = sys.argv[1]
    agent = ProspectAgent()
    await agent.run_pipeline(company)

if __name__ == "__main__":
    asyncio.run(main())
