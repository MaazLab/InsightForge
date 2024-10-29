import argparse
from crewai import Crew, Process
from tasks import research_task, write_task
from agents import news_researcher, news_writer

# Set up CLI argument parsing
parser = argparse.ArgumentParser(description="Run the InsightForge project to generate an article based on a specified topic.")
parser.add_argument("--topic", type=str, help="Topic for the article")

args = parser.parse_args()

# Check if topic is provided; if not, raise an exception
if not args.topic:
    raise ValueError("Error: A topic must be provided. Use --topic to specify the topic for the article.")

# Form the tech-focused crew with some enhanced configuration
crew = Crew(
    agents=[news_researcher, news_writer],
    tasks=[research_task, write_task],
    process=Process.sequential,
)

# Start the task execution process with the provided topic
result = crew.kickoff(inputs={'topic': args.topic})
print(result)
