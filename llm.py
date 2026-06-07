import logging
import os

import dotenv
from groq import Groq

dotenv.load_dotenv()
logger = logging.getLogger(__name__)
DEFAULT_MODEL = os.getenv("GROQ_MODEL", "llama-3.3-70b-versatile")
DEFAULT_TIMEOUT = 30

DEFAULT_PROMPT = (
    "You are a helpful assistant that analyzes CSV files and provides insights "
    "based on the data. Please read the CSV file and provide a summary in Russian of the "
    "data, including the number of rows, columns, and any interesting patterns "
    "you find."
)


def _get_model() -> Groq:
    """Create the Groq client only when content generation is requested."""
    key = os.getenv("GROQ_API_KEY")
    if not key:
        raise RuntimeError("GROQ_API_KEY not found in environment variables.")

    return Groq(api_key=key)


def generate_content(prompt: str = DEFAULT_PROMPT, data=None) -> str | None:
    """Generate Groq content from a prompt and optional CSV sample."""
    try:
        client = _get_model()
        full_prompt = prompt

        if data:
            if isinstance(data, list):
                data_str = "\n".join(str(row) for row in data)
            else:
                data_str = str(data)

            full_prompt = f"{prompt}\n\nCSV data sample:\n{data_str}"
        else:
            logger.warning("No data provided for content generation. Using prompt only.")

        response = client.chat.completions.create(
            model=DEFAULT_MODEL,
            messages=[
                {
                    "role": "system",
                    "content": "You analyze CSV samples and write concise summaries.",
                },
                {"role": "user", "content": full_prompt},
            ],
            temperature=0.2,
            timeout=DEFAULT_TIMEOUT
        )
        content = response.choices[0].message.content

        with open("groq_analysis_response.txt", "w", encoding="utf-8") as file:
            file.write(content)
            logger.info("Response saved to groq_analysis_response.txt")

        return content
    except Exception as e:
        logger.error("Error generating content: %s", e)
        return None
   