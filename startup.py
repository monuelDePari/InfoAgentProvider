import logging
from graph import create_agent_graph
from constants import GREETING_MESSAGE, GOODBYE_MESSAGE, EXIT_COMMAND

logging.basicConfig(
    level=logging.ERROR,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('agent.log'),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)

def main():
    print(GREETING_MESSAGE)

    try:
        graph = create_agent_graph()
    except Exception as e:
        logger.error(f"Failed to create agent graph: {e}")
        return

    while True:
        try:
            question = input("user > ").strip()
            if question.lower() == EXIT_COMMAND:
                print(GOODBYE_MESSAGE)
                break

            if not question:
                continue

            graph.invoke({"question": question})
        except KeyboardInterrupt:
            print(f"\n{GOODBYE_MESSAGE}")
            break
        except Exception as e:
            logger.error(f"Error processing question: {e}", exc_info=True)
            print(f"aiagent > Sorry, an error occurred: {e}")

if __name__ == "__main__":
    main()
