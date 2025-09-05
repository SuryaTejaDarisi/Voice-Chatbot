# Voice-Chatbot

## Workflow

#### Input Audio &rarr; Speech-To-Text Conversion &rarr; LLM Respnse Generation &rarr; Text-To-Speech Generation &rarr; Output Audio

We used Gemini 2.5 Flash API for Response Generation as it's a completely free and trustable API.
## Implementation
Initially, let's set up a virtual environment.
### 1. Setting up a Virtual Environment
To create an environment:
```
python -m venv <env_name>
```
To access it:
```
<env_name>\Scripts\activate
```
To deactivate it:
```
deactivate
```

### 2. Installing required Libraries
This repo contains a requirements.txt file which contains all the python libraries required.
```
pip install -r .\requirements.txt
```

### 3. Working on Code
Just run the last code cell in the notebook for testing.
```
main()
```
The file website.py contains code for hosting the website publicly.
A view of the website on mobile phone
![WhatsApp Image 2025-09-05 at 23 47 25_82665d01](https://github.com/user-attachments/assets/ddfe9e54-4c1b-4418-9fd2-aa0320114fe4)



### P.S.
This project can't be executed in Colab as it doesn't support a Mic. So, one can only run this locally.
