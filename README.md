# AI Agent with LangGraph

A Python-based AI agent that intelligently answers user questions using either its internal knowledge (local LLM via Ollama) or web search results.

## Features

- **Intelligent Routing**: Automatically determines whether to use internal LLM knowledge or web search
- **Local LLM Integration**: Uses Ollama for local language model inference
- **Web Search Fallback**: Performs DuckDuckGo searches for up-to-date information
- **LangGraph Workflow**: Implements a structured state machine for reliable execution
- **Comprehensive Logging**: Tracks all operations for debugging and monitoring

## Architecture

```
User Question
    ↓
[Check LLM Knowledge]
    ↓
Has Info? → Yes → [Get Short Answer] → [Display]
    ↓
   No → [Web Search] → [Summarize] → [Display]
```

## Installation

1. Install Python 3.11+
2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Install and run Ollama with your preferred model:
```bash
ollama pull phi4
ollama serve
```

4. Configure the model in `config.json`:
```json
{
  "model": "phi4"
}
```

## Usage

Run the agent:
```bash
python startup.py
```

The agent will greet you and wait for questions. Type your question and press Enter. Type `exit` to quit.

### Example Session

```
aiagent > Hi! What do you want to know? (type 'exit' to quit)
user > What is Python?
aiagent > Python is a high-level programming language... (* used internal LLM)

user > What are the latest breakthroughs in quantum computing announced in October 2025?
aiagent > [Web search results summarized] (* used external web search)

user > exit
aiagent > Bye
```

## Project Structure

```
InfoAgentProvider/
├── agent.py           # Main CLI entry point
├── graph.py           # LangGraph workflow definition
├── local_llm.py       # LocalLLM class for Ollama integration
├── utils.py           # Utility functions (web search)
├── constants.py       # Configuration and prompt templates
├── config.json        # Model configuration
├── requirements.txt   # Python dependencies
└── agent.log          # Runtime logs
```

## Configuration

### Prompts
All prompts are defined in `constants.py` and can be customized:
- `PROMPT_CHECK_UP_TO_DATE`: Asks LLM if it has confident knowledge
- `PROMPT_SHORT_ANSWER`: Requests concise 2-sentence answers
- `PROMPT_SUMMARIZE_WEB`: Summarizes web search results

### Search Configuration
- `MAX_WEB_RESULTS`: Maximum number of search results (default: 20)
- `MAX_TEXT_LENGTH_FOR_SUMMARY`: Max text length for summarization (default: 4000)

## Logging

Logs are written to both console and `agent.log` file.

## License

MIT License

