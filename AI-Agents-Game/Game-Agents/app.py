from game_agents import GameAgents, StreamToExpander
from game_tasks import GameTasks
import streamlit as st
import yaml
import sys
from crewai import Crew, Process

st.set_page_config(page_icon="🎮", layout="wide")


def icon(emoji: str):
    """Shows an emoji as a Notion-style page icon."""
    st.write(
        f'<span style="font-size: 78px; line-height: 1">{emoji}</span>',
        unsafe_allow_html=True,
    )


class GameCrew:

    def __init__(self, game, description, mechanics):
        # Not used right now just for display
        self.game = game
        self.description = description
        self.mechanics = mechanics
        self.output_placeholder = st.empty()

    def run(self):
        agents = GameAgents()
        tasks = GameTasks()

        senior_engineer_agent = agents.senior_engineer_agent()
        qa_engineer_agent = agents.qa_engineer_agent()
        chief_qa_agent = agents.chief_qa_engineer_agent()

        with open('config/design.yaml', 'r', encoding='utf-8') as file:
            examples = yaml.safe_load(file)

        inputs = {
            #'game' :  examples[game or 'pacman_basic']
            'game' :  examples[game or 'snake']
            #'game' :  examples[game or 'pacman_advanced']
        }

        code_task = tasks.code_task(
            senior_engineer_agent,
            inputs
        )

        review_task = tasks.review_task(
            qa_engineer_agent,
            inputs

        )

        evaluate_task = tasks.evaluate_task(
            chief_qa_agent,
            inputs
        )

        crew = Crew(
            agents=[
                senior_engineer_agent, qa_engineer_agent, chief_qa_agent
            ],
            tasks=[code_task, review_task, evaluate_task],
            process=Process.sequential,
            verbose=True
        )

        result = crew.kickoff()
        self.output_placeholder.markdown(result)

        return result


if __name__ == "__main__":
    icon("🎲 CoderDojo Game Coder AI Agents")

    st.subheader("Harness the Power of AI to Develop Your Next Game!",
                 divider="blue", anchor=False)


    with st.sidebar:
        st.header("👇 Enter your Game details")
        with st.form("my_form"):
            game = st.text_input(
                "What game would you like to code?", placeholder="snake")
            description = st.text_input(
                "Description of the game to code?", placeholder="The objective of the Snake game is for the player to control a snake that moves across the game area")

            mechanics = st.text_area("What is the mechanics of the game ?",
                                     placeholder="Game Area, Snake Movement, Food")

            submitted = st.form_submit_button("Submit")

        st.divider()


if submitted:
    with st.status("🤖 **Agents at work...**", state="running", expanded=True) as status:
        with st.container(height=500, border=False):
            sys.stdout = StreamToExpander(st)
            game_crew = GameCrew(game, description, mechanics)
            result = game_crew.run()
        status.update(label="✅ Game Plan Ready!",
                      state="complete", expanded=False)

    st.subheader("Here is your Game Plan", anchor=False, divider="green")
    st.markdown(result)