from crewai import Task
from crewai_tools import SerperDevTool

# Tool for YouTube search (Use Serper.dev for Google searches or replace with YouTube API)
youtube_search_tool = SerperDevTool()

class CourseGeneratorTasks():
    def generate_chapters_task(self,agent,units):
        return Task(
            description=(
                "It is your job to create a course about {title}. "
                f"The user has requested to create chapters for each of the following units: {', '.join(units)}."
            ),
            agent=agent,
            expected_output=(
                "A structured list of chapters relevant to the provided course units. follow the format given below  as example dont use any other format "
                """
                Example output

                Unit 1: Introduction to AI
                    Chapter 1:  What is Artificial Intelligence?
                    Chapter 2: History of AI
                unit 2: Machine Learning
                    Chapter 1: Introduction to Machine Learning
                    Chapter 2: Supervised Learning

                """
                
                )
        )
     
    def generate_youtube_queries_task(self,agent):
        # Task for generating YouTube search queries for each chapter
        return Task(
            description=(
                    "For each chapter in the course '{title}', provide a detailed YouTube search query "
                    "that can be used to find an informative educational video for each chapter. "
                    "Each query should return an educational course on YouTube."
                    ""
            ),
            agent=agent,
            expected_output=(
                "A JSON object where unit has list of chapters and each chapter has a 'chapter_title' , 'youtube_search_query' and 'video_url'"
                "follow the format given below  as example don't use any other format but JSON"
    
               
               
                "Example output"
                """
                unit 1: 
                    usint_title: Introduction to AI
                    Chapter 1:  What is Artificial Intelligence?
                        chapter_title : Defining AI
                        youtube_search_query: Build & Deploy: Full Stack AI Course
                        video_url: https://www.youtube.com/watch?v=EGW2HS2tqAQ&t=889s
                    Chapter 2: History of AI
                        chapter_title : Build & Deploy: Full Stack AI Course
                        youtube_search_query: Build & Deploy: Full Stack AI Course
                        video_url: https://www.youtube.com/watch?v=EGW2HS2tqAQ&t=889s
                 unit 2: 
                    unit_title: Machine Learning
                    Chapter 1: Introduction to Machine Learning
                        chapter_title : Types of ML (Supervised, Unsupervised, Reinforcement)
                        youtube_search_query: Build & Deploy: Full Stack AI Course
                        video_url: https://www.youtube.com/watch?v=EGW2HS2tqAQ&t=889s
                    Chapter 2: Supervised Learning
                        chapter_title : Classification techniques
                        youtube_search_query: Build & Deploy: Full Stack AI Course
                        video_url: https://www.youtube.com/watch?v=EGW2HS2tqAQ&t=889s
                
                """
            
                )
        )


