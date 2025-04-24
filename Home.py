import streamlit as st

def main():
    st.image("image14.png", width=200)
    st.title(" HIV Prevalence Prediction App")

    st.markdown("""
    Welcome to this interactive app that predicts HIV prevalence ( proportion of a population that is living with HIV at a given time) across countries and years 
    using machine learning and real-world health data.
    """)

    st.subheader(" What You Can Do Here:")

    st.markdown("""
    -  Explore HIV data trends and patterns  
    -  Learn about the model behind the predictions  
    -  Visualize HIV prevalence across the globe  
    -  Make predictions based on custom inputs  
    -  Ask questions to our chatbot assistant
    """)

    st.info("Navigate through the sidebar to get started!")


if __name__ == "__main__":
    st.set_page_config(
        page_title="HIV Prevalence Prediction App",
        layout="wide",
        initial_sidebar_state="expanded"
    )
    main()
