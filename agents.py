## Importing libraries and files
import os
from dotenv import load_dotenv
import google.generativeai as genai
from crewai import Agent
from tools import  FinancialDocumentTool
load_dotenv()
### Loading LLM

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

class GeminiWrapper:
    def __init__(self, model):
        self.model = model

    def __call__(self, prompt):
        response = self.model.generate_content(prompt)
        return response.text
    
llm = GeminiWrapper(genai.GenerativeModel("gemini-2.0-flash"))
# Creating an Experienced Financial Analyst agent
financial_analyst=Agent(
    role="Senior Financial Analyst",
    goal="Analyze uploaded financial documents and provide insights on key metrics such as revenue, profitability, and growth trends.",
    verbose=True,
    memory=True,
    backstory="Experienced in financial modeling, valuation, and market analysis",
    tools=[FinancialDocumentTool.read_data_tool],
    llm=llm,
    max_iter=1,
    max_rpm=1,
    allow_delegation=True  # Allow delegation to other specialists
)

# Creating a document verifier agent
verifier = Agent(
    role="Financial Document Verifier",
    goal="Verify if the input document is a valid financial report and extract relevant sections.",
    verbose=True,
    memory=True,
    backstory="Background in financial compliance and regulatory document verification.",
    llm=llm,
    max_iter=1,
    max_rpm=1,
    allow_delegation=False
)


investment_advisor = Agent(
    role="Investment Advisor",
    goal="Provide investment recommendations (buy/hold/sell) based on the financial analysis.",
    verbose=True,
    backstory="Professional advisor skilled in asset allocation and portfolio strategies.",
    llm=llm,
    max_iter=1,
    max_rpm=1,
    allow_delegation=False
)


risk_assessor = Agent(
    role="Risk Assessor",
    goal="Identify financial, operational, and market risks, and classify them as low, medium, or high.",
    verbose=True,
    backstory="Specialist in risk management, compliance, and financial stress testing.",
    llm=llm,
    max_iter=1,
    max_rpm=1,
    allow_delegation=False
)
