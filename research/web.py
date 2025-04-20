import requests
from bs4 import BeautifulSoup
import wikipedia
from googleapiclient.discovery import build
import os

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

def fetch_web_content(topic):
    """
    Fetches web content related to the specified topic.
    """
    results = []
    
    # Add W3Schools first for tech topics
    if is_tech_topic(topic):
        # Format topic for W3Schools URL
        w3_topic = topic.lower().replace(' ', '')
        w3_url = f"https://www.w3schools.com/{w3_topic}"
        
        results.append({
            "title": f"W3Schools Tutorial: {topic}",
            "source": "W3Schools",
            "summary": f"Interactive tutorials, references, and examples for {topic}. Includes practical exercises and certifications.",
            "url": w3_url
        })
        
        # MDN Web Docs for web development topics
        if any(keyword in topic.lower() for keyword in ['web', 'html', 'css', 'javascript', 'js', 'api']):
            mdn_topic = topic.lower().replace(' ', '-')
            results.append({
                "title": f"MDN Web Docs: {topic}",
                "source": "Mozilla Developer Network",
                "summary": f"Comprehensive documentation and guides for {topic} from Mozilla.",
                "url": f"https://developer.mozilla.org/en-US/docs/Web/{mdn_topic}"
            })

    # Wikipedia summary
    try:
        wiki_content = wikipedia.summary(topic, sentences=3)
        wiki_page = wikipedia.page(topic)
        results.append({
            "title": f"Wikipedia: {topic}",
            "source": "Wikipedia",
            "summary": wiki_content,
            "url": wiki_page.url
        })
    except:
        pass

    # GeeksforGeeks for programming topics
    if is_tech_topic(topic):
        geeks_topic = topic.lower().replace(' ', '-')
        results.append({
            "title": f"GeeksforGeeks: {topic}",
            "source": "GeeksforGeeks",
            "summary": f"Programming tutorials, algorithms, and practice problems for {topic}",
            "url": f"https://www.geeksforgeeks.org/{geeks_topic}"
        })

    # Khan Academy search
    khan_url = f"https://www.khanacademy.org/search?search_again=1&page_search_query={topic.replace(' ', '+')}"
    results.append({
        "title": f"Khan Academy Resources for {topic}",
        "source": "Khan Academy",
        "summary": f"Interactive lessons and practice exercises on {topic}",
        "url": khan_url
    })

    # Coursera search
    coursera_url = f"https://www.coursera.org/search?query={topic.replace(' ', '+')}"
    results.append({
        "title": f"Online Courses on {topic}",
        "source": "Coursera",
        "summary": f"Professional courses and certifications related to {topic}",
        "url": coursera_url
    })

    # GitHub resources for tech topics
    if is_tech_topic(topic):
        github_url = f"https://github.com/search?q={topic.replace(' ', '+')}&type=repositories"
        results.append({
            "title": f"GitHub Projects: {topic}",
            "source": "GitHub",
            "summary": f"Open source projects, examples, and learning resources for {topic}",
            "url": github_url
        })

    # Stack Overflow for tech topics
    if is_tech_topic(topic):
        stackoverflow_url = f"https://stackoverflow.com/questions/tagged/{topic.replace(' ', '-')}"
        results.append({
            "title": f"Stack Overflow: {topic}",
            "source": "Stack Overflow",
            "summary": f"Questions, answers, and discussions about {topic} from the developer community",
            "url": stackoverflow_url
        })

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
