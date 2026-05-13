import streamlit as st
from classify import classify_log

# Page title
st.title("Hybrid Log Classification System")

# Source dropdown
source = st.selectbox(
    "Select Source",
    [
        "ModernCRM",
        "BillingSystem",
        "AnalyticsEngine",
        "ModernHR",
        "LegacyCRM"
    ]
)

# Log input
log_message = st.text_area(
    "Enter Log Message"
)

# Button
if st.button("Classify Log"):

    if log_message.strip() == "":
        st.warning("Please enter a log message")

    else:
        # Call your existing function
        prediction = classify_log(source, log_message)

        # Display output
        st.success(f"Predicted Label: {prediction}")


# Enhanced `app.py` for Hybrid Log Classification System


# import streamlit as st
# from classify import classify_log

# # ---------------- PAGE CONFIG ----------------
# st.set_page_config(
#     page_title="Hybrid Log Classification",
#     page_icon="🧠",
#     layout="centered"
# )

# # ---------------- CUSTOM CSS ----------------
# st.markdown(
#     """
#     <style>
#     .stApp {
#         background: linear-gradient(to bottom right, #0f172a, #111827);
#         color: white;
#     }

#     h1 {
#         text-align: center;
#         color: #38bdf8;
#         font-size: 3rem !important;
#         margin-bottom: 10px;
#     }

#     .subtitle {
#         text-align: center;
#         color: #cbd5e1;
#         margin-bottom: 30px;
#         font-size: 18px;
#     }

#     .result-box {
#         background-color: #1e293b;
#         padding: 20px;
#         border-radius: 15px;
#         border: 1px solid #38bdf8;
#         margin-top: 20px;
#         text-align: center;
#         font-size: 22px;
#         font-weight: bold;
#         color: #38bdf8;
#         box-shadow: 0px 0px 15px rgba(56,189,248,0.3);
#     }

#     .method-box {
#         background-color: #111827;
#         padding: 10px;
#         border-radius: 10px;
#         text-align: center;
#         color: #94a3b8;
#         margin-top: 10px;
#     }

#     .stButton>button {
#         width: 100%;
#         background: linear-gradient(to right, #2563eb, #38bdf8);
#         color: white;
#         border-radius: 10px;
#         height: 50px;
#         font-size: 18px;
#         border: none;
#         font-weight: bold;
#     }

#     .stButton>button:hover {
#         background: linear-gradient(to right, #1d4ed8, #0ea5e9);
#         color: white;
#     }
#     </style>
#     """,
#     unsafe_allow_html=True
# )

# # ---------------- HEADER ----------------
# st.markdown("<h1>🧠 Hybrid Log Classification System</h1>", unsafe_allow_html=True)

# st.markdown(
#     "<div class='subtitle'>Regex + BERT + LLM Based Intelligent Log Analyzer</div>",
#     unsafe_allow_html=True
# )

# # ---------------- SIDEBAR ----------------
# st.sidebar.title("📌 About Project")

# st.sidebar.info(
#     """
#     This system classifies enterprise logs using:

#     ✅ Regex Matching
#     ✅ Sentence Transformer + Logistic Regression
#     ✅ LLM-based Classification

#     Built using Streamlit.
#     """
# )

# # ---------------- SOURCE SELECT ----------------
# source = st.selectbox(
#     "Select Source",
#     [
#         "ModernCRM",
#         "BillingSystem",
#         "AnalyticsEngine",
#         "ModernHR",
#         "LegacyCRM"
#     ]
# )

# # ---------------- LOG INPUT ----------------
# log_message = st.text_area(
#     "Enter Log Message",
#     height=180,
#     placeholder="Example: Unauthorized access attempt detected from IP 192.168.1.10"
# )

# # ---------------- CLASSIFICATION ----------------
# if st.button("🚀 Classify Log"):

#     if log_message.strip() == "":
#         st.warning("Please enter a log message.")

#     else:

#         with st.spinner("Analyzing log..."):
#             prediction = classify_log(source, log_message)

#         # ---------------- DISPLAY RESULT ----------------
#         st.markdown(
#             f"""
#             <div class='result-box'>
#                 Predicted Label: {prediction}
#             </div>
#             """,
#             unsafe_allow_html=True
#         )

#         # ---------------- METHOD INFO ----------------
#         if source == "LegacyCRM":
#             method = "LLM-Based Classification"
#         else:
#             method = "Regex / BERT Classification"

#         st.markdown(
#             f"""
#             <div class='method-box'>
#                 Classification Method Used: {method}
#             </div>
#             """,
#             unsafe_allow_html=True
#         )

# # ---------------- FOOTER ----------------
# st.markdown("---")

# st.markdown(
#     "<center>Built with ❤️ using Streamlit and NLP</center>",
#     unsafe_allow_html=True
# )


# Enhanced `app.py` for Hybrid Log Classification System
# Enhanced `app.py` for Hybrid Log Classification System

# import streamlit as st
# from classify import classify_log

# # ---------------- PAGE CONFIG ----------------
# st.set_page_config(
#     page_title="Hybrid Log Classification",
#     page_icon="🧠",
#     layout="centered"
# )

# # ---------------- CUSTOM CSS ----------------
# st.markdown("""
# <style>

# /* Main background */
# .stApp {
#     background: #0f172a;
#     color: white;
# }

# /* Remove top padding */
# .block-container {
#     padding-top: 2rem;
#     padding-bottom: 2rem;
#     max-width: 850px;
# }

# /* Main Card */
# .main-card {
#     background: rgba(30, 41, 59, 0.75);
#     padding: 40px;
#     border-radius: 25px;
#     border: 1px solid rgba(255,255,255,0.08);
#     box-shadow: 0 10px 30px rgba(0,0,0,0.3);
#     backdrop-filter: blur(10px);
# }

# /* Title */
# .main-title {
#     text-align: center;
#     font-size: 3rem;
#     font-weight: 700;
#     color: white;
#     margin-bottom: 10px;
# }

# /* Subtitle */
# .sub-text {
#     text-align: center;
#     color: #94a3b8;
#     font-size: 1rem;
#     margin-bottom: 35px;
# }

# /* Labels */
# label {
#     color: #cbd5e1 !important;
#     font-weight: 500 !important;
# }

# /* Input boxes */
# .stTextArea textarea,
# .stSelectbox div[data-baseweb="select"] {
#     background-color: #1e293b !important;
#     color: white !important;
#     border-radius: 12px !important;
#     border: 1px solid #334155 !important;
# }

# /* Button */
# .stButton > button {
#     width: 100%;
#     height: 52px;
#     border: none;
#     border-radius: 12px;
#     background: linear-gradient(90deg, #06b6d4, #3b82f6);
#     color: white;
#     font-size: 18px;
#     font-weight: 600;
#     transition: 0.3s ease;
# }

# .stButton > button:hover {
#     transform: scale(1.01);
#     background: linear-gradient(90deg, #0891b2, #2563eb);
# }

# /* Result Box */
# .result-box {
#     background: #111827;
#     border: 1px solid #1d4ed8;
#     padding: 20px;
#     border-radius: 15px;
#     margin-top: 25px;
#     text-align: center;
# }

# .result-label {
#     color: #94a3b8;
#     font-size: 16px;
# }

# .result-value {
#     color: #38bdf8;
#     font-size: 28px;
#     font-weight: bold;
#     margin-top: 10px;
# }

# /* Footer */
# .footer {
#     text-align: center;
#     color: #64748b;
#     margin-top: 25px;
#     font-size: 14px;
# }

# </style>
# """, unsafe_allow_html=True)

# # ---------------- MAIN CARD START ----------------
# st.markdown('<div class="main-card">', unsafe_allow_html=True)

# # ---------------- TITLE ----------------
# st.markdown(
#     '<div class="main-title">🧠 Hybrid Log Classification</div>',
#     unsafe_allow_html=True
# )

# st.markdown(
#     '<div class="sub-text">Regex + BERT + LLM Based Intelligent Log Analyzer</div>',
#     unsafe_allow_html=True
# )

# # ---------------- SOURCE ----------------
# source = st.selectbox(
#     "Select Source",
#     [
#         "ModernCRM",
#         "BillingSystem",
#         "AnalyticsEngine",
#         "ModernHR",
#         "LegacyCRM"
#     ]
# )

# # ---------------- LOG INPUT ----------------
# log_message = st.text_area(
#     "Enter Log Message",
#     height=180,
#     placeholder="Example: Unauthorized billing access attempt blocked from IP 192.168.1.45"
# )

# # ---------------- BUTTON ----------------
# if st.button("🚀 Classify Log"):

#     if log_message.strip() == "":
#         st.warning("Please enter a log message.")

#     else:

#         with st.spinner("Analyzing log..."):
#             prediction = classify_log(source, log_message)

#         st.markdown(f"""
#         <div class="result-box">
#             <div class="result-label">Predicted Label</div>
#             <div class="result-value">{prediction}</div>
#         </div>
#         """, unsafe_allow_html=True)

# # ---------------- FOOTER ----------------
# st.markdown(
#     '<div class="footer">Built with Streamlit • NLP • Machine Learning</div>',
#     unsafe_allow_html=True
# )

# # ---------------- MAIN CARD END ----------------
# st.markdown('</div>', unsafe_allow_html=True)




