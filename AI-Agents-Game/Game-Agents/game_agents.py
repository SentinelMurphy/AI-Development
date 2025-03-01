from crewai import Agent, LLM
import re
import streamlit as st

#waston_llm = LLM(
#    model="watsonx/meta-llama/llama-3-2-70b-instruct",
#    base_url="https://api.watsonx.ai/v1"
#)


ollama_llm = LLM(
    model="ollama/llama3.2",
    base_url="http://localhost:11434",
    temperature = 0.9
)


class GameAgents():

    def senior_engineer_agent(self):
        return Agent(
            role='Senior Software Engineer',
            goal='Create software as needed',
            backstory="""You are a Senior Software Engineer at a leading tech think tank. 
                         Your expertise in programming in python. and do your best to produce perfect code""",
            verbose=True,
            llm=ollama_llm
        )

    def qa_engineer_agent(self):
        return Agent(
            role='Software Quality Control Engineer',
            goal='Create Perfect code, by analyzing the code that is given for errors',
            backstory="""You are a software engineer that specializes in checking code
                        for errors. You have an eye for detail and a knack for finding
                        hidden bugs.You check for missing imports, variable declarations, 
                        mismatched brackets and syntax errors.
                        You also check for security vulnerabilities, and logic errors""",
            verbose=True,
            llm=ollama_llm
        )

    def chief_qa_engineer_agent(self):
        return Agent(
            role='Chief Software Quality Control Engineer',
            goal="""Ensure that the code does the job that it is supposed to do""",
            backstory="""You feel that programmers always do only half the job, so you are
                         super dedicate to make high quality code.""",
            verbose=True,
            llm=ollama_llm
        )

class StreamToExpander:
    def __init__(self, expander):
        self.expander = expander
        self.buffer = []
        self.colors = ['red', 'green', 'blue', 'orange']  # Define a list of colors
        self.color_index = 0  # Initialize color index

    def write(self, data):
        # Filter out ANSI escape codes using a regular expression
        cleaned_data = re.sub(r'\x1B\[[0-9;]*[mK]', '', data)

        # Check if the data contains 'task' information
        task_match_object = re.search(r'\"task\"\s*:\s*\"(.*?)\"', cleaned_data, re.IGNORECASE)
        task_match_input = re.search(r'task\s*:\s*([^\n]*)', cleaned_data, re.IGNORECASE)
        task_value = None
        if task_match_object:
            task_value = task_match_object.group(1)
        elif task_match_input:
            task_value = task_match_input.group(1).strip()

        if task_value:
            st.toast(":robot_face: " + task_value)


        # Check if the text contains the specified phrase and apply color
        if "Entering new CrewAgentExecutor chain" in cleaned_data:
            print('Set Color : ',self.colors)
            self.color_index = (self.color_index + 1) % len(self.colors)  # Increment color index and wrap around if necessary

            cleaned_data = cleaned_data.replace("Entering new CrewAgentExecutor chain", f":{self.colors[self.color_index]}[Entering new CrewAgentExecutor chain]")

        if "Senior Engineer Agent" in cleaned_data:
            # Apply different color
            cleaned_data = cleaned_data.replace("Senior Engineer Agent", f":{self.colors[self.color_index]}[Code Engineer Expert]")
        if "QA Engineer Agent" in cleaned_data:
            cleaned_data = cleaned_data.replace("QA Engineer Agent", f":{self.colors[self.color_index]}[Software Quality Expert]")
        if "Chief AQ Engineer Agent" in cleaned_data:
            cleaned_data = cleaned_data.replace("Chief AQ Engineer Agent", f":{self.colors[self.color_index]}[Chef Software Quality Expert]")
        if "Finished chain." in cleaned_data:
            cleaned_data = cleaned_data.replace("Finished chain.", f":{self.colors[self.color_index]}[Finished chain.]")

        self.buffer.append(cleaned_data)
        if "\n" in data:
            self.expander.markdown(''.join(self.buffer), unsafe_allow_html=True)
            self.buffer = []