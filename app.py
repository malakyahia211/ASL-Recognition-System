import streamlit as st
from PIL import Image

from backend import ASLPredictor

st.set_page_config(
    page_title="ASL | Sign Recognition",
    page_icon="🤟",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.markdown("""
<style>

html {
    scroll-behavior: smooth;
}

.stApp {
    background:
        radial-gradient(circle at 50% 0%,
        rgba(116, 91, 153, 0.12),
        transparent 32%),
        #080D18;
    color: #F3F0F7;
}

.block-container {
    max-width: 1180px;
    padding-top: 0.35rem;
    padding-bottom: 0.7rem;
}

[data-testid="stDecoration"] {
    display: none;
}

[data-testid="stHeader"] {
    display: none;
}

/* ================= NAVBAR ================= */

.navbar {
    width: 100%;
    height: 48px;
    display: flex;
    align-items: center;
    justify-content: space-between;
    margin-bottom: 8px;
}

.nav-brand {
    display: flex;
    align-items: center;
    gap: 8px;
}

.nav-icon {
    font-size: 23px;
    line-height: 1;
}

.nav-logo {
    font-size: 25px;
    font-weight: 800;
    letter-spacing: 4px;
    color: #D5C7E8;
}

.nav-links {
    display: flex;
    align-items: center;
    gap: 30px;
}

.nav-link {
    color: #A9A1B5;
    text-decoration: none;
    font-size: 16px;
    font-weight: 600;
    transition: color 0.2s ease;
}

.nav-link:hover {
    color: #D7C8EA;
}

/* ================= HERO ================= */

.hero-small {
    text-align: center;
    font-size: 13px;
    letter-spacing: 4px;
    color: #8D7BA9;
    margin-top: 9px;
}

.hero-title {
    text-align: center;
    font-size: 72px;
    font-weight: 800;
    letter-spacing: 16px;
    color: #F3F0F7;
    margin-top: 3px;
    margin-bottom: 0;
}

.hero-description {
    text-align: center;
    color: #7D889B;
    font-size: 14px;
    margin-top: 5px;
}

.hero-accent {
    width: 55px;
    height: 2px;
    background: #8D78A8;
    margin: 18px auto 30px auto;
    border-radius: 10px;
}

/* ================= SECTION TITLES ================= */

.section-title {
    font-size: 19px;
    font-weight: 700;
    color: #E9E3F0;
    margin-bottom: 4px;
}

.section-subtitle {
    color: #737F93;
    font-size: 12px;
    margin-bottom: 18px;
}

/* ================= RADIO ================= */

div[role="radiogroup"] {
    gap: 10px;
}

div[role="radiogroup"] label {
    color: #C3BECA !important;
}

/* ================= UPLOADER ================= */

[data-testid="stFileUploader"] {
    background: #0E1625;
    border: 1px solid #202C41;
    border-radius: 9px;
}

[data-testid="stFileUploader"] section {
    background: transparent;
}

/* ================= CAMERA ================= */

[data-testid="stCameraInput"] {
    background: #0E1625;
    border: 1px solid #202C41;
    border-radius: 9px;
}

/* ================= MAIN BUTTON ================= */

div.stButton > button {
    width: 100%;
    height: 45px;
    border: none;
    border-radius: 8px;
    background: #766391;
    color: #FFFFFF;
    font-size: 14px;
    font-weight: 700;
    transition: all 0.2s ease;
}

div.stButton > button:hover {
    background: #8774A4;
    color: #FFFFFF;
}

/* ================= IMAGE ================= */

[data-testid="stImage"] img {
    border-radius: 8px;
}

/* ================= PREDICTION ================= */

.prediction-label {
    text-align: center;
    color: #737F93;
    font-size: 12px;
    letter-spacing: 3px;
    margin-top: 28px;
}

.prediction-letter {
    text-align: center;
    font-size: 76px;
    font-weight: 800;
    color: #D7C8EA;
    line-height: 1.1;
    margin-top: 2px;
}

.prediction-confidence {
    text-align: center;
    color: #929DB0;
    font-size: 14px;
    margin-bottom: 24px;
}

/* ================= DIVIDER ================= */

hr {
    border-color: #1C2738;
    margin-top: 12px;
    margin-bottom: 12px;
}

/* ================= ABOUT ================= */

.about-section {
    text-align: center;
    margin-top: 8px;
    margin-bottom: 8px;
}

.about-title {
    color: #D3C5E6;
    font-size: 18px;
    font-weight: 700;
    margin-bottom: 4px;
}

.about-text {
    color: #737F93;
    font-size: 13px;
}

/* ================= FOOTER ================= */

.footer {
    width: 100%;
    text-align: center;
    padding: 8px 0;
}

.footer-title {
    color: #D3C5E6;
    font-size: 16px;
    font-weight: 600;
}

.footer-copy {
    color: #8994A7;
    font-size: 16px;
    font-weight: 600;
    margin-top: 8px;
}

</style>
""", unsafe_allow_html=True)


@st.cache_resource
def get_predictor():
    return ASLPredictor("asl_model.keras")


predictor = get_predictor()


# ================= NAVBAR =================

st.html("""
<div class="navbar">

    <div class="nav-brand">
        <span class="nav-icon">🤟</span>
        <span class="nav-logo">ASL</span>
    </div>

    <div class="nav-links">
        <a href="#home" class="nav-link">Home</a>
        <a href="#recognition" class="nav-link">Recognition</a>
        <a href="#about" class="nav-link">About</a>
    </div>

</div>
""")


# ================= HOME =================

st.html("""
<div id="home"></div>
""")

st.markdown(
    '<div class="hero-small">AMERICAN SIGN LANGUAGE</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="hero-title">ASL</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="hero-description">'
    'Recognize hand gestures using deep learning.'
    '</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="hero-accent"></div>',
    unsafe_allow_html=True
)


# ================= RECOGNITION =================

st.html("""
<div id="recognition"></div>
""")

input_col, output_col = st.columns(
    [1, 1],
    gap="large"
)

selected_image = None


with input_col:

    st.markdown(
        '<div class="section-title">Input Image</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="section-subtitle">'
        'Choose how you want to provide the sign.'
        '</div>',
        unsafe_allow_html=True
    )

    input_method = st.radio(
        "Input method",
        ["Upload Image", "Camera Shot"],
        horizontal=True,
        label_visibility="collapsed"
    )

    if input_method == "Upload Image":

        uploaded_file = st.file_uploader(
            "Choose an ASL image...",
            type=["jpg", "jpeg", "png"]
        )

        if uploaded_file is not None:
            selected_image = Image.open(uploaded_file)

    else:

        camera_file = st.camera_input(
            "Capture ASL Gesture"
        )

        if camera_file is not None:
            selected_image = Image.open(camera_file)

    if selected_image is not None:

        st.image(
            selected_image,
            caption="Selected Gesture",
            use_container_width=True
        )


with output_col:

    st.markdown(
        '<div class="section-title">Prediction</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="section-subtitle">'
        'The model will identify the detected sign.'
        '</div>',
        unsafe_allow_html=True
    )

    if predictor.model is None:

        st.error(
            "Model file not found. "
            "Please ensure 'asl_model.keras' exists."
        )

    elif selected_image is not None:

        if st.button("Predict Sign"):

            with st.spinner("Analyzing gesture..."):

                results = predictor.predict(
                    selected_image,
                    top_k=5
                )

            if results:

                top_prediction = results[0]

                st.markdown(
                    '<div class="prediction-label">'
                    'DETECTED SIGN'
                    '</div>',
                    unsafe_allow_html=True
                )

                st.markdown(
                    f'<div class="prediction-letter">'
                    f'{top_prediction["label"]}'
                    f'</div>',
                    unsafe_allow_html=True
                )

                st.markdown(
                    f'<div class="prediction-confidence">'
                    f'{top_prediction["confidence"] * 100:.2f}% confidence'
                    f'</div>',
                    unsafe_allow_html=True
                )

                st.markdown("---")

                st.markdown("**Top Probabilities**")

                for item in results:

                    st.text(
                        f'{item["label"]}: '
                        f'{item["confidence"] * 100:.2f}%'
                    )

                    st.progress(
                        min(
                            max(
                                item["confidence"],
                                0.0
                            ),
                            1.0
                        )
                    )

    else:

        st.info(
            "Upload an image or capture a frame "
            "to view prediction results."
        )


# ================= ABOUT ANCHOR =================

st.html("""
<div id="about"></div>
""")


# ================= FOOTER =================

st.markdown("---")

st.html("""
<div class="footer">

    <div class="footer-title">
        ASL Recognition System — American Sign Language Recognition
    </div>

    <div class="footer-copy">
        © 2026 ASL Recognition System
    </div>

</div>
""")