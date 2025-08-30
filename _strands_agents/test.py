import boto3

import json

# Initialize the Bedrock AgentCore client
agent_core_client = boto3.client("bedrock-agentcore", region_name="us-east-1")


# Prepare the payload
payload = json.dumps({"prompt": "Introduce Canada"}).encode()

# Invoke the agent
response = agent_core_client.invoke_agent_runtime(
    agentRuntimeArn="arn:aws:bedrock-agentcore:us-east-1:928738046450:runtime/strands_agent_file_system-05Bf9JCgOe",
    runtimeSessionId="strands_agent_file_system-05Bf9JCgOe",
    payload=payload,
)

# if "text/event-stream" in response.get("contentType", ""):
#     content = []
#     for line in response["response"].iter_lines(chunk_size=1):
#         if line:
#             line = line.decode("utf-8")
#             if line.startswith("data: "):
#                 line = line[6:]
#                 logger.info(line)
#                 content.append(line)
#     print(content)
# else:
#     try:
#         events = []
#         for event in response.get("response", []):
#             events.append(event)
#     except Exception as e:
#         events = [f"Error reading EventStream: {e}"]

print(response.get("response"))
