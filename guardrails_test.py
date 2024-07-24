import boto3
import json

# Initialize the Bedrock runtime client
client = boto3.client('bedrock-runtime')

# Define your prompt
prompt_text = "What are guardrails  ?"

# Create the request body
body = {
    "messages": [
        {"role": "user", "content": [{"text": prompt_text}]}
    ],
    "inferenceConfig": {
        "maxTokens": 1024,
        "temperature": 0.7,
        "topP": 0.9
    },
    "guardrailConfig": {
        "guardrailIdentifier": "p6f5a32ncdls", 
        "guardrailVersion": "1"  # Replace with your guardrail version
    }
}

# Invoke the Claude 3 Sonnet model with guardrails using ConverseStream
response = client.converse_stream(
    modelId='anthropic.claude-3-sonnet-20240229-v1:0',
    messages=body["messages"],
    inferenceConfig=body["inferenceConfig"],
    guardrailConfig=body["guardrailConfig"]
)

# Process and print the streamed response
if 'stream' in response:
    for event in response['stream']:
        if 'contentBlockDelta' in event:
            print(event['contentBlockDelta']['delta']['text'], end="")
