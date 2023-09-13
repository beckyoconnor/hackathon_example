import streamlit as st

st.set_page_config(
    page_title="UK Energy Hackathon",
    page_icon="👋",
)

st.write("# Vunerability assessment")

st.sidebar.success("Select a demo above.")

st.markdown(
    """##### 

Vulnerability Assessment: Develop tools and models that can identify and address vulnerabilities in communities, helping governments and organisations make informed decisions to improve safety and well-being.
By participating in this hackathon, you become a crucial part of the pursuit of a sustainable and efficient utilities and energy market. Together, we can drive innovation, reduce environmental impact, and create a brighter future for generations to come.

Ark Household File
ONS LSOA shape files

Join the tables potentially do clustering, classification of segments (find types of clusters based on the ark metric) 
Use https://nhess.copernicus.org/articles/23/2133/2023/ shared by Suraj Rajan 
Represent the clusters on a map in either a streamlit app or hex

"""
)
                
