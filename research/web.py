import requests
from bs4 import BeautifulSoup
import wikipedia
from googleapiclient.discovery import build
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

def fetch_web_content(topic: str) -> List[Dict]:
    """
    Fetch and process web content related to the given topic.
    
    Args:
        topic (str): The topic to search for
        
    Returns:
        List[Dict]: List of dictionaries containing processed web content
    """
    # This is a placeholder implementation
    # In a real implementation, you would:
    # 1. Use a search API to find relevant pages
    # 2. Fetch and parse the content
    # 3. Process and summarize the content
    
    sample_results = [
        {
            "title": f"Understanding {topic}",
            "source": "example.com",
            "summary": f"A comprehensive guide to {topic} covering basic concepts and advanced applications.",
            "url": "https://example.com/article1"
        },
        {
            "title": f"{topic} for Beginners",
            "source": "tutorial.com",
            "summary": f"Step-by-step introduction to {topic} with practical examples.",
            "url": "https://tutorial.com/basics"
        }
    ]
    
    return sample_results

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
