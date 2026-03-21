import google.generativeai as genai

# You can find your API key in the Google Cloud Console
key = 'AIzaSyBR5_09zevOyabNV4Ncg25-VnjrO9nJfKs'
genai.configure(api_key=key)
model = genai.GenerativeModel("gemini-3-flash-preview")

def generate_content(prompt, data=None):
    """
    Generates content from Google Gemini API based on the given prompt and CSV data
    
    Args:
        prompt (str): The prompt to send to the Gemini API
        data (str or list, optional): First 20 rows of CSV data to include with the prompt
        
    Returns:
        str: Generated content from the API or error message
    """
    try:
        # Combine prompt with data if provided
        full_prompt = prompt
        if data:
            if isinstance(data, list):
                # If data is a list, join it into a string
                data_str = "\n".join(data)
            else:
                # If data is already a string, use it directly
                data_str = str(data)
            
            full_prompt = f"{prompt}\n\nCSV Data (first 20 rows):\n{data_str}"
        
        response = model.generate_content(full_prompt)
        return response.text
    except Exception as e:
        return f"Error generating content: {str(e)}"

# Example usage:
if __name__ == "__main__":
    # Generate content and save to file
    prompt = "Explain what is markdown and how it is used in data science."
    content = generate_content(prompt)
    
    # Save the response to a text file
    with open('gemini_response.txt', 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("Content generated and saved to gemini_response.txt")