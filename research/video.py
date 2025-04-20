def fetch_video_transcripts(topic):
    """
    Provides video resources with working YouTube search links.
    """
    # Create search-friendly version of the topic
    search_topic = topic.replace(' ', '+')
    
    video_results = [
        {
            "title": f"{topic} for Beginners: A Comprehensive Introduction",
            "creator": "Various Educational Channels",
            "platform": "YouTube",
            "duration": "Various",
            "url": f"https://www.youtube.com/results?search_query={search_topic}+beginner+tutorial",
            "transcript_summary": f"Find beginner-friendly tutorials about {topic}. These videos cover fundamentals, basic concepts, and introductory examples.",
            "key_timestamps": {
                "Beginner": "Basic concepts and fundamentals",
                "Examples": "Practical demonstrations",
                "Practice": "Hands-on exercises"
            }
        },
        {
            "title": f"Advanced {topic} Techniques",
            "creator": "Various Expert Instructors",
            "platform": "YouTube",
            "duration": "Various",
            "url": f"https://www.youtube.com/results?search_query={search_topic}+advanced+tutorial",
            "transcript_summary": f"Discover advanced tutorials and in-depth explanations of {topic}.",
            "key_timestamps": {
                "Advanced": "Complex concepts and techniques",
                "Examples": "Advanced applications",
                "Practice": "Expert-level exercises"
            }
        },
        {
            "title": f"{topic} in Practice: Real-World Applications",
            "creator": "Industry Professionals",
            "platform": "YouTube",
            "duration": "Various",
            "url": f"https://www.youtube.com/results?search_query={search_topic}+real+world+applications",
            "transcript_summary": f"Learn how {topic} is applied in real-world scenarios and industries.",
            "key_timestamps": {
                "Applications": "Practical implementations",
                "Case Studies": "Real-world examples",
                "Industry": "Professional applications"
            }
        },
        {
            "title": f"Latest Developments in {topic}",
            "creator": "Educational Channels",
            "platform": "YouTube",
            "duration": "Various",
            "url": f"https://www.youtube.com/results?search_query={search_topic}+latest+developments",
            "transcript_summary": f"Stay updated with the latest trends and developments in {topic}.",
            "key_timestamps": {
                "Updates": "Recent developments",
                "Trends": "Current directions",
                "Future": "Upcoming changes"
            }
        }
    ]
    
    return video_results
