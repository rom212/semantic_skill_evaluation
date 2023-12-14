# Combining Semantic Kernel with Azure Machine Learning Prompt Flow

This repository is the sample code for the Tech Community blog [Combining Semantic Kernel with Azure Machine Learning Prompt Flow](https://techcommunity.microsoft.com/) (TODO: replace link once published)

## Semantic Kernel Spam Classification Skill

In the `skills/ClassificationSkill/Spam` directory, use the `/skprompt.txt` file to build your skill (aka prompt used to define and steer the skill) and the `config.json` file to adjust the Azure OpenAI Service call parameters, including `temperature` and `top_p` parameters.

## Prompt Flow Python Node Source Files

You will find the source code for components to the flow in the root folder. Refer to the blog post to see where/when to use each within Prompt Flow