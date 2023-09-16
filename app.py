import requests
import streamlit as st
from streamlit_lottie import st_lottie

st.set_page_config(page_title="Python web", page_icon=":floppy_disk:", layout="wide")
def loadlottieurl(url):
    r = requests.get(url)
    if r.status_code !=200:
        return None
    return r.json()

lotti_code = loadlottieurl("https://lottie.host/c0df62a1-de1b-46a4-9738-68fc288a20e9/NkGEYciRZB.json")

with st.container():
    st.subheader("Hello, Áron vagyok :wave:")
    st.title("Ezt én csináltam 13 évesen")
    st.text("Ez az első normális python webhelyem amivel két napot töltöttem el hogy létre jöjjön")
    
with st.container():
    st.write("---")
    left_coumn, right_column = st.columns(2)
    with left_coumn:
        st.header("What I do")
        st.write("##")
        st.write(
            """
            Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam a ipsum diam. Sed a sapien malesuada, tristique justo a, egestas nulla. Donec a feugiat ante. Maecenas interdum placerat lorem, ut interdum velit rhoncus ullamcorper. Praesent vitae orci sit amet orci suscipit condimentum quis in lacus. Quisque ut ante egestas, feugiat nibh ac, egestas augue. Etiam pharetra felis eu pulvinar malesuada. Vestibulum lobortis est nec lorem facilisis, vel faucibus ex rhoncus. Cras pharetra sed lorem ut facilisis. Quisque rhoncus hendrerit nisl vitae fermentum. Sed laoreet, nisl ut gravida mollis, dolor lectus elementum felis, in lobortis dui felis ut sem. Sed ac.
            """)
        
    with right_column:
        st_lottie(lotti_code, height=300, key="coding")