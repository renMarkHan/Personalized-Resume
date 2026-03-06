# Interactive Resume Streamlit App

This repository contains a Streamlit application that serves as a personalized, interactive resume for **Yuhan Ren**. It demonstrates several Streamlit features:

- ✅ Personal resume content pulled from an existing PDF
- ✅ Interactive widgets (checkboxes, slider, selectbox) that affect page content
- ✅ A table displaying skills, education, and experience
- ✅ A bar chart visualizing skill proficiencies with Altair

## Running locally

1. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```
2. Launch the app:
   ```bash
   streamlit run app.py
   ```
3. Open the provided localhost URL in your browser.

## Deploying to Streamlit Community Cloud

1. Push this repository to GitHub, making sure that `app.py` and `requirements.txt` are at the root.
2. Go to [Streamlit Community Cloud](https://streamlit.io/cloud) and sign in with your GitHub account.
3. Create a new app and select the GitHub repository and the branch containing `app.py`.
4. Set the main file path to `app.py` (it may auto-detect it).
5. Click **Deploy**. The app will build and launch; share the URL once it's live.

> 💡 Once deployed, any updates pushed to the branch will automatically trigger a rebuild.

## Customization

Feel free to modify the contents of `app.py` to update personal details, add more experiences, or change the visualizations. You can also adapt the interactive widgets to suit other filtering or display logic.
