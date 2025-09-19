## Importing libraries and files
import os
from dotenv import load_dotenv
load_dotenv()
from crewai_tools import PDFSearchTool
## Creating custom pdf reader tool
class FinancialDocumentTool():
    @staticmethod
    def read_data_tool(path='data/TSLA-Q2-2025-Update.pdf'):
        """Tool to read data from a pdf file from a path

        Args:
            path (str, optional): Path of the pdf file. Defaults to 'data/sample.pdf'.

        Returns:
            str: Full Financial Document file
        """
        
        pdf_tool = PDFSearchTool(pdf=path)
        docs = pdf_tool.load()

        full_report = ""
        for data in docs:
            # Clean and format the financial document data
            content = data.page_content
            
            # Remove extra whitespaces and format properly
            while "\n\n" in content:
                content = content.replace("\n\n", "\n")
                
            full_report += content + "\n"
            
        return full_report

## Creating Investment Analysis Tool
class InvestmentTool:
    @staticmethod
    def analyze_investment_tool(financial_document_data):
        # Process and analyze the financial document data
        processed_data = financial_document_data
        
        # Clean up the data format
        i = 0
        while i < len(processed_data):
            if processed_data[i:i+2] == "  ":  # Remove double spaces
                processed_data = processed_data[:i] + processed_data[i+1:]
            else:
                i += 1
                
        insights = []
        text = processed_data.lower()

        if "revenue" in text:
            insights.append("📊 Revenue information found — analyzing trend.")
        if "operating income" in text or "income from operations" in text:
            insights.append("💼 Operating income details detected.")
        if "gross margin" in text or "profitability" in text:
            insights.append("📈 Profitability metrics present.")
        if "cash flow" in text:
            insights.append("💵 Cash flow information found.")
        if "eps" in text or "earnings per share" in text:
            insights.append("📑 EPS details detected.")

        # --- Recommendation logic ---
        recommendation = "HOLD - Company shows mixed financial signals."

        if any(word in text for word in ["growth", "increase", "up", "improvement"]):
            recommendation = "BUY - Growth indicators suggest positive outlook."
        elif any(word in text for word in ["decline", "decreased", "down", "weakness", "loss"]):
            recommendation = "SELL - Financial performance shows consistent decline."
        else:
            recommendation = "HOLD - Insufficient signals for clear action."

        return {
            "insights": insights,
            "recommendation": recommendation
        }

## Creating Risk Assessment Tool
class RiskTool:
    @staticmethod
    def create_risk_assessment_tool(financial_document_data):        
        # processed_data = financial_document_data

        i = 0
        while i < len(processed_data):
            if processed_data[i:i+2] == "  ":  # Remove double spaces
                processed_data = processed_data[:i] + processed_data[i+1:]
            else:
                i += 1

        # --- Risk assessment logic ---
        text = processed_data.lower()
        risks_found = []
        risk_score = 0

        high_risk_keywords = ["loss", "bankruptcy", "debt", "default", "decline", "tariffs", "political uncertainty"]
        medium_risk_keywords = ["competition", "market volatility", "uncertain", "inflation", "regulatory"]
        low_risk_keywords = ["profit", "growth", "cash reserves", "diversification", "liquidity"]

        for word in high_risk_keywords:
            if word in text:
                risk_score += 2
                risks_found.append(f"⚠️ High Risk Indicator: '{word}' found")
        for word in medium_risk_keywords:
            if word in text:
                risk_score += 1
                risks_found.append(f"⚠️ Medium Risk Indicator: '{word}' found")
        for word in low_risk_keywords:
            if word in text:
                risk_score -= 1
                risks_found.append(f"✅ Positive Indicator: '{word}' found")

        if risk_score >= 3:
            level = "HIGH RISK 🚨"
        elif 1 <= risk_score < 3:
            level = "MEDIUM RISK ⚠️"
        else:
            level = "LOW RISK ✅"

        return {
            "overall_risk": level,
            "risk_score": risk_score,
            "indicators": risks_found
        }