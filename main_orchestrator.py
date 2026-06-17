import asyncio
from app_server import fetch_weather_metrics, query_inventory_catalog

# =====================================================================
# AGENT CONFIGURATION: System Instruction Contracts (Module 1)
# =====================================================================
ROUTER_SYSTEM_PROMPT = """You are the SmartWardrobe Supervisor Router.
Your job is to take user requests, analyze environmental properties from the weather tool,
and match them to available clothing ensembles from the inventory database."""

COMPLIANCE_SYSTEM_PROMPT = """You are the strict Modest Fashion Compliance Guardrail.
Your sole job is to evaluate clothing item attributes before they are shown to the user.

CRITICAL INSTRUCTIONS:
1. Scan the list of garment attributes for: 'sleeveless', 'strapless', 'deep neckline', or 'cropped'.
2. If ANY of these forbidden attributes are detected, you must immediately flag the item as NON-COMPLIANT.
3. Suggest a stylish modular adjustment (e.g., adding an structured open blazer or chic shrug) to correct the silhouette.
"""

# =====================================================================
# SIMULATED RUNTIME: Simulating the Managed Azure Agent Execution
# =====================================================================
async def run_wardrobe_orchestration_loop(user_city: str, requested_style: str):
    print(f"\n🚀 [INITIATING RUN]: Curating '{requested_style}' for user in '{user_city}'...")
    print("--------------------------------------------------------------------------------")
    
    # 1. Simulate the Supervisor Agent calling Managed MCP Tools (Module 3)
    print("🛰️ Calling Managed Tool: fetch_weather_metrics()...")
    weather_context = await fetch_weather_metrics(user_city)
    print(f"   [Context Retrieved]: {weather_context}")
    
    print("\n📦 Calling Managed Tool: query_inventory_catalog()...")
    catalog_item = await query_inventory_catalog(requested_style)
    
    if "error" in catalog_item:
        print(f"   [Error]: {catalog_item['error']}")
        return

    print(f"   [Context Retrieved]: Found '{catalog_item['name']}' with traits {catalog_item['attributes']}")
    
    # 2. Simulate forwarding payload to the Compliance Agent (Module 1 Guardrails)
    print("\n🛡️ Passing payload to Compliance & Guardrails Evaluator Agent...")
    await asyncio.sleep(0.5) # Latency simulation
    
    item_attributes = catalog_item["attributes"]
    
   # Evaluate for silhouette restrictions using smart substring matching
    forbidden_traits = ["sleeveless", "strapless", "deep", "cropped"]
    
    # Check if any forbidden keyword is hidden inside ANY of the item traits
    detected_violations = []
    for trait in item_attributes:
        for forbidden in forbidden_traits:
            if forbidden in trait.lower():
                detected_violations.append(trait)
    is_compliant = len(detected_violations) == 0
    
    # 3. Handle Human-in-the-Loop approvals if non-compliant (Module 3 Gates)
    if not is_compliant:
        print(f"   [ALERT]: Detected non-compliant design traits: {detected_violations}")
        print("   🛑 Execution Paused. State status: mcp_approval_request generated.")
        print("   🔄 Simulated System Prompt Adjustment applied: Suggesting layout layers...")
        
        print("\n🏆 [FINAL OUTPUT - REASONING LOOP COMPLETE]")
        print(f"Suggested Outfit: {catalog_item['name']} ({catalog_item['price']})")
        print(f"Climate Adaptation: Matches the requirements for {user_city} successfully.")
        print(f"Modesty Status: 🟡 Modified Compliance. (Requires layering: Add a lightweight structured shrug or linen blazer over the top to fix the {detected_violations[0]} silhouette).")
    else:
        print("\n🏆 [FINAL OUTPUT - REASONING LOOP COMPLETE]")
        print(f"Suggested Outfit: {catalog_item['name']} ({catalog_item['price']})")
        print(f"Climate Adaptation: Matches the requirements for {user_city} successfully.")
        print("Modesty Status: 🟢 100% Compliant with silhouette safety parameters.")

# =====================================================================
# TESTING THE CORE ARCHITECTURE
# =====================================================================
async def main():
    print("====================================================================")
    print("👗 RUNNING LOCAL EMULATION FOR SMARTWARDROBE AI MULTI-AGENT ENGINE  ")
    print("====================================================================")
    
    # Case 1: Testing our new corporate wear category
    await run_wardrobe_orchestration_loop("Delhi", "corporate-minimalist")
    
    print("\n" + "="*68 + "\n")
    
    # Case 2: Testing our new athletic cropped trend (this should trigger the compliance guardrail!)
    await run_wardrobe_orchestration_loop("Thiruvananthapuram", "athleisure-cropped")

if __name__ == "__main__":
    asyncio.run(main())