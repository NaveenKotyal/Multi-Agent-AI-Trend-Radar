from dotenv import load_dotenv
from linkedin_post_generator.crew import AITrendRadarCrew
import sys
import os

load_dotenv()
os.makedirs('Output', exist_ok=True)


def run():
    """
    Entry point for AI Trend Radar Crew.
    This function is used by `crewai run`.
    """

    print("\n🚀 AI Trend Radar + LinkedIn Generator Starting...\n")

    try:
        # You can hardcode or modify this later
        inputs = {
            "focus_area": "Latest AI trends in LLMs, startups, and AI regulation"
        }

        crew_instance = AITrendRadarCrew()

        result = crew_instance.crew().kickoff(
            inputs=inputs
        )

        print("\n✅ Crew execution completed successfully!\n")
        print("📢 Generated LinkedIn Post:\n")
        print(result)

        print("\n📄 Output saved to linkedin_post.md\n")

    except Exception as e:
        print("\n❌ Crew execution failed.")
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    run()