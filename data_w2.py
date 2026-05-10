en_concepts_w2 = {
    1: """
::: {.panel-tabset}
## The Limitation of Text
So far, you have built applications where the AI only responds with text or JSON. While powerful, this means the AI is trapped inside a box. It cannot read the current weather, it cannot execute code, and it cannot interact with the outside world.

## Introducing Function Calling
Function Calling (or Tool Use) is the mechanism that allows an LLM to interact with external APIs and local code. Instead of the model returning a text string, you provide the model with a list of "tools" (functions) it can use. If the model determines it needs to use a tool to answer your prompt, it returns a **function call request** containing the necessary arguments.

## The Paradigm Shift
This shifts the AI from a passive oracle into an active Agent. When the AI decides to call a function, your code executes the function locally, gets the result, and passes that result *back* to the AI so it can formulate a final answer.
:::
""",
    2: """
::: {.panel-tabset}
## How does the AI know what tools exist?
Before an AI can call a tool, you must define it. In the Gemini API, this is done by passing an OpenAPI-style schema or using Python type hints to describe the function's purpose, its arguments, and its expected output.

## Writing Good Descriptions
The most important part of defining a tool is the **docstring or description**. The AI relies entirely on your natural language description to decide when and how to use the tool. If you have a tool called `get_weather`, but the description is vague, the AI might hallucinate the arguments.

## The Contract
Defining a tool is like signing a contract with the AI: "If you give me these specific JSON arguments, I will execute this logic and give you back the result."
:::
""",
    3: """
::: {.panel-tabset}
## The Agentic Loop
An AI Agent is simply a language model wrapped in a `while` loop with access to tools and memory. 

## The Core Logic
1. **User Prompt:** The user asks a question ("What's the weather in Paris and then calculate 25% of the temperature?").
2. **AI Decision:** The AI decides it needs to call `get_weather("Paris")`.
3. **Execution:** Your Python script catches the function call request, executes the actual API call to a weather service, and gets `20°C`.
4. **Return:** Your script sends `20°C` back to the AI.
5. **AI Decision 2:** The AI decides it now needs to call `calculator(20, 0.25, 'multiply')`.
6. **Execution 2:** Your script calculates `5` and returns it.
7. **Final Answer:** The AI reads the final result and outputs: "The weather is 20°C, and 25% of that is 5."

This loop is the beating heart of all autonomous AI agents.
:::
""",
    4: """
::: {.panel-tabset}
## The Stateless Nature of LLMs
By default, LLMs have amnesia. If you ask a question, and then ask a follow-up question, the model has no idea what you asked previously. Every API call is isolated.

## Building Memory
To create a conversational agent, you must manually maintain the "Context". This involves storing every user message and every model response in an array (or list) and passing the *entire history* back to the model on every single turn.

## Context Windows
Modern models like Gemini 1.5 Pro have massive context windows (up to 2 million tokens), allowing them to remember entire books of history. However, managing this context efficiently in your code is crucial for performance and cost.
:::
""",
    5: """
::: {.panel-tabset}
## Single vs. Multi-Agent
So far, you've built a single agent that tries to do everything. As tasks get more complex, a single prompt becomes too convoluted and prone to failure.

## Agentic Workflows
Instead of one massive agent, Vibe Coding favors workflows where multiple specialized agents collaborate.
- **The Planner:** Takes the user's complex request and breaks it down into 5 sequential steps.
- **The Researcher:** Takes step 1, browses the web, and returns data.
- **The Coder:** Takes the data and writes a script.

By separating concerns, you drastically reduce hallucinations and improve the robustness of the system.
:::
""",
    6: """
::: {.panel-tabset}
## Project: The Sacristan Agent
A "Sacristan" is someone who takes care of a church—keeping it organized and clean. For your mini-project, you will build a "Sacristan Agent" for your local computer.

## Tool Arsenal
You will equip your agent with the following Python tools:
- `list_directory(path)`
- `read_file(path)`
- `write_file(path, content)`

## The Goal
You will prompt your Sacristan Agent to: "Look in the `./data` folder, read all the text files, summarize their contents, and write a new file called `summary.md`." 
This project proves you can build an AI that autonomously manages your file system!
:::
""",
    7: """
::: {.panel-tabset}
## Agentic Failure Modes
When building agents, they will inevitably fail. They might get stuck in an infinite loop calling the same tool, or they might try to read a file that doesn't exist.

## Robust Error Handling
Today, you will review your Sacristan Agent's execution logs. You must implement `try/except` blocks in your Python tools so that if a tool fails (e.g., File Not Found), your code doesn't crash. Instead, your code should return the error *back to the AI* so the AI can realize its mistake and try a different approach!
:::
"""
}

fr_concepts_w2 = {
    1: """
::: {.panel-tabset}
## La Limite du Texte
Jusqu'à présent, vous avez construit des applications où l'IA ne répond qu'avec du texte ou du JSON. Bien que puissant, cela signifie que l'IA est piégée dans une boîte. Elle ne peut pas lire la météo, exécuter du code ou interagir avec le monde extérieur.

## Introduction au Function Calling
L'Appel de Fonctions (Function Calling, ou Tool Use) est le mécanisme qui permet à un LLM d'interagir avec des API externes et du code local. Au lieu que le modèle renvoie une chaîne de texte, vous lui fournissez une liste d'« outils » (fonctions) qu'il peut utiliser. S'il décide qu'il a besoin d'un outil, il renvoie une **requête d'appel de fonction** contenant les arguments nécessaires.

## Le Changement de Paradigme
Cela transforme l'IA d'un oracle passif en un Agent actif.
:::
""",
    2: """
::: {.panel-tabset}
## Comment l'IA connaît-elle les outils ?
Avant qu'une IA puisse appeler un outil, vous devez le définir. Dans l'API Gemini, cela se fait en passant un schéma de type OpenAPI ou en utilisant les annotations de type Python (Type Hints) pour décrire le but de la fonction.

## Écrire de Bonnes Descriptions
La partie la plus importante de la définition d'un outil est sa **description (docstring)**. L'IA se fie entièrement à votre description en langage naturel pour décider quand et comment utiliser l'outil.
:::
""",
    3: """
::: {.panel-tabset}
## La Boucle Agentique
Un Agent IA est simplement un modèle de langage enveloppé dans une boucle `while` avec un accès à des outils et à de la mémoire.

## La Logique Principale
1. **Prompt Utilisateur :** L'utilisateur pose une question.
2. **Décision de l'IA :** L'IA décide d'appeler `get_weather("Paris")`.
3. **Exécution :** Votre script Python exécute l'appel API réel et obtient `20°C`.
4. **Retour :** Votre script renvoie `20°C` à l'IA.
5. **Réponse Finale :** L'IA lit le résultat et formule sa réponse en langage naturel.
:::
""",
    4: """
::: {.panel-tabset}
## La Nature "Stateless" des LLMs
Par défaut, les LLMs sont amnésiques. Si vous posez une question, puis une question de suivi, le modèle ne se souvient pas de la première. Chaque appel API est isolé.

## Construire la Mémoire
Pour créer un agent conversationnel, vous devez maintenir manuellement le "Contexte". Cela implique de stocker chaque message utilisateur et chaque réponse du modèle dans un tableau, et de renvoyer l'*historique complet* au modèle à chaque tour.
:::
""",
    5: """
::: {.panel-tabset}
## Workflows Agentiques
Au lieu d'un seul agent massif qui essaie de tout faire, le Vibe Coding privilégie les workflows où plusieurs agents spécialisés collaborent.

- **Le Planificateur :** Décompose la tâche complexe en étapes.
- **Le Chercheur :** Navigue sur le web pour trouver des données.
- **Le Codeur :** Écrit un script basé sur ces données.

En séparant les responsabilités, vous réduisez considérablement les hallucinations et améliorez la robustesse du système.
:::
""",
    6: """
::: {.panel-tabset}
## Projet : L'Agent Sacristain
Un "Sacristain" est quelqu'un qui s'occupe de l'organisation et de l'entretien. Pour votre mini-projet, vous allez construire un "Agent Sacristain" pour votre ordinateur.

## L'Arsenal d'Outils
Vous l'équiperez d'outils Python pour : `list_directory(path)`, `read_file(path)` et `write_file(path, content)`.

## L'Objectif
L'agent devra inspecter un dossier, résumer son contenu et générer un rapport Markdown de manière autonome !
:::
""",
    7: """
::: {.panel-tabset}
## Gestion Robuste des Erreurs
Lors de la construction d'agents, ils échoueront inévitablement (ex: essayer de lire un fichier inexistant).
Vous devez implémenter des blocs `try/except` dans vos outils Python. Ainsi, si un outil échoue, votre code ne plante pas. Au lieu de cela, votre code renvoie l'erreur *à l'IA* pour qu'elle puisse réaliser son erreur et essayer une approche différente !
:::
"""
}
