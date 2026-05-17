import logging
import os

import dotenv
import google.generativeai as genai

dotenv.load_dotenv()
logger = logging.getLogger(__name__)

DEFAULT_PROMPT = (
    "You are a helpful assistant that analyzes CSV files and provides insights "
    "based on the data. Please read the CSV file and provide a summary of the "
    "data, including the number of rows, columns, and any interesting patterns "
    "you find."
)


def _get_model() -> genai.GenerativeModel:
    """Create the Gemini model only when content generation is requested."""
    key = os.getenv("GEMINI_API_KEY")
    if not key:
        raise RuntimeError("GEMINI_API_KEY not found in environment variables.")

    genai.configure(api_key=key)
    return genai.GenerativeModel("gemini-3-flash-preview")


def generate_content(prompt: str = DEFAULT_PROMPT, data=None) -> str | None:
    """Generate Gemini content from a prompt and optional CSV sample."""
    try:
        model = _get_model()
        full_prompt = prompt

        if data:
            if isinstance(data, list):
                data_str = "\n".join(str(row) for row in data)
            else:
                data_str = str(data)

            full_prompt = f"{prompt}\n\nCSV Data (first 20 rows):\n{data_str}"
        else:
            logger.warning("No data provided for content generation. Using prompt only.")

        response = model.generate_content(full_prompt)

        with open("gemini_analysis_response.txt", "w", encoding="utf-8") as file:
            file.write(response.text)
            logger.info("Response saved to gemini_analysis_response.txt")

        return response.text
    except Exception as e:
        logger.error("Error generating content: %s", e)
        return None
