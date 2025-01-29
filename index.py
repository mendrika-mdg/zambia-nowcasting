import streamlit as st                                                      #type: ignore
st.set_page_config(layout="wide")
from datetime import time, datetime
from matplotlib.backends.backend_agg import RendererAgg                     #type: ignore
_lock = RendererAgg.lock
from datetime import datetime, time, timedelta
import os
from PIL import Image                                                       #type: ignore
import io

header_footer_css = """
    <style>
    .header {
      position: fixed;
        top: 0;
        left: 0;
        right: 0;
        background-color: #f1f1f1;
        color: black;
        text-align: center;
        padding: 10px;
        font-size: 20px;
        z-index: 10;
    }
    .footer {
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        background-color: #f1f1f1;
        color: black;
        text-align: center;
        padding: 10px;
        font-size: 12px;
        z-index: 10;
    }
    .main-content {
        padding-top: 0px;  /* Space for header */
        padding-bottom: 40px; /* Space for footer */
    }
    </style>
"""

########################################################################### HEADER ##########################################################################################################

st.markdown(header_footer_css, unsafe_allow_html=True)
#st.markdown('<div class="header">Welcome to My Streamlit App</div>', unsafe_allow_html=True)


########################################################################### CONTENT ##########################################################################################################

st.sidebar.title("Menu")
page = st.sidebar.radio("Go to", ["Home", "Climatology", "Model" ,"Nowcast Portal", "Contact us"])

# Content for Page 1
if page == "Home":
    st.title("Convective Storm Nowcasting Using Machine Learning")

    st.header("Project Abstract")
    abstract = """
    Convective storm nowcasting plays a crucial role in early warning and mitigating the impact of severe weather. 
    
    This study introduces a fast, simple, yet effective object based approach using machine learning. 
    Storm objects are identified via a 2D wavelet transform on cloud-top temperature satellite data. Features such as time of observation (t0), latitude, longitude, size, distance, and wavelet power of nearest storm to 
    Zambia are used to predict storm occurrence 1 to 6 hours ahead. 
    
    Initial results for Dakar outperformed an operational conditional climatology model for 1-, 3-, and 6-
    hour lead times. Explainable AI techniques, such as Shapley values, were used to ensure
    the model’s predictions are meteorologically consistent. The model was expanded to
    cover a larger region while maintaining the input structure. 
    
    Additionally, modifications
    were made to include LSTMs for sequential storm information and convolutional layers
    for gridded nowcasting. Performance, evaluated using the Fractions Skill Score (FSS),
    showed skill for 1- and 3-hour lead times.
    """
    st.success(abstract)

    st.info(
        """
        **Goal**: To leverage information about the nearest storm 
        (time of observation, latitude, longitude, size, distance) 
        to predict storm occurrences at different lead times using a hybrid LSTM-CONV based deep learning architecture.
        """)

    st.markdown('<div class="footer">&copy; 2025 Mendrika Rakotomanga. All Rights Reserved.</div>', unsafe_allow_html=True)


elif page == "Climatology":

    st.title("Diurnal climatology of convective cores in Zambia")
    st.write("Based on methods described by Anderson et al. (2024)")

    spatial_scale = st.radio( "Select a spatial scale (in km)", options=[45, 95], horizontal=True)
    time_pc = st.time_input("Choose a time of day", value=datetime.strptime('12:00', '%H:%M')).strftime('%H-%M')
    file_pc = f"./public/images/pc/{spatial_scale}/pc-Zambia-{time_pc}-{spatial_scale}.png"
    st.image(file_pc)
    st.markdown('<div class="footer">&copy; 2025 Mendrika Rakotomanga. All Rights Reserved.</div>', unsafe_allow_html=True)


elif page == "Model":

    st.title("An Object-Based Approach to Convective Storm Nowcasting Using Machine Learning")
    st.header("Model Architecture")

    st.image("/localhome/home/mmmhr/deploy-web/images/lstm.png", caption="Convective Storm Nowcasting Project", use_container_width=False)

    st.markdown('<div class="footer">&copy; 2025 Mendrika Rakotomanga. All Rights Reserved.</div>', unsafe_allow_html=True)

elif page == "Nowcast Portal":
    st.title("Convective Storm Nowcasting Using Machine Learning")
    st.write("**Author**: Mendrika Rakotomanga, Douglas Parker, Nadhir B. Rached, Seonaid Anderson, Cornelia Klein")
    st.empty()

    observation, spacer, nowcast = st.columns([1, 0.5, 1])  # Adjust the width ratios as needed

    with observation:

        selected_date = st.date_input("Choose a date", datetime.today())
        current_time = datetime.now().time()
        selected_time = st.time_input("Choose a time", current_time)
        # Display selected time
        st.write(f"Selected time: {selected_time.strftime('%H:%M')}")

        formatted_date = selected_date.strftime('%Y%m%d')
        formatted_time = selected_time.strftime('%H%M')        

    with spacer:
        st.write("") 


    # Add a title and slider in the second column
    with nowcast:
        st.subheader("Nowcast")

        lead_time = st.select_slider( "Select a lead time", options=[1, 3],  value=1)
        st.write(f"Lead time: {lead_time} h")

    st.empty()  
    st.markdown('<div class="footer">&copy; 2025 Mendrika Rakotomanga. All Rights Reserved.</div>', unsafe_allow_html=True)
    st.warning("This is just an example from 2020-07-11 at 18:30 UTC.")

elif page == "Contact us":

    # Add a description or introduction
    st.write("Have questions or want to get in touch? Fill out the form below and we’ll get back to you as soon as possible.")

    # Create a form for the "Contact Us" page
    with st.form(key="contact_form"):
        # Input fields for name, email, and message
        name = st.text_input("Name", placeholder="Your full name")
        email = st.text_input("Email", placeholder="yourname@example.com")
        message = st.text_area("Message", placeholder="Type your message here")

        # Submit and Clear buttons
        submit_button = st.form_submit_button(label="Submit")
        clear_button = st.form_submit_button(label="Clear")

    # Handle form submission
    if submit_button:
        if name and email and message:
            st.success(f"Thank you for reaching out, {name}! We'll get back to you at {email} soon.")
        else:
            st.error("Please fill out all fields before submitting the form.")

    # Optional: Display a footer or additional information
    st.markdown("---")
    st.write("You can also reach us at [mmmhr@leeds.ac.uk](mailto:mmmhr@leeds.ac.uk)")

    st.empty()  
    st.markdown('<div class="footer">&copy; 2025 Mendrika Rakotomanga. All Rights Reserved.</div>', unsafe_allow_html=True)
