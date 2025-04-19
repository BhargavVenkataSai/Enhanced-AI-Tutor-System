import random
import time
from datetime import datetime

def generate_report(topic, objective, preferences, web_results, academic_results, video_results):
    """
    Generates a comprehensive, structured educational report based on gathered research
    and user preferences.
    
    Args:
        topic (str): The learning topic
        objective (str): User's learning objectives
        preferences (dict): User's learning preferences and interests
        web_results (list): Web content research results
        academic_results (list): Academic research results
        video_results (list): Video transcript research results
        
    Returns:
        str: Formatted report in Markdown
    """
    # Generate a unique report ID for reference
    report_id = f"LR-{int(time.time())}"
    now = datetime.now().strftime("%Y-%m-%d %H:%M")
    
    # Start building the report with a header
    report = f"""
# 📚 Personalized Learning Report: {topic}

**Report ID:** {report_id}  
**Generated on:** {now}  
**Topic:** {topic}

## 🎯 Learning Objectives
{objective}

## 👤 Personalized Learning Profile
"""

    # Add user preferences to the report
    if isinstance(preferences, dict):
        for key, value in preferences.items():
            formatted_key = key.replace('_', ' ').title()
            report += f"- **{formatted_key}:** {value}\n"
    
    # Executive Summary section
    report += """
## 📋 Executive Summary

"""
    # Generate a simulated executive summary
    report += f"""This personalized learning guide on *{topic}* is designed to align with your specific learning objectives and preferences. Based on extensive research from academic sources, web content, and educational videos, this report provides a structured learning path from fundamental concepts to advanced applications.

The material is organized to accommodate your indicated knowledge level and preferred learning style, with emphasis on {'practical examples' if 'practical' in str(preferences).lower() else 'theoretical foundations'} as requested. Key concepts are explained using {'visual aids' if 'visual' in str(preferences).lower() else 'detailed descriptions'}, and the progression follows a logical flow to build understanding incrementally.

This report includes curated resources from {'academic literature' if 'academic' in str(preferences).lower() else 'practical tutorials'} and {'video content' if 'video' in str(preferences).lower() else 'text-based resources'} based on your preferences, with recommended activities to reinforce learning.
"""

    # Table of Contents
    report += """
## 📑 Table of Contents
1. [Introduction to {0}](#introduction)
2. [Core Concepts and Principles](#core-concepts)
3. [Detailed Knowledge Areas](#detailed-knowledge)
4. [Practical Applications](#practical-applications)
5. [Advanced Topics](#advanced-topics)
6. [Learning Activities](#learning-activities)
7. [Recommended Resources](#recommended-resources)
8. [References and Citations](#references)
""".format(topic)

    # Introduction Section
    report += f"""
## 1️⃣ Introduction to {topic} <a name="introduction"></a>

"""
    # Select content from web results for introduction
    if web_results and len(web_results) > 0 and isinstance(web_results[0], dict):
        intro_content = next((item for item in web_results if "fundamentals" in item["title"].lower() or "introduction" in item["title"].lower()), web_results[0])
        report += f"{intro_content['summary']}\n\n"
        report += f"*Source: [{intro_content['title']}]({intro_content['url']})*\n\n"
    else:
        report += f"An introduction to {topic} covering the basic definitions, key concepts, and historical context.\n\n"

    # Visualization placeholder
    report += f"""
### Visual Overview: {topic} Concept Map

```
+------------------+        +------------------+        +------------------+
|                  |        |                  |        |                  |
| Foundational     |------->| Key              |------->| Advanced         |
| Concepts         |        | Applications     |        | Topics           |
|                  |        |                  |        |                  |
+------------------+        +------------------+        +------------------+
         |                           |                           |
         v                           v                           v
+------------------+        +------------------+        +------------------+
|                  |        |                  |        |                  |
| Historical       |        | Current          |        | Future           |
| Development      |        | Practices        |        | Directions       |
|                  |        |                  |        |                  |
+------------------+        +------------------+        +------------------+
```

"""

    # Core Concepts section
    report += f"""
## 2️⃣ Core Concepts and Principles <a name="core-concepts"></a>

The following core concepts form the foundation of {topic}:

"""
    # Include academic content for core concepts
    if academic_results and len(academic_results) > 0 and isinstance(academic_results[0], dict):
        theoretical_paper = next((item for item in academic_results if "theoretical" in item["title"].lower() or "foundations" in item["title"].lower()), academic_results[0])
        report += f"According to {theoretical_paper['authors']} ({theoretical_paper['year']}), the theoretical foundations of {topic} include the following key principles:\n\n"
        report += f"{theoretical_paper['summary']}\n\n"
        
        # Add a simulated list of core concepts
        core_concepts = [
            f"**Foundational Principle 1**: A primary concept within {topic} that establishes the basic framework.",
            f"**Underlying Methodology**: The systematic approach used in {topic} to address problems in the field.",
            f"**Conceptual Framework**: The theoretical structure that organizes the various elements of {topic}.",
            f"**Key Relationships**: How different aspects of {topic} interact and influence each other."
        ]
        
        for concept in core_concepts:
            report += f"- {concept}\n"
            
        report += f"\n*Source: [{theoretical_paper['title']}] {theoretical_paper['journal']}, {theoretical_paper['year']}. DOI: {theoretical_paper['doi']}*\n\n"
    else:
        report += f"This section would outline the core theoretical principles and concepts that form the foundation of {topic}.\n\n"

    # Detailed Knowledge Areas section
    report += f"""
## 3️⃣ Detailed Knowledge Areas <a name="detailed-knowledge"></a>

Based on current research and educational materials, {topic} encompasses several key knowledge areas:

"""
    # Create simulated knowledge areas with content from our sources
    knowledge_areas = [
        {
            "title": f"Historical Development of {topic}",
            "content": f"This area explores how {topic} has evolved over time, from its origins to current state."
        },
        {
            "title": f"Methodological Approaches in {topic}",
            "content": f"This area covers the various methodologies and approaches used in {topic}, including their strengths and limitations."
        },
        {
            "title": f"Theoretical Frameworks in {topic}",
            "content": f"This area examines the theoretical underpinnings that guide work in {topic}."
        },
        {
            "title": f"Tools and Technologies in {topic}",
            "content": f"This area focuses on the practical tools, technologies, and resources commonly used in {topic}."
        }
    ]
    
    for i, area in enumerate(knowledge_areas):
        report += f"### 3.{i+1} {area['title']}\n\n"
        report += f"{area['content']}\n\n"
        
        # Add some simulated content from our research sources
        if web_results and len(web_results) > 0 and isinstance(web_results[0], dict):
            web_item = web_results[i % len(web_results)]
            report += f"From web resources: {web_item['summary']}\n\n"
            
        if i < 2 and video_results and len(video_results) > 0 and isinstance(video_results[0], dict):
            video_item = video_results[i % len(video_results)]
            report += f"**Video Insight:** {video_item['transcript_summary']}\n\n"
            report += f"*Source: [{video_item['title']}]({video_item['url']}) by {video_item['creator']} on {video_item['platform']}*\n\n"
            
            # Add key timestamps from the video
            report += "**Key video segments:**\n\n"
            for timestamp, description in list(video_item['key_timestamps'].items())[:3]:
                report += f"- [{timestamp}] {description}\n"
            report += "\n"

    # Practical Applications section
    report += f"""
## 4️⃣ Practical Applications <a name="practical-applications"></a>

{topic} has numerous practical applications across various fields:

"""
    # Add practical applications from our sources
    if web_results and len(web_results) > 0 and isinstance(web_results[0], dict):
        practical_article = next((item for item in web_results if "practical" in item["title"].lower() or "applications" in item["title"].lower()), None)
        if practical_article:
            report += f"{practical_article['summary']}\n\n"
            report += f"*Source: [{practical_article['title']}]({practical_article['url']})*\n\n"
    
    # Add case studies
    report += f"""
### Case Studies

1. **Case Study 1: {topic} in Healthcare**
   - Challenge: [Description of a problem in healthcare]
   - Solution: [How {topic} was applied]
   - Results: [Outcomes and benefits]

2. **Case Study 2: {topic} in Education**
   - Challenge: [Description of a problem in education]
   - Solution: [How {topic} was applied]
   - Results: [Outcomes and benefits]

3. **Case Study 3: {topic} in Business**
   - Challenge: [Description of a problem in business]
   - Solution: [How {topic} was applied]
   - Results: [Outcomes and benefits]

"""

    # Advanced Topics section
    report += f"""
## 5️⃣ Advanced Topics <a name="advanced-topics"></a>

For learners seeking deeper knowledge, these advanced topics represent the cutting edge of {topic}:

"""
    # Add advanced topics from academic sources
    if academic_results and len(academic_results) > 0 and isinstance(academic_results[0], dict):
        advanced_paper = next((item for item in academic_results if "advanced" in item["title"].lower() or "emerging" in item["title"].lower()), None)
        if advanced_paper:
            report += f"According to research by {advanced_paper['authors']} ({advanced_paper['year']}), emerging trends in {topic} include:\n\n"
            report += f"{advanced_paper['summary']}\n\n"
            
            if 'keywords' in advanced_paper:
                report += "**Keywords:** " + ", ".join(advanced_paper['keywords']) + "\n\n"
                
            report += f"*Source: [{advanced_paper['title']}] {advanced_paper['journal']}, {advanced_paper['year']}. DOI: {advanced_paper['doi']}*\n\n"
    
    # Add future directions
    if video_results and len(video_results) > 0 and isinstance(video_results[0], dict):
        future_video = next((item for item in video_results if "future" in item["title"].lower() or "emerging" in item["title"].lower()), None)
        if future_video:
            report += f"**Future Directions:** {future_video['transcript_summary']}\n\n"
            report += f"*Source: [{future_video['title']}]({future_video['url']}) by {future_video['creator']}*\n\n"

    # Learning Activities section
    report += f"""
## 6️⃣ Learning Activities <a name="learning-activities"></a>

To reinforce your understanding of {topic}, consider the following activities:

1. **Reflection Questions**
   - How does {topic} relate to your existing knowledge or experience?
   - What aspects of {topic} do you find most challenging to understand?
   - How might you apply {topic} in your specific context?

2. **Practical Exercises**
   - Exercise 1: [Description of a hands-on exercise related to {topic}]
   - Exercise 2: [Description of another practical activity]
   - Exercise 3: [Description of a more advanced application exercise]

3. **Discussion Topics**
   - Topic 1: [A controversial or evolving aspect of {topic} to consider]
   - Topic 2: [Ethical considerations related to {topic}]
   - Topic 3: [Future implications of {topic} in society]

"""

    # Recommended Resources section
    report += f"""
## 7️⃣ Recommended Resources <a name="recommended-resources"></a>

Based on your learning preferences and objectives, here are curated resources to deepen your knowledge:

### Books and Articles
"""
    
    # Add web resources
    if web_results and len(web_results) > 0 and isinstance(web_results[0], dict):
        for i, resource in enumerate(web_results[:3]):
            report += f"{i+1}. [{resource['title']}]({resource['url']}) - {resource['source']}\n"
            report += f"   *{resource['summary']}*\n\n"
    
    report += f"""
### Video Resources
"""
    
    # Add video resources
    if video_results and len(video_results) > 0 and isinstance(video_results[0], dict):
        for i, resource in enumerate(video_results[:3]):
            report += f"{i+1}. [{resource['title']}]({resource['url']}) ({resource['duration']}) - {resource['creator']}\n"
            report += f"   *{resource['transcript_summary']}*\n\n"
    
    report += f"""
### Academic Papers
"""
    
    # Add academic resources
    if academic_results and len(academic_results) > 0 and isinstance(academic_results[0], dict):
        for i, resource in enumerate(academic_results[:3]):
            report += f"{i+1}. {resource['authors']} ({resource['year']}). *{resource['title']}*. {resource['journal']}. DOI: {resource['doi']}\n"
            report += f"   *{resource['summary']}*\n\n"
    
    # References and Citations section
    report += f"""
## 8️⃣ References and Citations <a name="references"></a>

"""
    
    # Add all sources as references
    if web_results and len(web_results) > 0 and isinstance(web_results[0], dict):
        report += "### Web Resources\n\n"
        for i, resource in enumerate(web_results):
            report += f"{i+1}. {resource['source']} ({datetime.now().year}). \"{resource['title']}\". Retrieved from {resource['url']}\n\n"
    
    if academic_results and len(academic_results) > 0 and isinstance(academic_results[0], dict):
        report += "### Academic Sources\n\n"
        for i, resource in enumerate(academic_results):
            report += f"{i+1}. {resource['authors']} ({resource['year']}). {resource['title']}. *{resource['journal']}*. DOI: {resource['doi']}\n\n"
    
    if video_results and len(video_results) > 0 and isinstance(video_results[0], dict):
        report += "### Video Sources\n\n"
        for i, resource in enumerate(video_results):
            report += f"{i+1}. {resource['creator']} ({datetime.now().year}). \"{resource['title']}\". {resource['platform']}. Retrieved from {resource['url']}\n\n"
    
    # Feedback section
    report += f"""
---

## Feedback and Modifications

This report can be modified based on your feedback. If you'd like adjustments to any section or have follow-up questions, please provide your feedback to generate an updated version.

Report ID: {report_id} | Generated on: {now}
"""
    
    return report
