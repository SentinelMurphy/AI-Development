# Streamlit Web Application
import streamlit as st
import asyncio

from crew import CourseGeneratorCrew

# Configure Streamlit page
st.set_page_config(
    page_title="AI Course Creator",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Custom CSS
st.markdown(
    """
    <style>
        .stProgress .st-bo, {
            background-color: #00a0dc;
        }
        .success-text {
            color: #00c853;
        }
        .warning-text {
            color: #ffd700;
        }
        .error-text {
            color: #ff5252;
        }
        .st-emotion-cache-1v0mbdj.e115fcil1 {
            border: 1px solid #ddd;
            border-radius: 10px;
            padding: 20px;
        }
    </style>
""",
    unsafe_allow_html=True,
)


def create_course_contents(course,units):
    """Process course creator crew"""
    try: 
        return  CourseGeneratorCrew().run_crew(units).kickoff_async(inputs={'title':course})
    except Exception as e:
        print(f"Error starting crews: {str(e)}")
        raise


def main():
    # Sidebar navigation
    with st.sidebar:
        st.image(
            "https://img.icons8.com/?size=100&id=60436&format=png&color=000000",
            width=50,
        )

        with st.form(key='channel_form'):
           course = st.text_input("Course")
           units =  st.text_input("units")
           submit_button = st.form_submit_button(label='Generate course')
           

   
    st.header("📄 AI Course Generator!")
    if submit_button:
        
        st.write(" ")
        progress_bar = st.progress(0)
        status_text = st.empty()
        try:
            status_text.text("generating course content...")
            progress_bar.progress(25)
                
            print("start_crew start")
            result = asyncio.run(create_course_contents(course,units))
            print("start_crew end",result)

            progress_bar.progress(100)
            status_text.text("course content generation completed!")
            st.markdown(result.raw)
        except Exception as e:
            st.error(f"Error processing videos: {str(e)}")
        
    


if __name__ == "__main__":
    main()


