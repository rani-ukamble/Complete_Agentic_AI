from openai import OpenAI

client = OpenAI(
  api_key="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"
)

response = client.responses.create(
  model="gpt-5.4-mini",
  input="write a haiku about ai",
  store=True,
)

print(response.output_text);
