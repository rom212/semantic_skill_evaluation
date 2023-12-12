from promptflow import tool
import semantic_kernel as sk
from semantic_kernel.connectors.ai.open_ai import AzureChatCompletion

deployment, api_key, endpoint = sk.azure_openai_settings_from_dot_env()
kernel = sk.Kernel()
kernel.add_chat_service("chat_completion", AzureChatCompletion(deployment, endpoint, api_key=api_key))
skill = kernel.import_semantic_skill_from_directory("./skills", "ClassificationSkill")
spam_classification_function = skill["Spam"]

@tool
def my_spam_detection_tool(input1: str) -> str:

    # deployment, api_key, endpoint = sk.azure_openai_settings_from_dot_env()
    # kernel = sk.Kernel()
    # kernel.add_chat_service("chat_completion", AzureChatCompletion(deployment, endpoint, api_key=api_key))
    # skill = kernel.import_semantic_skill_from_directory("./skills", "ClassificationSkill")
    # spam_classification_function = skill["Spam"]
    return spam_classification_function(input1).result
