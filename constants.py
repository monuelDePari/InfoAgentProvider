# User Interface Messages
GREETING_MESSAGE = "aiagent > Hi! What do you want to know? (type 'exit' to quit)"
GOODBYE_MESSAGE = "aiagent > Bye"
EXIT_COMMAND = "exit"

# Prompt Templates
PROMPT_CHECK_UP_TO_DATE = """You are a knowledgeable AI assistant. 
Can you confidently answer the following question based on your training knowledge? 
Answer 'yes' if you know the answer (even for general topics like programming languages, science, history, etc.). 
Answer 'no' ONLY if the question requires very recent information (like today's news, current events, latest updates) 
or if you genuinely don't know the topic at all. 
Respond with ONLY 'yes' or 'no', nothing else.

Question: {question}"""

PROMPT_SHORT_ANSWER = """You are a reasoning AI assistant. 
Answer the following question in 2 sentences, clearly and concisely.

Question: {question}"""

PROMPT_SUMMARIZE_WEB = """Summarize the following web search results in 2 sentences to directly answer the user's question.
Question: {question}

{text}"""

# Source Labels
SOURCE_INTERNAL = "internal"
SOURCE_EXTERNAL = "external"
SOURCE_INTERNAL_LABEL = "internal LLM"
SOURCE_EXTERNAL_LABEL = "external web search"

# Response Messages
ANSWER_FORMAT = "aiagent > {answer} (* used {source})\n"
ERROR_WEB_SEARCH = "Web search error: {error}"
ERROR_SUMMARIZE = "Error summarizing with LLM: {error}"
NO_WEB_RESULTS = "No relevant web results found."

# Search Configuration
MAX_WEB_RESULTS = 20
MAX_TEXT_LENGTH_FOR_SUMMARY = 4000
