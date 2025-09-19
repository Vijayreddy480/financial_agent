## Importing libraries and files
from crewai import Task

from agents import financial_analyst, verifier, investment_advisor, risk_assessor
from tools import search_tool, FinancialDocumentTool

## Creating a task to help solve user's query
analyze_financial_document = Task(
    description="Analyze the uploaded financial document and extract key metrics such as revenue, profit, margins, and growth trends. Summarize the financial health of the company.",
    expected_output="A structured financial summary highlighting revenue, profitability, liquidity, and growth. Provide key ratios if available.",
    agent=financial_analyst,
    tools=[FinancialDocumentTool.read_data_tool],
    async_execution=False,
)

## Creating an investment analysis task
investment_analysis = Task(
    description="Based on the financial document, provide investment recommendations (buy, hold, or sell). Consider profitability, growth trends, cash flow, and overall market conditions.",
    expected_output="Clear investment recommendation with supporting reasoning. Highlight both strengths and weaknesses of the company from an investor’s perspective.",
    agent=investment_advisor,
    tools=[FinancialDocumentTool.read_data_tool],
    async_execution=False,
)

## Creating a risk assessment task
risk_assessment = Task(
    description="Evaluate potential risks based on the financial document. Consider financial risks, market volatility, operational challenges, and regulatory risks.",
    expected_output="Risk assessment with classification (low, medium, high). Include identified risk factors and possible mitigation strategies.",
    agent=risk_assessor,
    tools=[FinancialDocumentTool.read_data_tool],
    async_execution=False,
)

    
verification = Task(
    description="Check if the uploaded file is a valid financial report and confirm if it contains key sections such as Income Statement, Balance Sheet, and Cash Flow.",
    expected_output="Validation result stating whether the file is a financial document, with reasoning. Mention missing or incomplete sections if any.",
    agent=verifier,
    tools=[FinancialDocumentTool.read_data_tool],
    async_execution=False
)