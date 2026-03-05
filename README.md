# LinkedIn Post Generator (AI Trend Radar Crew)

A [crewAI](https://crewai.com) multi-agent system that researches recent AI/tech trends and generates ready-to-publish LinkedIn posts. The crew aggregates trends, analyzes strategic value, and writes concise, engagement-focused content.

## What it does

1. **Trend aggregation** — Searches the web for recent AI developments (last 7 days) in your chosen focus area.
2. **Insight analysis** — Picks the strongest trend and extracts business/professional takeaways.
3. **LinkedIn post** — Writes a short post (hook, explanation, insight, CTA, hashtags) saved to `Output/linkedin_post.md`.

## Installation

- **Python**: 3.10 to 3.13 (see `pyproject.toml`).
- **Package manager**: [uv](https://docs.astral.sh/uv/) is recommended.

Install uv (if needed):

```bash
pip install uv
```

From the project root, install dependencies:

```bash
uv sync
```

Optional: if you use the CrewAI CLI:

```bash
crewai install
```

## Environment variables

Create a `.env` file in the project root with:

| Variable | Purpose |
|----------|---------|
| `GROQ_API_KEY` | LLM API key (used by crewAI for agents). |
| `SERPER_API_KEY` | [Serper](https://serper.dev) API key for web search (trend aggregation). |

Example:

```env
OPENAI_API_KEY=sk-...
SERPER_API_KEY=...
```

## Running the project

### Option 1: CLI (crewAI)

From the project root:

```bash
crewai run
```

This uses the default focus area in `main.py`, runs the crew, prints the post, and writes it to `Output/linkedin_post.md`.

### Option 2: Streamlit app

From the project root, use the project environment so `crewai` and dependencies are available:

```bash
uv run streamlit run app.py
```

Then open the URL shown (e.g. http://localhost:8501). Enter a **focus area** (e.g. “Latest AI trends in LLMs, startups, and AI regulation”), click **Generate LinkedIn post**, and view or copy the result. The post is also saved to `Output/linkedin_post.md`.

> **Note:** Run with `uv run streamlit run app.py`, not plain `streamlit run app.py`, so the correct virtualenv (with crewai) is used.

### Option 3: Python entrypoint

```bash
uv run python -m linkedin_post_generator.main
```

Or after `uv sync`, from the repo root:

```bash
uv run linkedin_post_generator
```

## Project structure

| Path | Description |
|------|-------------|
| `app.py` | Streamlit UI; focus area input and post display. |
| `src/linkedin_post_generator/main.py` | CLI entrypoint; default `focus_area` and `crewai run` hook. |
| `src/linkedin_post_generator/crew.py` | Crew definition: agents, tasks, tools (Serper), sequential process. |
| `src/linkedin_post_generator/config/agents.yaml` | Agent roles, goals, backstories. |
| `src/linkedin_post_generator/config/tasks.yaml` | Task descriptions, expected outputs, and `{focus_area}` template. |
| `Output/linkedin_post.md` | Generated LinkedIn post (created by both CLI and app). |
| `knowledge/user_preference.txt` | Optional user context (e.g. name, role, interests). |

## Understanding the crew

| Agent | Role | Task |
|-------|------|------|
| **Trend aggregator** | AI Trend Intelligence Analyst | Collects 3 recent, high-impact AI trends (web search via Serper). |
| **Insight analyst** | Strategic AI Insight Analyst | Analyzes trends and selects one with the best strategic/value angle. |
| **LinkedIn content strategist** | LinkedIn Growth & Content Strategist | Writes the final post (hook, explanation, insight, CTA, 5 hashtags). |

Tasks are run **sequentially**: trends → analysis → post. The focus area is injected into the first task via the `{focus_area}` input.

## Customization

- **`.env`** — Set `OPENAI_API_KEY` and `SERPER_API_KEY`.
- **`config/agents.yaml`** — Edit roles, goals, and backstories (supports `{focus_area}`).
- **`config/tasks.yaml`** — Change search instructions, output format, or post constraints (e.g. word limit, tone).
- **`crew.py`** — Add tools, change `Process`, or tweak agent options (e.g. `max_iter`).
- **`main.py`** — Change the default `focus_area` in the `inputs` dict for the CLI run.

## Support

- [CrewAI documentation](https://docs.crewai.com)
- [CrewAI GitHub](https://github.com/joaomdmoura/crewai)
- [CrewAI Discord](https://discord.com/invite/X4JWnZnxPb)
- [Chat with docs](https://chatg.pt/DWjSBZn)
