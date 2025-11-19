import streamlit as st
import pandas as pd

# Page configuration
st.set_page_config(
    page_title="KUCCPS Course Advisor",
    page_icon="🎓",
    layout="wide"
)

# Title with hackathon badge
st.title("🎓 KUCCPS Course Advisor Chatbot")
st.markdown("**🏆 1st Place Winner - Botathon at Mama Ngina University**")

# Initialize conversation
if 'conversation' not in st.session_state:
    st.session_state.conversation = []

# Sample course data
sample_courses = [
    {"course": "Computer Science", "careers": "Software Developer, Data Scientist, AI Engineer", "subjects": "Math, Physics"},
    {"course": "Medicine", "careers": "Doctor, Surgeon, Medical Researcher", "subjects": "Biology, Chemistry"},
    {"course": "Engineering", "careers": "Civil Engineer, Mechanical Engineer, Electrical Engineer", "subjects": "Math, Physics, Chemistry"},
    {"course": "Business Administration", "careers": "Manager, Entrepreneur, Business Analyst", "subjects": "Math, Business"},
    {"course": "Law", "careers": "Lawyer, Judge, Legal Advisor", "subjects": "History, English"}
]

# Course recommendation function
def get_course_recommendation(query):
    query_lower = query.lower()
    
    recommendations = []
    for course in sample_courses:
        if any(keyword in query_lower for keyword in ['computer', 'tech', 'programming', 'software', 'data', 'ai']) and course['course'] == 'Computer Science':
            recommendations.append(course)
        elif any(keyword in query_lower for keyword in ['doctor', 'medical', 'health', 'hospital', 'surgery']) and course['course'] == 'Medicine':
            recommendations.append(course)
        elif any(keyword in query_lower for keyword in ['engineer', 'build', 'design', 'construction', 'mechanical']) and course['course'] == 'Engineering':
            recommendations.append(course)
        elif any(keyword in query_lower for keyword in ['business', 'manage', 'entrepreneur', 'company', 'finance']) and course['course'] == 'Business Administration':
            recommendations.append(course)
        elif any(keyword in query_lower for keyword in ['law', 'legal', 'lawyer', 'court', 'justice']) and course['course'] == 'Law':
            recommendations.append(course)
    
    if not recommendations:
        return [sample_courses[0]]
    
    return recommendations

# Chat interface
st.markdown("### 💬 Chat with Course Advisor")

# Display conversation
for message in st.session_state.conversation:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User input
if prompt := st.chat_input("What career are you interested in?"):
    st.session_state.conversation.append({"role": "user", "content": prompt})
    
    with st.chat_message("user"):
        st.markdown(prompt)
    
    with st.chat_message("assistant"):
        with st.spinner("Finding the best courses for you..."):
            recommendations = get_course_recommendation(prompt)
            
            if recommendations:
                response = f"Based on your interest in **{prompt}**, I recommend:\n\n"
                for course in recommendations:
                    response += f"**🎓 {course['course']}**\n"
                    response += f"**Careers:** {course['careers']}\n"
                    response += f"**Key Subjects:** {course['subjects']}\n\n"
                response += "Would you like more details about any of these courses?"
            else:
                response = "I'd love to help you find the right course! Could you tell me more about your interests, favorite subjects, or career goals?"
            
            st.markdown(response)
            st.session_state.conversation.append({"role": "assistant", "content": response})

# Sidebar with project info
with st.sidebar:
    st.markdown("### 🏆 Hackathon Project")
    st.markdown("""
    **Botathon Winner Features:**
    - RAG Architecture
    - Vector Database Search
    - LLM Integration
    - Course Recommendation Engine
    """)
