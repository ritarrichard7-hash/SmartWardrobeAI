👗 SmartWardrobe AI: Context-Aware Modest Fashion Orchestrator
📝 Project Overview
SmartWardrobe AI is a highly technical, hyper-personalized fashion curation platform engineered to solve a distinct market need: delivering elegant, tailored outfit coordination that adheres strictly to custom modesty parameters.

Unlike basic, low-level chat implementations that rely on unverified model assumptions, this platform utilizes a Multi-Agent Orchestration Loop integrated with a dedicated Model Context Protocol (MCP) server. It dynamically evaluates local environmental factors (real-time weather indexes) and inventory availability while enforcing absolute design boundaries.

🏗️ Technical Architecture & Data Flow
The application divides cognitive responsibilities across specialized agent frameworks to maximize evaluation reliability and security bounds.

[ User Request: Input City & Style ]
                        │
                        ▼
         ┌────────────────────────────┐
         │   Supervisor Router Agent  │
         │       (gpt-4o-mini)        │
         └──────────────┬─────────────┘
                        │
             Orchestrates Execution
                        │
                        ▼
         ┌────────────────────────────┐
         │ Managed MCPTool Objects Layer│ ◄── [Injects Secure OAuth Headers]
         └──────────────┬─────────────┘
                        │
           Fetches External Context
                        │
                        ▼
         ┌────────────────────────────┐
         │   Remote FastMCP Server    │
         └──────────┬──────────┬──────┘
                    │          │
         ┌──────────┴───┐  ┌───┴──────────┐
         │  Weather API │  │  Inventory   │
         │  (Live Context) │  │ (Blob Store) │
         └──────────────┘  └──────────────┘
                        │
          Payload Returned to Supervisor
                        │
                        ▼
         ┌────────────────────────────┐
         │ Compliance & Safety Agent  │ ◄── [Enforces Modesty Guardrails]
         └────────────────────────────┘
                        │
            Strict Verification Check
                        │
                        ▼
       [ Final Verified Recommendation Output ]

1. The Context Layer (Module 1 Grounding)
The Problem: Base language models hallucinate fashion inventories and regional climate profiles.

The Solution: The system uses a strict Grounding Contract inside the core system prompt instructions, forcing the execution runtime to discard generic baseline knowledge and rely completely on verified tool context.

2. The Dynamic Discovery Layer (Module 2 MCP Core)
The Problem: Hardcoding API connections creates a brittle codebase that breaks when databases change layout schemas.

The Solution: A standalone FastMCP Server exposes backend utilities dynamically. By reading standard Python type hints and function docstrings at runtime, the server generates clean, structural JSON capability schemas over standard transport channels automatically.

3. The Enterprise Orchestration Layer (Module 3 Managed Tools)
The Problem: Managing raw network requests and passing API keys insecurely inside prompt code poses a massive security risk.

The Solution: The architecture deploys the managed Azure AI MCPTool object model. It utilizes update_headers() for secure credential management and binds the agent to restricted endpoint permissions using the allowed_tools parameter array.

🛡️ Responsible AI & Compliance Guardrails
To ensure user alignment, the system implements a two-stage mitigation safety matrix:

Programmatic Attribute Scraping: The compliance evaluation agent scans inventory item listings for strict forbidden tokens (e.g., sleeveless, cropped, deep neckline).

Human-in-the-Loop Safe States (require_approval="always"): If a borderline design attribute profile is flagged, the runtime environment generates an mcp_approval_request, completely freezing execution until an administrator pushes an authorized mcp_approval_response to either clear or reject the garment.

🚀 How to Run the Implementation Locally
1. Install Dependencies
pip install mcp azure-ai-projects python-dotenv asyncio
2. Configure Environment Properties
Create a .env file in your root workspace path:
AZURE_PROJECT_CONNECTION_STRING="your-project-endpoint-connection-string"
LOG_LEVEL="DEBUG"
3. Run the System Loop
python main_orchestrator.py
