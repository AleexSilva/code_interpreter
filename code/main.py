import os
from IPython.display import Markdown, display, update_display
from datetime import datetime
from openai import OpenAI
from decouple import config
from yaml_handler import YAMLHandler
from logger import Logger


logger = Logger("code_interpreter")


MODEL='gpt-4o-mini'
MODEL_LLAMA = 'llama3.2'

api_key = config('OPENAI_API_KEY')

if api_key and api_key.startswith('sk-proj-') and len(api_key)>10:
    logger.info("API key looks good so far")
else:
    logger.info("There might be a problem with your API key? Please visit the troubleshooting notebook!")

openai = OpenAI(api_key = api_key)
ollama = OpenAI(base_url='http://localhost:11434/v1', api_key='ollama')


def system_prompt():
    """
    Reads the system prompt from the YAML file and returns it as a string.
    
    The system prompt is the prompt that is sent to the AI model as the first message, 
    and is used to set the context for the conversation. The system prompt is 
    typically used to provide information about the code that is being analyzed, 
    such as the language and the type of code.

    Returns:
        str: The system prompt as a string.
    """
    yaml_handler = YAMLHandler("input.yaml")
    yaml_data = yaml_handler.read_yaml()
    system_prompt = yaml_data.get("system_prompt")
    logger.info(f"system_prompt: {system_prompt}")
    return system_prompt

def code_explain(LLM, model, question):
    stream = LLM.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": system_prompt()},
            {"role": "user", "content": question}
        ],
        stream=True
    )

    response = ""
    display_handle = display(Markdown(""), display_id=True)
    

    output_dir = "Output"
    os.makedirs(output_dir, exist_ok=True)
    date = datetime.now().strftime("%Y-%m-%d")
    if LLM == openai:
        llm = 'openai'
    else:
        llm = 'ollama'
    output_file = os.path.join(output_dir,f"code_explain_{llm}_{date}.md")

    with open(output_file, "w", encoding="utf-8") as file:
        for chunk in stream:
            text = chunk.choices[0].delta.content or ''
            response += text
            response = response.replace("```", "").replace("markdown", "")


            update_display(Markdown(response), display_id=display_handle.display_id)


            file.write(text)

    logger.info(f"Brochure saved to: {output_file}")

if __name__ == "__main__":
    code_explain(LLM=ollama, model=MODEL_LLAMA, question = question)