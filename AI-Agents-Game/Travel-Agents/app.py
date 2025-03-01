from crewai import Crew, Process
from trip_agents import TripAgents, StreamToExpander
from trip_tasks import TripTasks
import streamlit as st
import sys

st.set_page_config(page_icon="✈️", layout="wide")


def icon(emoji: str):
    """Shows an emoji as a Notion-style page icon."""
    st.write(
        f'<span style="font-size: 78px; line-height: 1">{emoji}</span>',
        unsafe_allow_html=True,
    )


class TripCrew:

    def __init__(self, origin, cities, date_range, interests):
        self.cities = cities
        self.origin = origin
        self.interests = interests
        self.date_range = date_range
        self.output_placeholder = st.empty()

    def run(self):
        agents = TripAgents()
        tasks = TripTasks()

        city_selector_agent = agents.city_selection_agent()
        local_expert_agent = agents.local_expert()
        travel_concierge_agent = agents.travel_concierge()

        identify_task = tasks.identify_task(
            city_selector_agent,
            self.origin,
            self.cities,
            self.interests,
            self.date_range
        )

        gather_task = tasks.gather_task(
            local_expert_agent,
            self.origin,
            self.interests,
            self.date_range
        )

        plan_task = tasks.plan_task(
            travel_concierge_agent,
            self.origin,
            self.interests,
            self.date_range
        )

        crew = Crew(
            agents=[
                city_selector_agent, local_expert_agent, travel_concierge_agent
            ],
            tasks=[identify_task, gather_task, plan_task],
            process=Process.sequential,
            verbose=True
        )

        result = crew.kickoff()
        self.output_placeholder.markdown(result)

        return result


if __name__ == "__main__":
    icon("🏖️ CoderDojo Travel AI Agents")

    st.subheader("Let AI agents plan your next vacation!",
                 divider="blue", anchor=False)

    import datetime

    today = datetime.datetime.now().date()
    next_year = today.year + 1
    jan_16_next_year = datetime.date(next_year, 1, 10)

    with st.sidebar:
        st.header("👇 Enter your Travel details")
        with st.form("my_form"):
            location = st.text_input(
                "Where are you currently located?", placeholder="Cork")
            cities = st.text_input(
                "Country and city are you interested in vacationing at?", placeholder="Germany, Berlin")
            date_range = st.date_input(
                "Date range you are interested in traveling?",
                min_value=today,
                value=(today, jan_16_next_year + datetime.timedelta(days=5)),
                format="DD/MM/YYYY",
            )
            interests = st.text_area("High level interests and hobbies or extra details about your Travel?",
                                     placeholder="Food, dancing, hiking")

            submitted = st.form_submit_button("Submit")

        st.divider()


if submitted:
    with st.status("🤖 **Agents at work...**", state="running", expanded=True) as status:
        with st.container(height=500, border=False):
            sys.stdout = StreamToExpander(st)
            trip_crew = TripCrew(location, cities, date_range, interests)
            result = trip_crew.run()
        status.update(label="✅ Travel Plan Ready!",
                      state="complete", expanded=False)

    st.subheader("Here is your Travel Plan", anchor=False, divider="rainbow")
    st.markdown(result)