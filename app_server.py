import asyncio
from mcp.server.fastmcp import FastMCP

# Initialize the Model Context Protocol Server
mcp = FastMCP("SmartWardrobe-Context-Server")

# =====================================================================
# TOOL 1: Live Regional Weather Metrics
# Uses Python type-hints and docstrings to auto-generate JSON schemas
# =====================================================================
@mcp.tool()
async def fetch_weather_metrics(location: str) -> str:
    """
    Retrieves the current real-time environmental climate conditions for a given location.
    Used to dynamically calculate optimal, breathable seasonal fabric selections.
    """
    loc_clean = location.lower()
    
    # Context-aware regional routing
    if "trivandrum" in loc_clean or "thiruvananthapuram" in loc_clean:
        return (
            "Current Climate Focus: 31°C | High Humidity | Passing Monsoon showers. "
            "Fabric recommendation engineering baseline: Pure Linen, Light Breathable Organic Cottons."
        )
    elif "delhi" in loc_clean:
        return (
            "Current Climate Focus: 42°C | Extreme Dry Heatwave. "
            "Fabric recommendation engineering baseline: Ultra-lightweight Khadi, Loose Cottons."
        )
    else:
        return (
            "Current Climate Focus: 24°C | Clear / Mild Conditions. "
            "Fabric recommendation engineering baseline: Universal light layering, standard knits."
        )

# =====================================================================
# TOOL 2: Managed Inventory Catalog Lookup
# Emulates a secure, production-grade warehouse database
# =====================================================================
@mcp.tool()
async def query_inventory_catalog(style_tag: str) -> dict:
    """
    Queries the central warehouse inventory management store based on specific style filters.
    Returns structured clothing item data properties including detailed silhouette attributes.
    """
    tag_clean = style_tag.lower()
    
   # Mocking an expanded enterprise database asset container
    warehouse_database = {
        "casual-chic": {
            "name": "Classic Linen Co-ord Ensemble",
            "attributes": ["three-quarter sleeves", "mandarin premium collar", "tailored formal trousers"],
            "price": "₹3,190",
            "in_stock": True
        },
        "boho-summer": {
            "name": "Ethereal Pastel Maxi Silhouette",
            "attributes": ["long billowy sleeves", "high crew neckline", "breathable layered woven cotton knit"],
            "price": "₹2,499",
            "in_stock": True
        },
        "streetwear-retro": {
            "name": "Oversized Structural Utility Cargo Set",
            "attributes": ["short dropped-shoulder sleeves", "standard crewneck", "heavyweight cotton fabric"],
            "price": "₹4,200",
            "in_stock": True
        },
        "corporate-minimalist": {
            "name": "Power Tailored Blazer & Wide-Leg Trouser Suit",
            "attributes": ["full-length structured sleeves", "high-lapel collar alignment", "premium lightweight wool blend"],
            "price": "₹6,800",
            "in_stock": True
        },
        "evening-gala": {
            "name": "Midnight Velvet Floor-Length Gown",
            "attributes": ["long fitted sleeves", "elegant boat neckline", "structured inner lining"],
            "price": "₹8,500",
            "in_stock": True
        },
        "cricket-activewear": {
            "name": "Premium Team India Supporter Jersey & Track Set",
            "attributes": ["half sleeves", "athletic collar", "moisture-wicking mesh ventilation"],
            "price": "₹1,999",
            "in_stock": True
        },
        "borderline-trend": {
            "name": "Asymmetrical Summer Garden Dress",
            "attributes": ["sleeveless cut", "deep scoop neckline", "lightweight rayon finish"],
            "price": "₹1,850",
            "in_stock": True
        },
        "athleisure-cropped": {
            "name": "Urban Training Boxy Top & Joggers",
            "attributes": ["cropped waistline silhouette", "short sleeves", "flexible tech-fleece"],
            "price": "₹2,900",
            "in_stock": True
        }
    }
    return warehouse_database.get(tag_clean, {"error": f"No inventory assets matching tag '{style_tag}' found."})

if __name__ == "__main__":
    # Launch the FastMCP server instance over standard I/O communication pipes
    mcp.run()