from crewai import  Crew
from agents import CourseCreatorAgents
from tasks import CourseGeneratorTasks

agents = CourseCreatorAgents()
tasks = CourseGeneratorTasks()

course_creator = agents.course_curator()
course_reasercher = agents.youtube_reasercher()

class CourseGeneratorCrew():
    def run_crew(self,units_input):
        units = [unit.strip() for unit in units_input.split(",")]  # Convert comma-separated string to list

        return  Crew(
            agents=[course_creator, course_reasercher],
            tasks=[tasks.generate_chapters_task(course_creator, units), tasks.generate_youtube_queries_task (course_reasercher)],
            verbose=True
        )

