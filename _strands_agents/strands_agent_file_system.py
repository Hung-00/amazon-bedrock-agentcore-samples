import os

os.environ["BYPASS_TOOL_CONSENT"] = "true"

from strands import Agent
from strands_tools import file_read, file_write, editor
from strands.models import BedrockModel

bedrock_model = BedrockModel(
    model_id="us.anthropic.claude-3-7-sonnet-20250219-v1:0",
)

agent = Agent(model=bedrock_model, tools=[file_read, file_write, editor])

# Integrate with Bedrock AgentCore
from bedrock_agentcore.runtime import BedrockAgentCoreApp

app = BedrockAgentCoreApp()


@app.entrypoint
def agent_invocation(payload, context):
    """Handler for agent invocation"""
    user_message = payload.get(
        "prompt",
        "No prompt found in input, please guide customer to create a json payload with prompt key",
    )
    result = agent(user_message)
    return {"result": result.message}


app.run()
