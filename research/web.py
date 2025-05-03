import requests
from bs4 import BeautifulSoup
import wikipedia
import os
from typing import Dict, List, Optional

def is_tech_topic(topic):
    """
    Check if the topic is related to software/computer science.
    """
    tech_keywords = [
        'programming', 'python', 'java', 'javascript', 'html', 'css', 'sql',
        'database', 'web development', 'coding', 'software', 'computer science',
        'api', 'react', 'angular', 'vue', 'node', 'php', 'C langunage','C programming', 'ruby', 'c++', 'c#',
        'django', 'flask', 'bootstrap', 'jquery', 'mongodb', 'mysql', 'postgresql',
        'algorithm', 'data structure', 'cyber security', 'networking', 'linux',
        'git', 'docker', 'kubernetes', 'aws', 'cloud computing', 'machine learning'
    ]
    return any(keyword in topic.lower() for keyword in tech_keywords)

def fetch_wikipedia_content(topic: str) -> Optional[Dict]:
    """
    Fetch content from Wikipedia for the given topic.
    
    Args:
        topic (str): The topic to search for
        
    Returns:
        Optional[Dict]: Dictionary containing Wikipedia content or None if not found
    """
    try:
        # Search for the topic
        search_results = wikipedia.search(topic)
        if not search_results:
            return None
            
        # Get the first result
        page = wikipedia.page(search_results[0])
        
        # Get a summary of the content
        summary = wikipedia.summary(search_results[0], sentences=3)
        
        return {
            "title": page.title,
            "source": "Wikipedia",
            "summary": summary,
            "url": page.url,
            "content": page.content[:1000]  # First 1000 characters of content
        }
    except wikipedia.exceptions.DisambiguationError as e:
        # If there are multiple matches, use the first one
        page = wikipedia.page(e.options[0])
        summary = wikipedia.summary(e.options[0], sentences=3)
        return {
            "title": page.title,
            "source": "Wikipedia",
            "summary": summary,
            "url": page.url,
            "content": page.content[:1000]
        }
    except Exception as e:
        print(f"Error fetching Wikipedia content: {e}")
        return None

def fetch_web_content(topic: str) -> List[Dict]:
    """
    Fetch and process web content related to the given topic.
    
    Args:
        topic (str): The topic to search for
        
    Returns:
        List[Dict]: List of dictionaries containing processed web content
    """
    results = []
    
    # Fetch Wikipedia content
    wiki_content = fetch_wikipedia_content(topic)
    if wiki_content:
        results.append(wiki_content)
    
    # Add tech-specific resources if it's a tech topic
    if is_tech_topic(topic):
        tech_resources = [
            {
                "title": f"{topic} - GeeksforGeeks",
                "source": "GeeksforGeeks",
                "summary": f"Comprehensive tutorials and articles about {topic}",
                "url": f"https://www.geeksforgeeks.org/search/?q={topic.replace(' ', '+')}"
            },
            {
                "title": f"{topic} Tutorial",
                "source": "Javatpoint",
                "summary": f"Detailed tutorials and examples for {topic}",
                "url": f"https://www.javatpoint.com/search?q={topic.replace(' ', '+')}"
            },
            {
                "title": f"{topic} - W3Schools",
                "source": "W3Schools",
                "summary": f"Interactive tutorials and examples for {topic}",
                "url": f"https://www.w3schools.com/search/?q={topic.replace(' ', '+')}"
            },
            {
                "title": f"{topic} - TutorialsPoint",
                "source": "TutorialsPoint",
                "summary": f"Free tutorials and reference materials for {topic}",
                "url": f"https://www.tutorialspoint.com/search?q={topic.replace(' ', '+')}"
            },
            {
                "title": f"{topic} - freeCodeCamp",
                "source": "freeCodeCamp",
                "summary": f"Free coding tutorials and projects for {topic}",
                "url": f"https://www.freecodecamp.org/search/?query={topic.replace(' ', '+')}"
            }
        ]
        results.extend(tech_resources)
    
    # Add math and science resources
    math_science_keywords = ['math', 'mathematics', 'physics', 'chemistry', 'biology', 'science']
    if any(keyword in topic.lower() for keyword in math_science_keywords):
        math_science_resources = [
            {
                "title": f"{topic} - BYJU'S",
                "source": "BYJU'S",
                "summary": f"Interactive learning materials and video lessons for {topic}",
                "url": f"https://byjus.com/search/?q={topic.replace(' ', '+')}"
            }
        ]
        results.extend(math_science_resources)
    
    return results

def fetch_video_transcripts(topic):
    """
    Provides curated video resources for the topic.
    """
    search_topic = topic.replace(' ', '+')
    
    videos = [
        {
            "title": f"{topic} - Complete Tutorial for Beginners",
            "creator": "Educational Platforms",
            "platform": "YouTube",
            "duration": "Various",
            "transcript_summary": "Comprehensive beginner-friendly tutorials",
            "key_timestamps": {
                "Basics": "Fundamental concepts",
                "Practice": "Hands-on exercises",
                "Examples": "Real-world applications"
            },
            "url": f"https://www.youtube.com/results?search_query={search_topic}+complete+tutorial+for+beginners"
        }
    ]
    
    # Add tech-specific video resources
    if is_tech_topic(topic):
        videos.extend([
            {
                "title": f"{topic} - Coding Tutorial",
                "creator": "Programming Channels",
                "platform": "YouTube",
                "duration": "Various",
                "transcript_summary": "Hands-on coding tutorials and examples",
                "key_timestamps": {
                    "Setup": "Environment setup",
                    "Coding": "Live coding examples",
                    "Projects": "Project implementation"
                },
                "url": f"https://www.youtube.com/results?search_query={search_topic}+coding+tutorial+programming"
            },
            {
                "title": f"{topic} Project Tutorial",
                "creator": "Dev Channels",
                "platform": "YouTube",
                "duration": "Various",
                "transcript_summary": "Build real projects step by step",
                "key_timestamps": {
                    "Planning": "Project planning",
                    "Implementation": "Step-by-step coding",
                    "Deployment": "Deployment guide"
                },
                "url": f"https://www.youtube.com/results?search_query={search_topic}+project+tutorial+build"
            }
        ])
    
    return videos

def get_premium_course_suggestions(topic: str) -> List[Dict]:
    """
    Get suggestions for premium courses on the topic.
    
    Args:
        topic (str): The topic to search for
        
    Returns:
        List[Dict]: List of dictionaries containing premium course suggestions
    """
    premium_courses = [
        {
            "title": f"{topic} - Udemy",
            "source": "Udemy",
            "summary": f"Comprehensive paid courses for {topic} with lifetime access",
            "url": f"https://www.udemy.com/courses/search/?q={topic.replace(' ', '+')}"
        },
        {
            "title": f"{topic} - Coursera",
            "source": "Coursera",
            "summary": f"Professional courses and certifications for {topic}",
            "url": f"https://www.coursera.org/search?query={topic.replace(' ', '+')}"
        }
    ]
    return premium_courses
