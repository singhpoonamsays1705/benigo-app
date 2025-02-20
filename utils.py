# api_functions.py

from bs4 import BeautifulSoup
import requests
import re
import json
from langchain_community.document_loaders.recursive_url_loader import RecursiveUrlLoader
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os

def scrape(url):
    if not url:
        return {'error': 'URL parameter is required'}

    def custom_extractor(html_content):
        soup = BeautifulSoup(html_content, "html.parser")
        return soup.get_text()

    # Instantiate the RecursiveUrlLoader with the provided URL
    loader = RecursiveUrlLoader(url=url, extractor=custom_extractor, max_depth=2)
    docs = loader.load()

    output_file = "scraped_data.txt"
    with open(output_file, "w", encoding="utf-8") as file:
        for doc in docs:
            title = doc.metadata.get("title")
            source = doc.metadata.get("source")
            content = doc.page_content
            if isinstance(title, str) and isinstance(source, str) and isinstance(content, str):
                file.write("Page Title: " + title + "\n")
                file.write("Page URL: " + source + "\n")
                file.write("Page Content:\n" + content + "\n\n")
            else:
                print("Skipped a document due to non-string content.")

    # Read and clean the scraped data
    with open("scraped_data.txt", "r", encoding="utf-8") as file:
        content = file.read()

    cleaned_content = re.sub(r'[\n\t]+', '\n', content.strip())
    lines = cleaned_content.split('\n')
    unique_lines = []
    prev_line = None
    for line in lines:
        if line != prev_line:
            unique_lines.append(line)
        prev_line = line
    cleaned_content = '\n'.join(unique_lines)

    with open("cleaned_scraped_data.txt", "w", encoding="utf-8") as file:
        file.write(cleaned_content + '\n')

    return {'message': 'Data has been successfully written to cleaned_scraped_data.txt'}

def generate_response_context():
    # with open("prompts/prompt_context.txt", "r", encoding="utf-8") as f:
    #     prompt_context = f.read()
    # extracted_data = open("cleaned_scraped_data.txt", "r", encoding="utf-8").read()
    # prompt_context = prompt_context.replace("{{extracted_data}}", extracted_data)
        
    # load_dotenv(override=True)
    # print(os.getenv("OPENAI_API_KEY"))
    
    # llm = ChatOpenAI(model="o3-mini")
    # For demonstration, reading sample response
    with open("sample_context.json", "r", encoding="utf-8") as f:
        response_context = json.load(f)
    with open("output_context.json", "w", encoding="utf-8") as f:
        json.dump(response_context, f, indent=4)
    
    return {'message': 'Response for business context is saved to output_context.json'}

def generate_response_core_intent():
    # with open("prompts/prompt_core_intent.txt", "r", encoding="utf-8") as f:
    #     prompt_core_intent = f.read()
    # # extracted_data = open("cleaned_scraped_data.txt", "r", encoding="utf-8").read()
    # # prompt_core_intent = prompt_core_intent.replace("{{extracted_data}}", extracted_data)
        
    # # load_dotenv(override=True)
    # # print(os.getenv("OPENAI_API_KEY"))
    
    # # llm = ChatOpenAI(model="o3-mini")
    with open("sample_core_intent.json", "r", encoding="utf-8") as f:
        response_core_intent = json.load(f)
    with open("output_core_intent.json", "w", encoding="utf-8") as f:
        json.dump(response_core_intent, f, indent=4)
    
    return {'message': 'Response for core intent is saved to output_core_intent.json'}

def generate_response_off_intent():
    # with open("prompts/prompt_off_intent.txt", "r", encoding="utf-8") as f:
    #     prompt_off_intent = f.read()
    # extracted_data = open("cleaned_scraped_data.txt", "r", encoding="utf-8").read()
    # prompt_off_intent = prompt_off_intent.replace("{{extracted_data}}", extracted_data)
        
    # load_dotenv(override=True)
    # print(os.getenv("OPENAI_API_KEY"))
    
    # llm = ChatOpenAI(model="o3-mini")
    with open("sample_off_intent.json", "r", encoding="utf-8") as f:
        response_off_intent = json.load(f)
    with open("output_off_intent.json", "w", encoding="utf-8") as f:
        json.dump(response_off_intent, f, indent=4)
    
    return {'message': 'Response for off intent is saved to output_off_intent.json'}

def generate_response_role():
    # with open("prompts/prompt_role.txt", "r", encoding="utf-8") as f:
    #     prompt_role = f.read()
    # extracted_data = open("cleaned_scraped_data.txt", "r", encoding="utf-8").read()
    # prompt_role = prompt_role.replace("{{extracted_data}}", extracted_data)
        
    # load_dotenv(override=True)
    # print(os.getenv("OPENAI_API_KEY"))
    
    # llm = ChatOpenAI(model="o3-mini")
    with open("sample_role.json", "r", encoding="utf-8") as f:
        response_role = json.load(f)
    with open("output_role.json", "w", encoding="utf-8") as f:
        json.dump(response_role, f, indent=4)
    
    return {'message': 'Response for role is saved to output_role.json'}


def run_all(url):
    # First, scrape the provided URL
    # scrape_result = scrape(url)
    # If an error occurred in scraping, return the error message
    # if 'error' in scrape_result:
    #     return scrape_result

    # Run the rest of the functions sequentially
    generate_response_context()
    generate_response_core_intent()
    generate_response_off_intent()
    generate_response_role()
    print("Executed!!!")
    return {'message': f'All processes completed successfully from {url}!'}
