from langchain_mcp_adapters.client import MultiServerMCPClient
from langchain.agents import create_agent
from langchain_ollama import ChatOllama

import asyncio


async def main():
    client = MultiServerMCPClient(
        {
            "math": {
                "command": "python",
                "args": [
                    r"D:\AGENTIC_AI_PROJECTS\AGENTIC_AI\MCP_server_Langchain\mathserver.py"
                ],
                "transport": "stdio",
            },

            "weather": {
                "url": "http://localhost:8000/mcp",
                "transport": "streamable_http",
            }
        }
    )

    # Load MCP tools
    tools = await client.get_tools()

    # Local Ollama model
    model = ChatOllama(
        model="llama3.2"      # change if using mistral, qwen, gemma, etc.
    )

    # Create agent
    agent = create_agent(
        model,
        tools
    )

    # Math test
    math_response = await agent.ainvoke(
        {
            "messages": [
                {"role": "user", "content": "what's (3 + 5) x 12?"}
            ]
        }
    )

    print("Math response:", math_response["messages"][-1].content)

    # Weather test
    weather_response = await agent.ainvoke(
        {
            "messages": [
                {"role": "user", "content": "what is the weather in California?"}
            ]
        }
    )

    print("Weather response:", weather_response["messages"][-1].content)


asyncio.run(main())



# Final architecture

#                  User Query
#                       │
#                       ▼
#               Ollama Local Model
#               (llama3.2 / qwen3)
#                       │
#                       ▼
#                ReAct Agent Logic
#                       │
#          ┌────────────┴────────────┐
#          │                         │
#          ▼                         ▼
#    Math MCP Server           Weather MCP Server
#       (stdio)                (HTTP streamable)
#          │                         │
#          ▼                         ▼
#     Return Result            Return Result
#          │                         │
#          └────────────┬────────────┘
#                       ▼
#                LLM Final Answer