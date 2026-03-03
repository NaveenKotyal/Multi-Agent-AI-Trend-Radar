from crewai import Crew, Process, Agent, Task
from crewai.project import CrewBase, crew, agent, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from crewai_tools import SerperDevTool
from typing import List
from dotenv import load_dotenv

load_dotenv()

# ================== TOOLS ==================

serper_tool = SerperDevTool(n_results=3)

# rss_tool = RSSFeedTool(
#     rss_urls=[
#         "https://techcrunch.com/tag/artificial-intelligence/feed/",
#         "https://venturebeat.com/category/ai/feed/",
#         "https://openai.com/blog/rss.xml",
#         "https://huggingface.co/blog/feed.xml"
#     ]
# )

tools = [serper_tool]


# ================== CREW CLASS ==================

@CrewBase
class AITrendRadarCrew():
    """AI Trend Radar + LinkedIn Generator Crew"""

    agents: List[BaseAgent]
    tasks: List[Task]

    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"

    # -------- AGENTS --------

    @agent
    def trend_aggregator(self) -> Agent:
        return Agent(
            config=self.agents_config["trend_aggregator"],
            tools=tools,
            verbose=True,
            max_iter=2
        )

    @agent
    def insight_analyst(self) -> Agent:
        return Agent(
            config=self.agents_config["insight_analyst"],
            verbose=True,
            max_iter=2
        )

    @agent
    def linkedin_content_strategist(self) -> Agent:
        return Agent(
            config=self.agents_config["linkedin_content_strategist"],
            verbose=True,
            max_iter=2
        )

    # -------- TASKS --------

    @task
    def trend_collection_task(self) -> Task:
        return Task(
            config=self.tasks_config["trend_collection_task"]
        )

    @task
    def insight_analysis_task(self) -> Task:
        return Task(
            config=self.tasks_config["insight_analysis_task"],
            context=[self.trend_collection_task()]
        )

    @task
    def linkedin_post_generation_task(self) -> Task:
        return Task(
            config=self.tasks_config["linkedin_post_generation_task"],
            context=[self.trend_collection_task(),
                     self.insight_analysis_task()],
            output_file="Output/linkedin_post.md"
        )

    # -------- CREW --------

    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True
        )