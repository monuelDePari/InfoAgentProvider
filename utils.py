from duckduckgo_search import DDGS
from constants import (
    ERROR_WEB_SEARCH,
    NO_WEB_RESULTS,
    MAX_WEB_RESULTS
)

def perform_web_search(query: str) -> str:
    try:
        with DDGS() as ddgs:
            results = [r for r in ddgs.text(query, max_results=MAX_WEB_RESULTS)]
        text = "\n".join([r["body"] for r in results if "body" in r])

        return text or NO_WEB_RESULTS
    except Exception as e:
        return ERROR_WEB_SEARCH.format(error=e)
