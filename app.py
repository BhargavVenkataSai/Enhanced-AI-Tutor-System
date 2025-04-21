"""
Main Streamlit app for Enhanced Learning Assistant.
Handles all stages from topic input to report generation.
"""
import streamlit as st
from research.web import fetch_web_content
from research.academic import fetch_academic_papers
from research.video import fetch_video_transcripts
from personalize.interactive_questions import ask_questions
from research.report import generate_report
import time
import json

def load_custom_css():
    st.markdown("""
        <style>
            html, body, [class*="css"] {
                font-family: 'Segoe UI', sans-serif;
                background: linear-gradient(135deg, #f8f9fa, #ff6633);
            }
            .main {
                background-color: #ffffffcc;
                padding: 1.5rem;
                border-radius: 15px;
                box-shadow: 0px 2px 10px rgba(0,0,0,0.1);
            }
            h1 {
                color: #0056b3;
            }
            h2 {
                color: #007bff;
                margin-top: 1rem;
            }
            h3 {
                color: #0069d9;
            }
            .stButton > button {
                background-color: #1f77b4;
                color: white;
                border-radius: 10px;
                padding: 0.5rem 1rem;
                transition: 0.3s;
            }
            .stButton > button:hover {
                background-color: #0056b3;
                transform: scale(1.05);
            }
            .stRadio > div {
                background-color: #1c1e29;
                border-radius: 10px;
                padding: 0.5rem;
                margin-bottom: 0.5rem;
                box-shadow: 0px 1px 3px rgba(0,0,0,0.05);
            }
            .question-card {
                background-color: #3364b4;
                border-radius: 10px;
                padding: 1rem;
                margin-bottom: 1rem;
                border-left: 4px solid #bbbbbb;
            }
            .resource-card {
                background-color: white;
                border-radius: 10px;
                padding: 1rem;
                margin-bottom: 1rem;
                box-shadow: 0px 2px 5px rgba(0,0,0,0.05);
                border-left: 4px solid #1f77b4;
            }
            .citation {
                font-size: 0.8rem;
                color: #6c757d;
                font-style: italic;
            }
            .feedback-box {
                background-color: #e3f2fd;
                border-radius: 10px;
                padding: 1rem;
                margin-top: 1rem;
                border: 1px solid #b3e5fc;
            }
            .stage-indicator {
                display: flex;
                justify-content: space-between;
                margin-bottom: 2rem;
            }
            .stage {
                text-align: center;
                padding: 0.5rem;
                border-radius: 5px;
                background-color: #007bff;
                flex: 1;
                margin: 0 0.5rem;
            }
            .stage.active {
                background-color: #007bff;
                color: white;
                font-weight: bold;
            }
            .source-link {
                text-decoration: none;
                color: #007bff;
                font-weight: 500;
            }
            .source-link:hover {
                text-decoration: underline;
            }
            .stTabs [data-baseweb="tab-list"] {
                gap: 2px;
            }
            .stTabs [data-baseweb="tab"] {
                border-radius: 5px 5px 0px 0px;
                padding: 10px 20px;
                background-color: #3364b4;
            }
            .stTabs [aria-selected="true"] {
                background-color: #3364b4;
                color: blue;
            }
        </style>
    """, unsafe_allow_html=True)

def display_stage_indicator(current_stage):
    stages = ["Input Topic", "Research", "Personalize", "Generate Report", "Review & Refine"]
    
    html_stages = ""
    for i, stage in enumerate(stages):
        if i+1 == current_stage:
            html_stages += f'<div class="stage active">{i+1}. {stage}</div>'
        else:
            html_stages += f'<div class="stage">{i+1}. {stage}</div>'
    
    st.markdown(f'<div class="stage-indicator">{html_stages}</div>', unsafe_allow_html=True)

def render_web_results(web_results):
    if not web_results:
        st.info("No web content has been collected yet.")
        return
    
    for i, result in enumerate(web_results):
        with st.expander(f"{result['title']}", expanded=i < 1):
            st.markdown(f"**Source:** {result['source']}")
            st.markdown(f"**Summary:** {result['summary']}")
            st.markdown(f"[View Source]({result['url']})", unsafe_allow_html=True)

def render_academic_results(academic_results):
    if not academic_results:
        st.info("No academic papers have been collected yet.")
        return
    
    for i, paper in enumerate(academic_results):
        with st.expander(f"{paper['title']}", expanded=i < 1):
            st.markdown(f"**Authors:** {paper['authors']}")
            st.markdown(f"**Journal:** {paper['journal']} ({paper['year']})")
            st.markdown(f"**DOI:** {paper['doi']}")
            st.markdown(f"**Summary:** {paper['summary']}")
            if 'keywords' in paper:
                st.markdown(f"**Keywords:** {', '.join(paper['keywords'])}")

def render_video_results(video_results):
    if not video_results:
        st.info("No video transcripts have been collected yet.")
        return
    
    for i, video in enumerate(video_results):
        with st.expander(f"{video['title']} ({video['duration']})", expanded=i < 1):
            st.markdown(f"**Creator:** {video['creator']} on {video['platform']}")
            st.markdown(f"**Summary:** {video['transcript_summary']}")
            
            st.markdown("**Key Timestamps:**")
            for timestamp, description in video['key_timestamps'].items():
                st.markdown(f"- **{timestamp}:** {description}")
                
            st.markdown(f"[Watch Video]({video['url']})", unsafe_allow_html=True)

def render_interactive_questions(questions_by_category, topic):
    if not questions_by_category:
        st.info("No questions have been generated yet.")
        return
    
    answers = {}
    
    for category, questions in questions_by_category.items():
        st.subheader(f"{category.replace('_', ' ').title()}")
        
        for q in questions:
            q_id = q['id']
            question = q['question']
            
            st.markdown(f"<div class='question-card'><strong>{question}</strong>", unsafe_allow_html=True)
            
            if q['type'] == 'single_select':
                answers[q_id] = st.radio(
                    label=f"Select one option for {q_id}",
                    options=q['options'],
                    key=f"q_{q_id}",
                    label_visibility="collapsed"
                )
            elif q['type'] == 'multi_select':
                answers[q_id] = st.multiselect(
                    label=f"Select one or more options for {q_id}",
                    options=q['options'],
                    key=f"q_{q_id}",
                    label_visibility="collapsed"
                )
            elif q['type'] == 'text_input':
                placeholder = q.get('placeholder', 'Enter your response here')
                answers[q_id] = st.text_input(
                    label=f"Enter text for {q_id}",
                    placeholder=placeholder,
                    key=f"q_{q_id}",
                    label_visibility="collapsed"
                )
            
            st.markdown("</div>", unsafe_allow_html=True)
    
    return answers

def collect_research(topic):
    # Perform simulated research on topic
    with st.spinner(f"📚 Researching {topic}..."):
        # Simulate research time
        progress_bar = st.progress(0)
        
        # Fetch web content
        progress_bar.progress(10)
        st.session_state.web_results = fetch_web_content(topic)
        progress_bar.progress(40)
        
        # Fetch academic papers
        st.session_state.academic_results = fetch_academic_papers(topic)
        progress_bar.progress(70)
        
        # Fetch video transcripts
        st.session_state.video_results = fetch_video_transcripts(topic)
        progress_bar.progress(100)
        
        time.sleep(0.5)
        progress_bar.empty()
        
    return {
        "web_results": st.session_state.web_results,
        "academic_results": st.session_state.academic_results,
        "video_results": st.session_state.video_results
    }

# Set page config first (must be the first Streamlit command)
st.set_page_config(page_title="Enhanced Learning Assistant", layout="wide", initial_sidebar_state="expanded")

# Load custom CSS
load_custom_css()

# Initialize session state variables if they don't exist
if 'stage' not in st.session_state:
    st.session_state.stage = 1

for key in ['web_results', 'academic_results', 'video_results', 'preferences', 'topic', 'objective', 'report', 'user_feedback']:
    if key not in st.session_state:
        st.session_state[key] = None

# Display title and stage indicator
st.title("🎓 Enhanced Interactive Learning Assistant")
display_stage_indicator(st.session_state.stage)

# STAGE 1: Topic and Objective Input
if st.session_state.stage == 1:
    st.header("Step 1: Define Your Learning Goals")
    
    topic = st.text_input("What topic would you like to learn about?", value=st.session_state.topic or "")
    objective = st.text_area("What are your specific learning objectives or goals?", 
                            value=st.session_state.objective or "",
                            placeholder="Example: I want to understand the basic principles and learn how to apply them in my work")
    
    if st.button("Start Learning Journey"):
        if not topic or not objective:
            st.warning("Please provide both a topic and objectives to continue.")
        else:
            st.session_state.topic = topic
            st.session_state.objective = objective
            st.session_state.stage = 2
            st.rerun()

# STAGE 2: Research Collection
elif st.session_state.stage == 2:
    st.header(f"Step 2: Research on {st.session_state.topic}")
    
    if not all([st.session_state.web_results, st.session_state.academic_results, st.session_state.video_results]):
        research_results = collect_research(st.session_state.topic)
        st.success(f"✅ Research on {st.session_state.topic} completed!")
    
    tab1, tab2, tab3 = st.tabs(["📄 Web Content", "📚 Academic Papers", "🎥 Video Transcripts"])
    
    with tab1:
        render_web_results(st.session_state.web_results)
    
    with tab2:
        render_academic_results(st.session_state.academic_results)
    
    with tab3:
        render_video_results(st.session_state.video_results)
    
    if st.button("Continue to Personalization"):
        st.session_state.stage = 3
        st.rerun()

# STAGE 3: Personalization Questions
elif st.session_state.stage == 3:
    st.header("Step 3: Personalize Your Learning Experience")
    
    questions = ask_questions(st.session_state.topic)
    
    answers = render_interactive_questions(questions, st.session_state.topic)
    
    if st.button("Save Preferences & Continue"):
        st.session_state.preferences = answers
        st.success("✅ Your learning preferences have been saved!")
        st.session_state.stage = 4
        st.rerun()

# STAGE 4: Generate Report
elif st.session_state.stage == 4:
    st.header("Step 4: Generate Personalized Learning Report")
    
    if st.session_state.report is None:
        with st.spinner("🧠 Generating your personalized learning report..."):
            # Simulate report generation time
            progress_bar = st.progress(0)
            for i in range(0, 101, 10):
                progress_bar.progress(i)
                time.sleep(0.2)
            
            st.session_state.report = generate_report(
                st.session_state.topic,
                st.session_state.objective,
                st.session_state.preferences,
                st.session_state.web_results,
                st.session_state.academic_results,
                st.session_state.video_results
            )
            progress_bar.empty()
    
    st.info("Your personalized learning report has been generated! Click 'View Full Report' to review and make adjustments if needed.")
    
    if st.button("View Full Report"):
        st.session_state.stage = 5
        st.rerun()

# STAGE 5: Report Review and Modification
elif st.session_state.stage == 5:
    st.header(f"Personalized Learning Report: {st.session_state.topic}")
    
    # Display the full report
    st.markdown(st.session_state.report, unsafe_allow_html=True)
    
    # Feedback and modification section
    st.markdown("### Provide Feedback for Report Modifications")
    
    feedback = st.text_area(
        "Please provide any feedback or requests for modifications to your report:",
        placeholder="Example: I'd like more focus on practical applications or please expand the section on historical context",
        key="feedback_input"
    )
    
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("Regenerate Report with Feedback"):
            if feedback:
                st.session_state.user_feedback = feedback
                
                # In a real implementation, this would analyze the feedback and modify the report
                # For this simulation, we'll just acknowledge the feedback
                st.session_state.report += f"\n\n## Report Modification Based on Feedback\n\n{feedback}\n\n*The report has been updated to address this feedback.*"
                
                st.success("Report has been updated based on your feedback!")
                st.rerun()
            else:
                st.warning("Please provide feedback for report modification.")
    
    with col2:
        if st.button("Start a New Learning Journey"):
            # Reset all state except for preferences which might be reused
            for key in ['web_results', 'academic_results', 'video_results', 'topic', 'objective', 'report', 'user_feedback']:
                st.session_state[key] = None
            
            st.session_state.stage = 1
            st.rerun()

# Sidebar with navigation and help
with st.sidebar:
    st.header("Navigation")
    
    # Allow direct navigation between stages
    if st.button("1. Define Topic & Objectives"):
        st.session_state.stage = 1
        st.rerun()
    
    if st.button("2. Research Collection"):
        if st.session_state.topic:
            st.session_state.stage = 2
            st.rerun()
        else:
            st.warning("Please define a topic first")
    
    if st.button("3. Personalization"):
        if all([st.session_state.topic, st.session_state.web_results]):
            st.session_state.stage = 3
            st.rerun()
        else:
            st.warning("Complete research first")
    
    if st.button("4. Generate Report"):
        if all([st.session_state.topic, st.session_state.preferences]):
            st.session_state.stage = 4
            st.rerun()
        else:
            st.warning("Complete personalization first")
    
    if st.button("5. View & Modify Report"):
        if st.session_state.report:
            st.session_state.stage = 5
            st.rerun()
        else:
            st.warning("Generate report first")
    
    st.markdown("---")
    
    # Help section
    st.header("How It Works")
    st.markdown("""
    1. **Define** your learning topic and objectives
    2. **Research** gathers information from multiple sources
    3. **Personalize** by answering questions about your preferences
    4. **Generate** a comprehensive learning report
    5. **Review & Modify** the report based on your feedback
    """)
    
    st.markdown("---")
    
    # About section
    st.header("About")
    st.markdown("""
    Enhanced Learning Assistant uses simulated AI research capabilities to create personalized educational reports on any topic.
    
    This is a demonstration of an AI tutor system that could integrate with real-world research APIs and learning resources.
    """)


