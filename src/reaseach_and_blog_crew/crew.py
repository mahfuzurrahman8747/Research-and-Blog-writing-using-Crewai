from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent


@CrewBase
class ResearchAndBlogCrew():
    """Research and Blog Crew is a crew that researches a topic and writes a blog post about it."""

    agents: list[BaseAgent]
    tasks: list[Task]

    # Learn more about YAML configuration files here:
    agents_config = 'config\\agents.yaml'
    tasks_config = 'config\\tasks.yaml'
    
    #=================agents=================
    #oder of agent definition does not matter, but the names should match the ones in the config file

    @agent
    def report_generator(self) -> Agent:
        return Agent(
            config=self.agents_config['report_generator'], # type: ignore[index]
            verbose=True
        )

    @agent
    def blog_writer(self) -> Agent:
        return Agent(
            config=self.agents_config['blog_writer'], # type: ignore[index]
            verbose=True
        )

    #=================tasks=================
    #oder of task definition matters

    @task
    def report_task(self) -> Task:
        return Task(
            config=self.tasks_config['report_task'], # type: ignore[index]
        )

    @task
    def blog_task(self) -> Task:
        return Task(
            config=self.tasks_config['blog_writing_task'], # type: ignore[index]
            output_file='blogs/blog.md'
        )

    #=================crew=================
    # The crew method defines the crew, which is a collection of agents and tasks.
    
    @crew
    def crew(self) -> Crew:
        """Creates the ResearchAndBlogCrew crew"""
        
        return Crew(
            agents=self.agents, # Automatically created by the @agent decorator
            tasks=self.tasks, # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
            
        )
