from crewai import Agent,LLM
from crewai_tools import SerperDevTool,YoutubeVideoSearchTool

# Tool for YouTube search (Use Serper.dev for Google searches or replace with YouTube API)
youtube_search_tool = YoutubeVideoSearchTool(
    config=dict(
        llm=dict(
            provider="ollama", # or google, openai, anthropic, llama2, ...
            config=dict(
                model="llama3.2",
                #temperature=0.5,
                # top_p=1,
                #stream=True,
            ),
        ),
        embedder=dict(
            provider="ollama", # or openai, ollama, ...
            config=dict(
                model="nomic-embed-text",
                #task_type="retrieval_document",
                #title="Embeddings",
            ),
        )
    )
)

# === LLM ===
llm = LLM(
    model="ollama/llama3.2",
    base_url="http://localhost:11434",
)


class CourseCreatorAgents():
   def course_curator(self):
        # Agent to generate chapters based on units
        return Agent(
            llm=llm,
            name="Course Curator",
            role="Course Content Curator",
            goal="Generate well-structured chapters for each unit in the course",
            backstory="An expert in educational content creation, skilled at structuring courses with engaging chapters.",
            verbose=True,
            #allow_delegation=True
        )
  
   def youtube_reasercher(self):
       # Agent to find YouTube videos for each chapter
       return Agent(
            llm=llm,
            name="YouTube Researcher",
            role="Educational Video Finder",
            goal="Find the best educational videos for each chapter",
            backstory="A specialist in discovering high-quality educational content on YouTube.",
            verbose=True,
            tools=[youtube_search_tool]  # Assigning the YouTube search tool
        )