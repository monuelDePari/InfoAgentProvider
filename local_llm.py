import json
import logging
from ollama import chat
from constants import (
    PROMPT_CHECK_UP_TO_DATE,
    PROMPT_SHORT_ANSWER,
    PROMPT_SUMMARIZE_WEB,
    ERROR_SUMMARIZE,
    MAX_TEXT_LENGTH_FOR_SUMMARY
)

logger = logging.getLogger(__name__)

class LocalLLM:
    def __init__(self, config_path: str = "config.json"):
        try:
            with open(config_path, "r", encoding="utf-8") as f:
                config = json.load(f)
                self.model = config["model"]
        except FileNotFoundError:
            logger.error(f"Config file not found: {config_path}")
            raise
        except KeyError:
            logger.error("'model' key missing from config file")
            raise

    def query(self, prompt: str) -> str:
        response = chat(model=self.model, messages=[{"role": "user", "content": prompt}])
        return response.get("message", {}).get("content") or response.get("content", "")

    def check_has_up_to_date_info(self, question: str) -> bool:
        try:
            content = self.query(PROMPT_CHECK_UP_TO_DATE.format(question=question)).strip().lower()
            return content.startswith("yes")
        except Exception as e:
            logger.error(f"Error checking LLM knowledge: {e}")
            return False

    def get_short_answer(self, question: str) -> str:
        try:
            return self.query(PROMPT_SHORT_ANSWER.format(question=question)).strip()
        except Exception as e:
            logger.error(f"Error getting short answer: {e}")
            return f"Error getting answer: {e}"

    def summarize_web_results(self, text: str, question: str) -> str:
        try:
            truncated_text = text[:MAX_TEXT_LENGTH_FOR_SUMMARY]
            content = self.query(PROMPT_SUMMARIZE_WEB.format(
                question=question,
                text=truncated_text
            )).strip()
            return content
        except Exception as e:
            logger.error(f"Error summarizing web results: {e}")
            return ERROR_SUMMARIZE.format(error=e)
