def fetch_video_transcripts(topic):
    """
    Simulates fetching and processing video transcripts related to the topic.
    In a production environment, this would integrate with platforms like YouTube,
    Coursera, or educational video APIs.
    
    Args:
        topic (str): The learning topic to search for
        
    Returns:
        list: List of video transcripts with metadata and content summaries
    """
    video_results = [
        {
            "title": f"{topic} for Beginners: A Comprehensive Introduction",
            "creator": "LearnTech Academy",
            "platform": "YouTube",
            "duration": "18:24",
            "url": f"https://youtube.com/watch?v={hash(topic) % 10000000:07d}",
            "transcript_summary": f"This beginner-friendly video covers the fundamentals of {topic}. The instructor breaks down complex concepts into digestible segments with visual aids. Key sections include basic definitions, historical context, and starter examples.",
            "key_timestamps": {
                "0:00": "Introduction",
                "2:15": f"What is {topic}?",
                "5:30": "Historical Development",
                "10:45": "Basic Principles",
                "15:20": "Practical Applications"
            }
        },
        {
            "title": f"Advanced {topic} Techniques Explained",
            "creator": "Prof. Sarah Johnson",
            "platform": "Coursera",
            "duration": "42:18",
            "url": f"https://coursera.org/lecture/{topic.lower().replace(' ', '-')}/advanced-techniques",
            "transcript_summary": f"This university-level lecture delves into advanced aspects of {topic}. Professor Johnson explains complex methodologies with real-world examples from her research. The discussion includes cutting-edge developments and expert perspectives.",
            "key_timestamps": {
                "0:00": "Recap of Fundamentals",
                "4:30": "Advanced Concept Introduction",
                "12:15": "Detailed Methodology",
                "25:40": "Case Studies",
                "38:00": "Future Research Directions"
            }
        },
        {
            "title": f"{topic} in Practice: Real-World Applications",
            "creator": "Industry Insights Channel",
            "platform": "Vimeo",
            "duration": "31:05",
            "url": f"https://vimeo.com/{hash(topic) % 100000000:08d}",
            "transcript_summary": f"This practical demonstration shows {topic} being applied in various industries. Professionals share their experiences implementing {topic} solutions to real business problems.",
            "key_timestamps": {
                "0:00": "Introduction to Case Studies",
                "5:20": f"{topic} in Healthcare",
                "12:45": f"{topic} in Finance",
                "19:30": f"{topic} in Education",
                "26:15": "Implementation Tips"
            }
        },
        {
            "title": f"The Future of {topic}: Emerging Trends",
            "creator": "Tech Forward Conference",
            "platform": "TED Talks",
            "duration": "15:42",
            "url": f"https://ted.com/talks/{topic.lower().replace(' ', '_')}_future",
            "transcript_summary": f"This visionary talk explores how {topic} is likely to evolve in the next decade. The speaker discusses emerging technologies that will impact {topic} and makes predictions about future applications.",
            "key_timestamps": {
                "0:00": "Current State of the Field",
                "3:15": "Technological Drivers",
                "7:30": "Predicted Developments",
                "11:00": "Potential Challenges",
                "13:20": "Preparing for the Future"
            }
        }
    ]
    
    return video_results
