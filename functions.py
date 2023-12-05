from dotenv import load_dotenv
from langchain.agents.openai_assistant import OpenAIAssistantRunnable
import re

load_dotenv()


def get_answer(question: str) -> str:
    assistant = OpenAIAssistantRunnable(
        assistant_id="asst_8HFshA1tzFfosxA6G7kzqpCt", as_agent=True
    )

    response = assistant.invoke({"content": question})
    # Access the 'return_values' dictionary
    return_values = response.return_values

    # Extract the 'output' value
    return return_values["output"]


def parse_response(response: str) -> str:
    pattern = r"Text\(annotations=\[\], value='(.*?)'\), type='text'"

    values = re.findall(pattern, response, re.DOTALL)

    return values[0]
