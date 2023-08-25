import semantic_kernel as sk
from semantic_kernel.connectors.ai.open_ai import OpenAITextCompletion, AzureTextCompletion

kernel = sk.Kernel()

api_key, org_id = sk.openai_settings_from_dot_env()

kernel.add_text_completion_service("gpt-service", OpenAITextCompletion("text-davinci-003", api_key, org_id))


skills_directory = "skills"

contentFunctions = kernel.import_semantic_skill_from_directory(skills_directory, "ContentSkill")

emailWritingFunction = contentFunctions["Email"]

print("\n\nWriting email...")
print(emailWritingFunction("sick leave"))


socialPostFunction = contentFunctions["Social"]

print("\n\nWriting social post with hash tags...")
print(socialPostFunction("ขอเชิญมาเที่ยวเมืองไทย"))