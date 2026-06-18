import streamlit as st
import asyncio
from app_server import fetch_weather_metrics
from google import genai
import os
from PIL import Image

# Initialize the Gemini Client
ai_client = genai.Client()

st.set_page_config(page_title="SmartWardrobe AI", page_icon="👗", layout="centered")
st.title("👗 SmartWardrobe AI")
st.subheader("Multimodal Vision Curation & Compliance Platform")

# Added key="location_input" to break the browser cache loop!
user_city = st.text_input("📍 Location for Climate Context:", value="Thiruvananthapuram", key="location_input")

if user_city:
    with st.spinner("Fetching live climate data..."):
        weather_context = asyncio.run(fetch_weather_metrics(user_city))
    st.info(f"☀️ **Local Climate Adaptation:** {weather_context}")

st.markdown("---")
st.markdown("### 📸 Upload a Photo for Smart Styling & Compliance Check")
uploaded_file = st.file_uploader("Snap or drag an outfit photo here...", type=["jpg", "jpeg", "png"])

# Handle the Image Vision Flow if a file exists
if uploaded_file is not None:
    image_asset = Image.open(uploaded_file)
    st.image(image_asset, caption="Uploaded Garment Matrix", use_container_width=True)
    
    if st.button("🚀 Analyze Outfit with Vision AI", use_container_width=True):
        with st.spinner("Vision agent scanning silhouette traits..."):
            vision_prompt = """
Analyze the garment in this image and provide a comprehensive styling profile.
Format your response EXACTLY like this text block:

Description: [1-sentence description of the outfit]
Attributes: [sleeveless, cropped, deep neckline, long sleeve, etc.]

👠 FOOTWEAR MATCHING:
Provide 2 concrete shoe or heel suggestions that complement this specific silhouette, hemline, and fabric. Explain why.

✨ JEWELRY & ACCESSORY LOOKBOOK:
Analyze the neckline and style, then suggest specific jewelry (necklaces, earrings, or bracelets) and bag choices that elevate the look without cluttering it.
"""
            
            try:
                response = ai_client.models.generate_content(
                    model='gemini-2.5-flash',
                    contents=[image_asset, vision_prompt]
                )
                
                analysis_text = response.text
                st.markdown("### 🏆 AI Analysis Results")
                st.write(analysis_text)
                
                # Programmatic Guardrail Policy Check
                analysis_lower = analysis_text.lower()
                forbidden_traits = ["sleeveless", "strapless", "deep neckline", "cropped"]
                detected_violations = [trait for trait in forbidden_traits if trait in analysis_lower]
                
                st.markdown("#### 🛡️ Style Guardrail Status")
                if detected_violations:
                    st.warning(f"🟡 **Modified Compliance Triggered**\n\nOur guardrails flagged a design attribute: *{detected_violations[0]}*.")
                    st.markdown(
                        f"> **Styling Idea:** To adapt this look to your modest style profile, "
                        f"try layering it with a lightweight structured shrug, a chic open abaya, or a linen blazer!"
                    )
                else:
                    st.success("🟢 **100% Compliant**\n\nThis garment silhouette looks completely clear of any flagged cuts!")
                    
            except Exception as e:
                st.error(f"API Connection Error: {e}")
else:
    st.write("💡 *Tip: Drop an outfit photo above to trigger the computer vision compliance engine!*")