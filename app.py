"""
AI Tutor Module - Provides intelligent tutoring capabilities using OpenAI's API.
"""
import os
import openai
from dotenv import load_dotenv
from typing import Dict, List, Optional, Tuple

# Load environment variables
load_dotenv()

# Initialize OpenAI client
client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_explanation(topic: str, concept: str, difficulty: str = "intermediate") -> str:
    """
    Generate a detailed explanation of a concept using OpenAI's API.
    
    Args:
        topic (str): The main topic
        concept (str): The specific concept to explain
        difficulty (str): The difficulty level (beginner, intermediate, advanced)
        
    Returns:
        str: A detailed explanation of the concept
    """
    prompt = f"""
    Explain the concept of {concept} within the topic of {topic} at a {difficulty} level.
    Include:
    1. A clear definition
    2. Key components or principles
    3. Examples or analogies
    4. Common misconceptions
    5. How it relates to the broader topic
    
    Format the explanation in a clear, structured way that's easy to understand.
    """
    
    try:
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are an expert tutor with deep knowledge across many subjects."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=1000
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error generating explanation: {str(e)}"

def generate_quiz_questions(topic: str, num_questions: int = 5, difficulty: str = "intermediate") -> List[Dict]:
    """
    Generate quiz questions on a specific topic using OpenAI's API.
    
    Args:
        topic (str): The topic to generate questions about
        num_questions (int): Number of questions to generate
        difficulty (str): The difficulty level (beginner, intermediate, advanced)
        
    Returns:
        List[Dict]: List of quiz questions with answers and explanations
    """
    prompt = f"""
    Generate {num_questions} quiz questions about {topic} at a {difficulty} difficulty level.
    For each question, provide:
    1. The question text
    2. 4 multiple choice options (A, B, C, D)
    3. The correct answer (A, B, C, or D)
    4. A brief explanation of why the answer is correct
    
    Format the response as a JSON array of objects with the following structure:
    [
        {{
            "question": "Question text",
            "options": ["Option A", "Option B", "Option C", "Option D"],
            "correct_answer": "A",
            "explanation": "Explanation of the correct answer"
        }},
        ...
    ]
    """
    
    try:
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are an expert quiz creator with deep knowledge across many subjects."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=1500,
            response_format={"type": "json_object"}
        )
        
        # Parse the JSON response
        import json
        result = json.loads(response.choices[0].message.content)
        return result.get("questions", [])
    except Exception as e:
        return [{"error": f"Error generating quiz questions: {str(e)}"}]

def generate_practice_problems(topic: str, num_problems: int = 3, difficulty: str = "intermediate") -> List[Dict]:
    """
    Generate practice problems on a specific topic using OpenAI's API.
    
    Args:
        topic (str): The topic to generate problems about
        num_problems (int): Number of problems to generate
        difficulty (str): The difficulty level (beginner, intermediate, advanced)
        
    Returns:
        List[Dict]: List of practice problems with solutions and explanations
    """
    prompt = f"""
    Generate {num_problems} practice problems about {topic} at a {difficulty} difficulty level.
    For each problem, provide:
    1. The problem statement
    2. A step-by-step solution
    3. The final answer
    4. Key concepts tested by this problem
    
    Format the response as a JSON array of objects with the following structure:
    [
        {{
            "problem": "Problem statement",
            "solution_steps": ["Step 1", "Step 2", ...],
            "answer": "Final answer",
            "key_concepts": ["Concept 1", "Concept 2", ...]
        }},
        ...
    ]
    """
    
    try:
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are an expert problem creator with deep knowledge across many subjects."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=1500,
            response_format={"type": "json_object"}
        )
        
        # Parse the JSON response
        import json
        result = json.loads(response.choices[0].message.content)
        return result.get("problems", [])
    except Exception as e:
        return [{"error": f"Error generating practice problems: {str(e)}"}]

def provide_feedback(user_answer: str, correct_answer: str, question: str) -> Dict:
    """
    Provide detailed feedback on a user's answer using OpenAI's API.
    
    Args:
        user_answer (str): The user's answer
        correct_answer (str): The correct answer
        question (str): The question that was asked
        
    Returns:
        Dict: Feedback on the user's answer
    """
    prompt = f"""
    Question: {question}
    Correct Answer: {correct_answer}
    User's Answer: {user_answer}
    
    Provide detailed feedback on the user's answer. Include:
    1. Whether the answer is correct, partially correct, or incorrect
    2. Specific feedback on what was good about their answer
    3. Specific feedback on what could be improved
    4. A brief explanation of the correct answer
    5. Suggestions for further study
    
    Format the response as a JSON object with the following structure:
    {{
        "is_correct": true/false,
        "feedback": "Detailed feedback text",
        "improvement_suggestions": "Suggestions for improvement",
        "correct_answer_explanation": "Explanation of the correct answer",
        "further_study": "Suggestions for further study"
    }}
    """
    
    try:
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are an expert tutor providing constructive feedback."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=1000,
            response_format={"type": "json_object"}
        )
        
        # Parse the JSON response
        import json
        return json.loads(response.choices[0].message.content)
    except Exception as e:
        return {"error": f"Error providing feedback: {str(e)}"}

def generate_learning_path(topic: str, user_knowledge: str, learning_goals: str) -> Dict:
    """
    Generate a personalized learning path using OpenAI's API.
    
    Args:
        topic (str): The topic to learn about
        user_knowledge (str): Description of the user's current knowledge
        learning_goals (str): The user's learning goals
        
    Returns:
        Dict: A structured learning path
    """
    prompt = f"""
    Topic: {topic}
    User's Current Knowledge: {user_knowledge}
    Learning Goals: {learning_goals}
    
    Create a personalized learning path that will help the user achieve their learning goals.
    Include:
    1. A list of modules or sections to cover
    2. For each module:
       - Key concepts to learn
       - Learning resources (articles, videos, exercises)
       - Estimated time to complete
       - Prerequisites (if any)
    3. Milestones to track progress
    4. Assessment methods
    
    Format the response as a JSON object with the following structure:
    {{
        "overview": "Brief overview of the learning path",
        "modules": [
            {{
                "title": "Module title",
                "key_concepts": ["Concept 1", "Concept 2", ...],
                "resources": ["Resource 1", "Resource 2", ...],
                "estimated_time": "Estimated time to complete",
                "prerequisites": ["Prerequisite 1", "Prerequisite 2", ...]
            }},
            ...
        ],
        "milestones": ["Milestone 1", "Milestone 2", ...],
        "assessment_methods": ["Method 1", "Method 2", ...]
    }}
    """
    
    try:
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are an expert curriculum designer with deep knowledge across many subjects."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=2000,
            response_format={"type": "json_object"}
        )
        
        # Parse the JSON response
        import json
        return json.loads(response.choices[0].message.content)
    except Exception as e:
        return {"error": f"Error generating learning path: {str(e)}"}

def answer_user_question(question: str, context: Optional[str] = None) -> str:
    """
    Answer a user's question using OpenAI's API.
    
    Args:
        question (str): The user's question
        context (str, optional): Additional context to help answer the question
        
    Returns:
        str: Answer to the user's question
    """
    prompt = f"""
    User Question: {question}
    
    {f"Additional Context: {context}" if context else ""}
    
    Provide a clear, accurate, and helpful answer to the user's question.
    If the question is unclear, ask for clarification.
    If you don't know the answer, be honest about it.
    """
    
    try:
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a helpful and knowledgeable tutor."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=1000
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error answering question: {str(e)}" 
