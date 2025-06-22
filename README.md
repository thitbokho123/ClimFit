# ClimFit - Weather-Based Outfit Advisor

**ClimFit** is a smart outfit recommendation app that helps you choose what to wear based on the current weather. Whether it's sunny, rainy, or cold, ClimFit suggests the best clothing style tailored to your gender, age, and weather conditions.

## Features

- 🌍 Get real-time weather based on your city.
- 👕 Suggest outfits based on your style.
- ⚙️ Customize based on gender and age.
- 🤖 AI-generated outfit ideas via Dify.ai integration.
- 📸 Stylish image previews (optional).

## Tech Stack

- **Python**
- **Streamlit** – Web UI
- **Dify API** – For AI outfit advice
- **Weather API** – For real-time weather data
- **Stable Diffusion** - For AI outfit generate

## Demo
![](https://github.com/thitbokho123/ClimFit/blob/main/climfit/demo1)
![](https://github.com/thitbokho123/ClimFit/blob/main/climfit/demo2)
![](https://github.com/thitbokho123/ClimFit/blob/main/climfit/services/Screenshot%202025-06-22%20164623.png)

## Installation

```bash
# Clone the repo
git clone https://github.com/thitbokho123/ClimFit.git
cd ClimFit

# Install dependencies
pip install -r requirements.txt

# Run the app
python -m streamlit run app.py

