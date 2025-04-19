def ask_questions(topic=None):
    """
    Generates interactive questions to personalize the learning experience.
    
    Args:
        topic (str, optional): The learning topic to customize questions
        
    Returns:
        dict: Dictionary of questions categorized by purpose
    """
    # Questions to understand user's knowledge level
    knowledge_questions = [
        {
            "id": "knowledge_level",
            "question": f"How would you rate your current knowledge of {topic if topic else 'this topic'}?",
            "options": ["Beginner - little to no knowledge", "Intermediate - some basic understanding", "Advanced - solid understanding but want to deepen knowledge", "Expert - looking for very specific advanced information"],
            "type": "single_select"
        },
        {
            "id": "previous_experience",
            "question": f"Have you studied or worked with {topic if topic else 'this topic'} before?",
            "options": ["No previous experience", "Self-study only", "Academic coursework", "Professional experience"],
            "type": "single_select"
        },
        {
            "id": "specific_concepts",
            "question": f"Are there specific concepts within {topic if topic else 'this topic'} you're already familiar with?",
            "placeholder": "E.g., basic principles, specific methodologies, etc.",
            "type": "text_input"
        }
    ]
    
    # Questions to understand learning preferences
    learning_preferences = [
        {
            "id": "learning_style",
            "question": "How do you prefer to learn new material?",
            "options": ["Visual (diagrams, charts, videos)", "Reading (articles, books)", "Interactive (exercises, quizzes)", "Mixed approach"],
            "type": "single_select"
        },
        {
            "id": "content_depth",
            "question": "What depth of content are you looking for?",
            "options": ["Broad overview", "Moderate depth with key details", "In-depth with technical specifics", "Comprehensive expert-level"],
            "type": "single_select"
        },
        {
            "id": "session_duration",
            "question": "How much time can you dedicate to learning per session?",
            "options": ["Under 30 minutes", "30-60 minutes", "1-2 hours", "More than 2 hours"],
            "type": "single_select"
        },
        {
            "id": "learning_frequency",
            "question": "How frequently do you plan to engage with this material?",
            "options": ["Daily", "Several times per week", "Weekly", "Less frequently"],
            "type": "single_select"
        }
    ]
    
    # Questions to understand specific interests
    interest_questions = [
        {
            "id": "primary_goal",
            "question": f"What is your primary goal for learning about {topic if topic else 'this topic'}?",
            "options": ["Academic requirements", "Professional development", "Personal interest", "Solving a specific problem"],
            "type": "single_select"
        },
        {
            "id": "application_focus",
            "question": "Do you prefer theoretical understanding or practical applications?",
            "options": ["Heavily theoretical", "Mostly theoretical with some applications", "Balanced", "Mostly practical with supporting theory", "Purely practical and applied"],
            "type": "single_select"
        },
        {
            "id": "specific_interests",
            "question": f"What specific aspects of {topic if topic else 'this topic'} are you most interested in?",
            "placeholder": "Enter specific areas of interest",
            "type": "text_input"
        }
    ]
    
    # Questions about preferred output format
    output_preferences = [
        {
            "id": "preferred_resources",
            "question": "What types of resources do you find most helpful?",
            "options": ["Video tutorials", "Academic papers", "Written guides/tutorials", "Interactive exercises", "Case studies", "Code examples"],
            "type": "multi_select"
        },
        {
            "id": "format_preference",
            "question": "How would you like the learning material structured?",
            "options": ["Linear progression (step-by-step)", "Concept map (interconnected ideas)", "Problem-based (learning through examples)", "Reference style (organized by topic)"],
            "type": "single_select"
        },
        {
            "id": "visual_aids",
            "question": "How important are visual elements (diagrams, charts, etc.) to your learning?",
            "options": ["Essential", "Very helpful", "Somewhat helpful", "Not important"],
            "type": "single_select"
        }
    ]
    
    return {
        "knowledge_assessment": knowledge_questions,
        "learning_preferences": learning_preferences,
        "interests": interest_questions,
        "output_preferences": output_preferences
    }
