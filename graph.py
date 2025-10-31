import logging
from langgraph.graph import StateGraph, END
from typing import TypedDict
from utils import perform_web_search
from local_llm import LocalLLM
from constants import (
    SOURCE_INTERNAL,
    SOURCE_EXTERNAL,
    SOURCE_INTERNAL_LABEL,
    SOURCE_EXTERNAL_LABEL,
    ANSWER_FORMAT
)

logger = logging.getLogger(__name__)

class AgentState(TypedDict, total=False):
    question: str
    answer: str
    source: str
    has_info: bool

class AgentGraph:
    def __init__(self):
        self.llm = LocalLLM()
        self.graph = self._build_graph()

    def invoke(self, initial_state: dict) -> dict:
        return self.graph.invoke(initial_state)

    def _check_llm_knowledge(self, state: AgentState) -> AgentState:
        question = state["question"]
        has_info = self.llm.check_has_up_to_date_info(question)
        if has_info:
            answer = self.llm.get_short_answer(question)
            return {
                "answer": answer,
                "source": SOURCE_INTERNAL,
                "has_info": True
            }

        return {
            "has_info": False
        }

    def _perform_web_search(self, state: AgentState) -> AgentState:
        question = state["question"]
        results = perform_web_search(question)
        summary = self.llm.summarize_web_results(results, question)
        return {
            "answer": summary,
            "source": SOURCE_EXTERNAL
        }

    def _display_answer(self, state: AgentState) -> AgentState:
        answer = state["answer"].strip()
        src = SOURCE_INTERNAL_LABEL if state["source"] == SOURCE_INTERNAL else SOURCE_EXTERNAL_LABEL
        print(ANSWER_FORMAT.format(answer=answer, source=src))
        return {}

    def _decide_next_node(self, state: AgentState) -> str:
        has_info = state.get("has_info", False)
        return "show_answer" if has_info else "web_search"

    def _build_graph(self):
        graph = StateGraph(AgentState)

        graph.add_node("local_llm", self._check_llm_knowledge)
        graph.add_node("web_search", self._perform_web_search)
        graph.add_node("show_answer", self._display_answer)

        graph.set_entry_point("local_llm")

        graph.add_conditional_edges(
            "local_llm",
            self._decide_next_node,
            {
                "web_search": "web_search",
                "show_answer": "show_answer"
            },
        )
        graph.add_edge("web_search", "show_answer")
        graph.add_edge("show_answer", END)

        return graph.compile()


def create_agent_graph() -> AgentGraph:
    return AgentGraph()
