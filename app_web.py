import streamlit as st
import asyncio
from app_server import fetch_weather_metrics
from google import genai
import os
from PIL import Image

# Initialize the Gemini Client (It looks for the GEMINI_API_KEY environment variable)
ai_client = genai.Client()

st.set_page_config(page_title="SmartWardrobe AI", page_icon="👗", layout="centered")
st.title("👗 SmartWardrobe AI")
st.subheader("Multimodal Vision Curation & Compliance Platform")

# Get environmental context from your local FastMCP weather tool
user_city = st.text_input("📍 Location for Climate Context:", value="Thiruvananthapuram")

st.markdown("---")
st.markdown("### 📸 Upload a Photo for Smart Styling & Compliance Check")
uploaded_file = st.file_uploader("Snap or drag an outfit photo here...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # 1. Open and display the image file in the UI
    image_asset = Image.open(uploaded_file)
    st.image(image_asset, caption="Uploaded Garment Matrix", use_container_width=True)
    
    if st.button("🚀 Analyze Outfit with Vision AI", use_container_width=True):
        with st.spinner("Vision agent scanning silhouette traits..."):
            
            # Fetch weather context from our local tool server
            weather_context = asyncio.run(fetch_weather_metrics(user_city))
            
            # 2. Craft a structured prompt for the Vision LLM
            vision_prompt = """
            Analyze the garment in this image. Provide a brief 1-sentence description of what it is.
            Then, list its structural attributes clearly. You MUST specifically check for and mention if it has any of these traits:
            'sleeveless', 'strapless', 'deep neckline', or 'cropped'.
            Format your response exactly like this:
            Description: [Your 1-sentence description]
            Attributes: [trait1, trait2, trait3]
            """
            
            try:
                # 3. Fire the multimodal payload to Gemini 2.5 Flash
                response = ai_client.models.generate_content(
                    model='gemini-2.5-flash',
                    contents=[image_asset, vision_prompt]
                )
                
                analysis_text = response.text
                st.markdown("### 🏆 AI Analysis Results")
                st.write(analysis_text)
                
                # Show climate data from our local tool backend
                st.info(f"☀️ **Local Climate Adaptation:** {weather_context}")
                
                # 4. Programmatic Guardrail Policy Check
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
                st.error(f"API Connection Error: Ensure your GEMINI_API_KEY environment variable is set up correctly. Details: {e}")