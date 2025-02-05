import streamlit as st                                                      #type: ignore
from datetime import datetime, time, timedelta

st.set_page_config(
    page_title="Object-based Nowcasting",
    page_icon="🌧️",               
    layout="wide"                 
)

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
st.markdown(header_footer_css, unsafe_allow_html=True)


st.sidebar.title("Menu")
page = st.sidebar.radio("Go to", ["Home", "Climatology" ,"Nowcast Portal", "Contact us"])

# Content for Page 1
if page == "Home":

    st.title("Convective Core Nowcasting Using Machine Learning with an Object-Based Approach")
    st.write("**Authors**: Mendrika Rakotomanga, Douglas Parker, Nadhir B. Rached, Steven Tobias, Seonaid Anderson, Cornelia Klein")

    st.header("Description")
    abstract = """
    Convective core nowcasting plays a crucial role in early warning and mitigating the impact of severe weather. 
    
    This study introduces a fast, simple, yet effective object based approach using machine learning. 
    Storm objects are identified via a 2D wavelet transform on cloud-top temperature satellite data. 
    
    Features such as time of observation ($t_0$), latitude, longitude, size, distance, and wavelet power of nearby storms to 
    Zambia are used to predict storm occurrence 1 hour ahead. 
    """
    st.success(abstract)

    st.image("./public/images/model/architecture/example-of-prediction.png",  caption="Example of forecast using our model")

    st.success("Data from EUMETSAT and developed at UKCEH")

    st.markdown('<div class="footer">&copy; 2025 Mendrika Rakotomanga. All Rights Reserved.</div>', unsafe_allow_html=True)


elif page == "Climatology":

    st.title("Diurnal climatology of convective cores in Zambia")

    st.write("""The full climatological probabilities of convective activity give a static overview of diurnal 
    and spatial variations in convective probability
    
    Climatology probabilities calculated as described by Anderson et al. (2024)""")

    spatial_scale = st.radio( "Select a spatial scale (in km)", options=[45, 95], horizontal=True)
    time_pc = st.time_input("Choose a time of day", value=datetime.strptime('12:00', '%H:%M')).strftime('%H-%M')
    file_pc = f"./public/images/pc/{spatial_scale}/pc-Zambia-{time_pc}-{spatial_scale}.png"
    st.image(file_pc)

    st.markdown('<div class="footer">&copy; 2025 Mendrika Rakotomanga. All Rights Reserved.</div>', unsafe_allow_html=True)

elif page == "Nowcast Portal":
    st.title("Convective Core Nowcasting Using Machine Learning")
    st.empty()

    observation, spacer, nowcast = st.columns([1, 0.5, 1])  # Adjust the width ratios as needed

    with observation:
        st.subheader("Observation")

        st.write("Choose nowcast origin ($t_0$) in UTC")

        # Get the current UTC time and round it to the nearest past 15-minute step
        now_utc = datetime.utcnow()
        rounded_minutes = (now_utc.minute // 15) * 15  # Round down to nearest 15 minutes
        default_time = now_utc.replace(minute=rounded_minutes, second=0, microsecond=0).time()

        # User inputs
        selected_date = st.date_input("Choose a date", value=now_utc.date())
        selected_time = st.time_input("Choose a time", value=default_time)
        selected_datetime = datetime.combine(selected_date, selected_time)

        formatted_date = selected_date.strftime('%Y-%m-%d')
        formatted_time = selected_time.strftime('%H-%M')

        # Create the slider
        selected_value = st.slider("Observation before $t_0$ (in minutes):", min_value=-120, max_value=0, step=15, value=0)

        # Compute and display adjusted observation time
        display_datetime = selected_datetime + timedelta(minutes=int(selected_value))
        # st.write(f"Observation displayed: {display_datetime}")

        # Construct file path
        file_observation = f"./public/images/observation/observation-{display_datetime.strftime('%Y-%m-%d-%H-%M')}.png"

        # Display image if available
        try:
            st.image(file_observation)
        except Exception:
            st.error("No data available")

    with spacer:
        st.write("") 

    with nowcast:
        st.subheader("1 Hour Nowcast")
        file_nowcast = f"./public/images/nowcast/nowcast-{selected_datetime.strftime('%Y-%m-%d-%H-%M')}.png"   
        try:
            st.image(file_nowcast)
            st.write(f"1 pixel is equal to 45 Km")
        except Exception as e:
            st.error(f"Nowcast unavailable since no cores were observed at {selected_datetime} UTC")
    st.empty()  
    st.markdown('<div class="footer">&copy; 2025 Mendrika Rakotomanga. All Rights Reserved.</div>', unsafe_allow_html=True)

elif page == "Contact us":

    st.write("Have questions or want to get in touch? Fill out the form below and we’ll get back to you as soon as possible.")

    # Create a form for the "Contact Us" page
    with st.form(key="contact_form"):
        # Input fields for name, email, and message
        name = st.text_input("Name", placeholder="Your name")
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
