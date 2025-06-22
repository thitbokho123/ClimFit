import streamlit as st
from services.weather_api import get_weather
from services.dify_api import get_outfit_advice
from image_gen import generate_image  

st.set_page_config(page_title="Weather Outfit Advisor")
st.title("Weather-Based Outfit Advisor")

city   = st.text_input("Enter your city", "New York")
gender = st.selectbox("Gender", ["Male", "Female", "Other"])
age    = st.number_input("Age", 1, 100, 25)
style  = st.text_input("Style (comma-separated)", "Casual, Sporty, Formal")

if city:
    try:
        weather = get_weather(city)
        st.success(f"Weather in {city}: {weather['temp']} °C, {weather['desc']}")
    except Exception as e:
        st.error(e)
        st.stop()

    advice = get_outfit_advice(weather, gender, age, style)
    st.markdown("**Appropriate outfit:**")
    st.write(advice)

    if st.button("Generate outfit image"):
        with st.spinner("Generating…"):
            try:
                img_path = generate_image(advice)  
                st.image(img_path, caption="Suggested outfit")
            except Exception as e:
                st.error(f"❌ {e}")


