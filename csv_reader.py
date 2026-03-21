import csv, logging, os
import google.generativeai as genai

# Configure logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    filename='csv_reader.log',
    filemode='a',
    encoding='utf-8'
)

logger = logging.getLogger(__name__)



def read_csv(file_path):
    '''Reads a CSV file and returns a list of dictionaries representing each row.'''
    try: 
        with open(file_path, 'r', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            return [row for row in reader]
    except FileNotFoundError:
        logger.error(f"File not found: {file_path}")
        return []
    except Exception as e:
        logger.error(f"Error reading CSV file: {e}")
        return []

def csv_analyzer(file_path):
    '''Analyzes the CSV file and prints summary information.'''
    data = read_csv(file_path)
    if not data:
        logger.warning("No data found in the CSV file.")
        return

    logger.info(f"Total rows: {len(data)}")
    cols = data[0].keys()
    print(f"Columns: {', '.join(cols)}")
    logger.info(f"Columns: {', '.join(cols)}")

    # Example analysis: Count occurrences of values in a specific column
    column_name = input("Enter the column name to analyze: ")
    if column_name not in cols:
        logger.warning(f"Column '{column_name}' not found in the CSV file.")
        return

    value_counts = {}
    for row in data:
        value = row[column_name]
        value_counts[value] = value_counts.get(value, 0) + 1

    logger.info(f"Value counts for column '{column_name}':")
    for value, count in value_counts.items():
        logger.info(f"{value}: {count}")

def get_size(file_path):
    '''Gets the size of the CSV file and prints it.'''
    size = os.path.getsize(file_path)
    logger.info(f"File size: {size} bytes")
    print(f"File size: {size} bytes")


prompt = 'You are a helpful assistant that analyzes CSV files and provides insights based on the data. Please read the CSV file and provide a summary of the data, including the number of rows, columns, and any interesting patterns you find.'
def generate_content(prompt, data=None):
    '''Generates content from Google Gemini API based on the given prompt.'''
    key = 'AIzaSyBR5_09zevOyabNV4Ncg25-VnjrO9nJfKs'
    genai.configure(api_key=key)
    model = genai.GenerativeModel("gemini-3-flash-preview")
    try:
        full_prompt = prompt

        if data:
            if isinstance(data, list):
                data_str = "\n".join(str(row) for row in data)
            else:
                data_str = str(data)

            full_prompt = f"{prompt}\n\nCSV Data (first 20 rows):\n{data_str}"
        elif not data:
            logger.warning("No data provided for content generation. Using prompt only.")

        response = model.generate_content(full_prompt)

        with open('gemini_analysis_response.txt', 'w', encoding='utf-8') as f:
            f.write(response.text)
            logger.info("Response saved to gemini_analysis_response.txt")
            print("Response saved to gemini_analysis_response.txt")

        return response.text

    except Exception as e:
        logger.error(f"Error generating content: {e}")
        return None



if __name__ == "__main__":
    file_path = input("Enter the path to the CSV file: ")
    csv_analyzer(file_path)
    get_size(file_path)
    data = read_csv(file_path)[:20]  # Get the first 20 rows of data
    content = generate_content(prompt, data)
   

