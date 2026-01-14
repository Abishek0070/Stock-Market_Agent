import os
from typing import List
from crewai import Agent, Crew, Process, Task, LLM
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import SerperDevTool
from langchain_groq import ChatGroq
from dotenv import load_dotenv
import litellm
litellm.set_verbose = False
litellm.suppress_debug_info = True

load_dotenv()

@CrewBase
class Finance():
    """Finance crew for daily stock market updates"""

    # These point to your YAML files in the config folder
    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    def __init__(self) -> None:
        # 1. Standardize on the Native LLM class for better stability
        self.groq_llm = LLM(
            model="groq/llama-3.3-70b-versatile",
            api_key=os.getenv("GROQ_API_KEY"),
            temperature=0.1
        )
        # 2. Initialize the Search Tool once to be reused
        self.search_tool = SerperDevTool()

    @agent
    def researcher(self) -> Agent:
        return Agent(
            config=self.agents_config['researcher'],
            llm=self.groq_llm,
            tools=[self.search_tool], # Use the pre-initialized tool
            verbose=True,
            allow_delegation=False
        )

    @agent
    def reporting_analyst(self) -> Agent:
        return Agent(
            config=self.agents_config['reporting_analyst'],
            llm=self.groq_llm,
            verbose=True,
            allow_delegation=False
        )

    @task
    def research_task(self) -> Task:
        return Task(
            config=self.tasks_config['research_task'],
        )

    @task
    def reporting_task(self) -> Task:
        return Task(
            config=self.tasks_config['reporting_task'],
            output_file='report.md'
        )

    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
            memory=False, # Keeps it fast and avoids OpenAI embedding calls
            llm=self.groq_llm,
            manager_llm=self.groq_llm
        )