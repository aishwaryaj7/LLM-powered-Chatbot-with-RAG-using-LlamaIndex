import os
import yaml

def get_apikey():
    """
    Reads API key from a configuration file.
    Returns: api_key (str): The OpenAI API key.

    """

    # Construct the full path to the configuration file
    # script_dir = "/LLM_chat_assistant/"
    # file_path = os.path.join(script_dir, "apikeys.yml")
    file_path = "/Users/ajsharma/PycharmProjects/LLM_chat_assistant/apikeys.yml"

    with open(file_path, 'r') as yamlfile:
        loaded_yamlfile = yaml.safe_load(yamlfile)
        API_KEY = loaded_yamlfile['openai']['api_key']

    return API_KEY