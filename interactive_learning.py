"""
Interactive Learning Module - Provides interactive learning features for the AI tutor.
"""
import streamlit as st
import json
import random
from typing import Dict, List, Optional, Tuple
from ai_tutor import generate_explanation, generate_quiz_questions, generate_practice_problems, provide_feedback

def render_concept_explorer(topic: str, concept: str, difficulty: str = "intermediate"):
    """
    Render an interactive concept explorer.
    
    Args:
        topic (str): The main topic
        concept (str): The specific concept to explore
        difficulty (str): The difficulty level (beginner, intermediate, advanced)
    """
    st.subheader(f"Concept Explorer: {concept}")
    
    # Generate explanation
    with st.spinner(f"Generating explanation for {concept}..."):
        explanation = generate_explanation(topic, concept, difficulty)
    
    # Display explanation
    st.markdown(explanation)
    
    # Add interactive elements
    st.markdown("### Interactive Elements")
    
    # Ask if the explanation was helpful
    helpful = st.radio(
        "Was this explanation helpful?",
        ["Yes", "Partially", "No"],
        horizontal=True
    )
    
    if helpful == "No" or helpful == "Partially":
        st.text_area("What could be improved?", key=f"improve_{concept}")
    
    # Ask for questions
    question = st.text_input("Do you have any questions about this concept?", key=f"question_{concept}")
    if question:
        with st.spinner("Generating answer..."):
            answer = generate_explanation(topic, question, difficulty)
            st.markdown(f"**Answer:** {answer}")
    
    # Add a "Generate Quiz" button
    if st.button("Generate Quiz on this Concept", key=f"quiz_{concept}"):
        with st.spinner("Generating quiz questions..."):
            questions = generate_quiz_questions(f"{topic} - {concept}", num_questions=3, difficulty=difficulty)
            
            # Display questions
            for i, q in enumerate(questions):
                st.markdown(f"### Question {i+1}")
                st.markdown(f"**{q['question']}**")
                
                # Display options
                options = q.get('options', [])
                if options:
                    user_answer = st.radio(
                        "Select your answer:",
                        options,
                        key=f"q_{i}_{concept}",
                        label_visibility="collapsed"
                    )
                    
                    # Check answer
                    if st.button("Check Answer", key=f"check_{i}_{concept}"):
                        correct_answer = q.get('correct_answer', '')
                        feedback = provide_feedback(user_answer, correct_answer, q['question'])
                        
                        # Display feedback
                        if feedback.get('is_correct', False):
                            st.success("Correct! 🎉")
                        else:
                            st.error("Incorrect. Try again!")
                        
                        st.markdown(f"**Explanation:** {feedback.get('correct_answer_explanation', '')}")
                        st.markdown(f"**Further Study:** {feedback.get('further_study', '')}")

def render_interactive_quiz(topic: str, num_questions: int = 5, difficulty: str = "intermediate"):
    """
    Render an interactive quiz.
    
    Args:
        topic (str): The topic to quiz on
        num_questions (int): Number of questions to generate
        difficulty (str): The difficulty level (beginner, intermediate, advanced)
    """
    st.subheader(f"Interactive Quiz: {topic}")
    
    # Generate questions
    with st.spinner("Generating quiz questions..."):
        questions = generate_quiz_questions(topic, num_questions, difficulty)
    
    # Initialize session state for quiz
    if 'quiz_answers' not in st.session_state:
        st.session_state.quiz_answers = {}
    if 'quiz_feedback' not in st.session_state:
        st.session_state.quiz_feedback = {}
    if 'quiz_completed' not in st.session_state:
        st.session_state.quiz_completed = False
    
    # Display questions
    for i, q in enumerate(questions):
        st.markdown(f"### Question {i+1}")
        st.markdown(f"**{q['question']}**")
        
        # Display options
        options = q.get('options', [])
        if options:
            user_answer = st.radio(
                "Select your answer:",
                options,
                key=f"q_{i}",
                label_visibility="collapsed"
            )
            
            # Store answer
            st.session_state.quiz_answers[i] = user_answer
            
            # Check answer
            if st.button("Check Answer", key=f"check_{i}"):
                correct_answer = q.get('correct_answer', '')
                feedback = provide_feedback(user_answer, correct_answer, q['question'])
                
                # Store feedback
                st.session_state.quiz_feedback[i] = feedback
                
                # Display feedback
                if feedback.get('is_correct', False):
                    st.success("Correct! 🎉")
                else:
                    st.error("Incorrect. Try again!")
                
                st.markdown(f"**Explanation:** {feedback.get('correct_answer_explanation', '')}")
    
    # Add a "Complete Quiz" button
    if st.button("Complete Quiz"):
        st.session_state.quiz_completed = True
        
        # Calculate score
        correct_count = sum(1 for i, feedback in st.session_state.quiz_feedback.items() 
                           if feedback.get('is_correct', False))
        total_questions = len(questions)
        score_percentage = (correct_count / total_questions) * 100
        
        # Display results
        st.markdown("### Quiz Results")
        st.markdown(f"**Score:** {correct_count}/{total_questions} ({score_percentage:.1f}%)")
        
        # Provide overall feedback
        if score_percentage >= 80:
            st.success("Excellent job! You have a strong understanding of this topic.")
        elif score_percentage >= 60:
            st.info("Good job! You have a good understanding of this topic, but there's room for improvement.")
        else:
            st.warning("You might need to review this topic. Consider going through the material again.")
        
        # Add a "Generate Practice Problems" button
        if st.button("Generate Practice Problems"):
            with st.spinner("Generating practice problems..."):
                problems = generate_practice_problems(topic, num_problems=3, difficulty=difficulty)
                
                # Display problems
                for i, p in enumerate(problems):
                    st.markdown(f"### Practice Problem {i+1}")
                    st.markdown(f"**{p['problem']}**")
                    
                    # Add a "Show Solution" button
                    if st.button("Show Solution", key=f"solution_{i}"):
                        st.markdown("**Solution:**")
                        for step in p.get('solution_steps', []):
                            st.markdown(f"- {step}")
                        
                        st.markdown(f"**Answer:** {p.get('answer', '')}")
                        st.markdown(f"**Key Concepts:** {', '.join(p.get('key_concepts', []))}")

def render_practice_problems(topic: str, num_problems: int = 3, difficulty: str = "intermediate"):
    """
    Render interactive practice problems.
    
    Args:
        topic (str): The topic to practice
        num_problems (int): Number of problems to generate
        difficulty (str): The difficulty level (beginner, intermediate, advanced)
    """
    st.subheader(f"Practice Problems: {topic}")
    
    # Generate problems
    with st.spinner("Generating practice problems..."):
        problems = generate_practice_problems(topic, num_problems, difficulty)
    
    # Display problems
    for i, p in enumerate(problems):
        st.markdown(f"### Problem {i+1}")
        st.markdown(f"**{p['problem']}**")
        
        # Add a text area for the user's solution
        user_solution = st.text_area(
            "Your solution:",
            key=f"solution_{i}",
            height=150
        )
        
        # Add a "Check Solution" button
        if st.button("Check Solution", key=f"check_solution_{i}"):
            # In a real implementation, this would compare the user's solution with the correct solution
            # For now, we'll just show the solution
            st.markdown("**Solution:**")
            for step in p.get('solution_steps', []):
                st.markdown(f"- {step}")
            
            st.markdown(f"**Answer:** {p.get('answer', '')}")
            st.markdown(f"**Key Concepts:** {', '.join(p.get('key_concepts', []))}")
            
            # Ask if the solution was helpful
            helpful = st.radio(
                "Was this solution helpful?",
                ["Yes", "Partially", "No"],
                horizontal=True,
                key=f"helpful_{i}"
            )
            
            if helpful == "No" or helpful == "Partially":
                st.text_area("What could be improved?", key=f"improve_solution_{i}")

def render_learning_path(topic: str, user_knowledge: str, learning_goals: str):
    """
    Render an interactive learning path.
    
    Args:
        topic (str): The topic to learn about
        user_knowledge (str): Description of the user's current knowledge
        learning_goals (str): The user's learning goals
    """
    st.subheader(f"Personalized Learning Path: {topic}")
    
    # Generate learning path
    with st.spinner("Generating personalized learning path..."):
        from ai_tutor import generate_learning_path
        learning_path = generate_learning_path(topic, user_knowledge, learning_goals)
    
    # Display overview
    st.markdown("### Overview")
    st.markdown(learning_path.get('overview', ''))
    
    # Display modules
    st.markdown("### Learning Modules")
    for i, module in enumerate(learning_path.get('modules', [])):
        with st.expander(f"Module {i+1}: {module.get('title', '')}"):
            st.markdown(f"**Key Concepts:**")
            for concept in module.get('key_concepts', []):
                st.markdown(f"- {concept}")
            
            st.markdown(f"**Resources:**")
            for resource in module.get('resources', []):
                st.markdown(f"- {resource}")
            
            st.markdown(f"**Estimated Time:** {module.get('estimated_time', '')}")
            
            if module.get('prerequisites', []):
                st.markdown(f"**Prerequisites:**")
                for prereq in module.get('prerequisites', []):
                    st.markdown(f"- {prereq}")
            
            # Add a "Start Module" button
            if st.button("Start Module", key=f"start_module_{i}"):
                st.session_state.current_module = i
                st.session_state.module_started = True
                st.rerun()
    
    # Display milestones
    st.markdown("### Milestones")
    for i, milestone in enumerate(learning_path.get('milestones', [])):
        st.markdown(f"{i+1}. {milestone}")
    
    # Display assessment methods
    st.markdown("### Assessment Methods")
    for i, method in enumerate(learning_path.get('assessment_methods', [])):
        st.markdown(f"- {method}")
    
    # Initialize session state for module tracking
    if 'current_module' not in st.session_state:
        st.session_state.current_module = 0
    if 'module_started' not in st.session_state:
        st.session_state.module_started = False
    
    # If a module is started, display its content
    if st.session_state.module_started:
        current_module = learning_path.get('modules', [])[st.session_state.current_module]
        
        st.markdown(f"### Current Module: {current_module.get('title', '')}")
        
        # Display module content
        for i, concept in enumerate(current_module.get('key_concepts', [])):
            with st.expander(f"Concept {i+1}: {concept}"):
                render_concept_explorer(topic, concept)
        
        # Add a "Complete Module" button
        if st.button("Complete Module"):
            st.session_state.module_started = False
            st.session_state.current_module += 1
            st.rerun()

def render_question_answer(topic: str):
    """
    Render an interactive Q&A interface.
    
    Args:
        topic (str): The topic to ask questions about
    """
    st.subheader(f"Ask Questions About {topic}")
    
    # Add a text input for the user's question
    question = st.text_input("Your question:", key="user_question")
    
    # Add a "Ask" button
    if st.button("Ask"):
        if question:
            with st.spinner("Generating answer..."):
                from ai_tutor import answer_user_question
                answer = answer_user_question(question, context=f"Topic: {topic}")
            
            # Display answer
            st.markdown("### Answer")
            st.markdown(answer)
            
            # Ask if the answer was helpful
            helpful = st.radio(
                "Was this answer helpful?",
                ["Yes", "Partially", "No"],
                horizontal=True
            )
            
            if helpful == "No" or helpful == "Partially":
                st.text_area("What could be improved?", key="improve_answer")
        else:
            st.warning("Please enter a question.") 