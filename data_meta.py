# --- DATA: META ---
en_home = """---
title: "Welcome to Vibe Coding"
subtitle: "A 21-Day Journey to Agentic AI Mastery"
page-layout: full
title-block-banner: true
---

:::{.grid}
:::{.g-col-12 .g-col-md-8}
## 🚀 The Future of Coding is Here
Welcome to the Vibe Coding Mastery curriculum. In just 3 weeks (2 hours a day), you will learn how to leverage Google AI Studio, the Gemini Python SDK, and natural language to build powerful, real-world AI agents and applications.

This isn't just about writing code—it's about directing an AI to write it with you.

### What You'll Achieve

- **Week 1:** Master the art of advanced prompting and structured outputs.
- **Week 2:** Give your AI tools, memory, and agency to perform real-world tasks.
- **Week 3:** Build full-stack applications and deploy your intelligent Community Manager Agent.

<br>
<a href="week1/day1.qmd" class="btn btn-primary btn-lg" style="border-radius: 50px; padding: 10px 30px; font-weight: 600; box-shadow: 0 4px 15px rgba(26,115,232,0.4);">Start Your Journey →</a>
:::

:::{.g-col-12 .g-col-md-4}
:::{.callout-note appearance="simple" icon="false" style="border-radius: 15px; padding: 20px;"}
### 🛠️ Prerequisites

- Python installed (`>= 3.10`)
- A Google Account for [Google AI Studio](https://aistudio.google.com/)
- An IDE (VS Code or Cursor)
- A basic understanding of logic
:::

:::{.callout-tip appearance="simple" icon="false" style="border-radius: 15px; padding: 20px; margin-top: 15px;"}
### ⏱️ Time Commitment
Just **2 hours a day**. We focus on high-impact concepts and hands-on mini-projects to solidify your understanding.
:::
:::
:::
"""

fr_home = """---
title: "Bienvenue dans Vibe Coding"
subtitle: "Un voyage de 21 jours vers la maîtrise de l'IA Agentique"
page-layout: full
title-block-banner: true
---

:::{.grid}
:::{.g-col-12 .g-col-md-8}
## 🚀 Le futur du code est là
Bienvenue dans le programme Vibe Coding Mastery. En seulement 3 semaines (2 heures par jour), vous apprendrez à utiliser Google AI Studio, le SDK Python Gemini et le langage naturel pour créer de puissants agents et applications d'IA.

Il ne s'agit pas seulement d'écrire du code, mais de diriger une IA pour qu'elle l'écrive avec vous.

### Ce que vous allez accomplir

- **Semaine 1 :** Maîtriser l'art du "Prompt Engineering" avancé et des "Structured Outputs".
- **Semaine 2 :** Donner à votre IA des "tools", de la mémoire et une agentivité pour accomplir des tâches réelles.
- **Semaine 3 :** Créer des applications full-stack et déployer votre "Agent Community Manager" intelligent.

<br>
<a href="week1/day1.qmd" class="btn btn-primary btn-lg" style="border-radius: 50px; padding: 10px 30px; font-weight: 600; box-shadow: 0 4px 15px rgba(26,115,232,0.4);">Commencer votre voyage →</a>
:::

:::{.g-col-12 .g-col-md-4}
:::{.callout-note appearance="simple" icon="false" style="border-radius: 15px; padding: 20px;"}
### 🛠️ Prérequis

- Python installé (`>= 3.10`)
- Un compte Google pour [Google AI Studio](https://aistudio.google.com/)
- Un IDE (VS Code ou Cursor)
- Une compréhension de base de la logique de programmation
:::

:::{.callout-tip appearance="simple" icon="false" style="border-radius: 15px; padding: 20px; margin-top: 15px;"}
### ⏱️ Temps requis
Seulement **2 heures par jour**. Nous nous concentrons sur les concepts à fort impact et des mini-projets pratiques pour consolider votre compréhension.
:::
:::
:::
"""

en_titles = {
    "week1": ["Foundations", "The Vibe Coding Mindset", "Advanced Prompt Engineering & Reasoning", "Structured Outputs", "Multimodal Magic", "Transitioning to Code", "Mini-Project 1", "Review & Rest"],
    "week2": ["Agents", "Introduction to Function Calling", "Defining Tools", "Building your First Agent", "Context & Memory", "Agentic Workflows", "Mini-Project 2: Community Manager Agent", "Review & Rest"],
    "week3": ["Advanced & Deploy", "AI-Assisted Coding", "Test-Driven Vibe Coding", "System Architecture", "Generating UIs", "Integrating the CM Agent", "Final Project Polish", "Deploying & Wrap-up"]
}

fr_titles = {
    "week1": ["Fondations", "L'état d'esprit Vibe Coding", "Prompt Engineering Avancé & Raisonnement", "Structured Outputs", "Magie Multimodale", "Transition vers le Code", "Mini-Projet 1", "Révision & Repos"],
    "week2": ["Agents", "Introduction au Function Calling", "Définition de Tools", "Construire votre Premier Agent", "Contexte & Mémoire", "Workflows Agentiques", "Mini-Projet 2 : Agent Community Manager", "Révision & Repos"],
    "week3": ["Avancé & Déploiement", "Codage Assisté par l'IA", "Test-Driven Vibe Coding", "Architecture Système", "Génération d'Interfaces Utilisateur (UIs)", "Intégration de l'Agent CM", "Finalisation du Projet", "Déploiement & Conclusion"]
}

en_exercises = {
    "week1": [
        "",
        "**Task:** Write a natural language prompt that acts as a 'Vibe Coding' mentor. Have Gemini explain a complex sorting algorithm to you as if you were pair programming.",
        "**Task:** Use few-shot prompting and chain-of-thought to solve a complex logic puzzle with Gemini. Provide at least 3 examples in your prompt.",
        "**Task:** Force Gemini to output a strict JSON schema for a 'User Profile' including name, age, and occupation using the `response_schema` parameter.",
        "**Task:** Pass an image of a handwritten UI sketch to Gemini and ask it to output the corresponding HTML/CSS.",
        "**Task:** Write a Python script using the Gemini SDK that takes a user query and returns a response. Securely load your API keys using `dotenv`.",
        "**Task:** Build a CLI flashcard generator. The user provides a topic, Gemini generates 5 Q&A pairs in JSON format, and your script quizzes the user interactively.",
        "**Task:** Reflect on Week 1. Refactor your CLI flashcard generator to improve the prompt, add robust error handling, and support scoring."
    ],
    "week2": [
        "",
        "**Task:** Define a Python function that gets the current weather (mocked). Prompt Gemini and observe how it constructs a function call request instead of a text response.",
        "**Task:** Create an OpenAPI-style tool schema for a 'Calculator' function. Pass it to Gemini and test it with a complex math query.",
        "**Task:** Write a script where Gemini can call the 'Calculator' tool, execute the function locally, return the result to Gemini, and formulate a final answer.",
        "**Task:** Implement a simple chat loop array that stores User and Model messages, passing the full history to Gemini on each turn to maintain context.",
        "**Task:** Design a workflow with a Planner agent (breaks down a task) and an Executor agent (writes the code). Run them in sequence.",
        "**Task:** Build the core of the Community Manager Agent: give it tools to call Gemini (for scripting), Imagen (for images), and Google TTS (for voiceover). Test it with a romance author prompt.",
        "**Task:** Review the Community Manager Agent's tool execution logs. Add error handling for when the agent hits an API quota limit or a content moderation block."
    ],
    "week3": [
        "",
        "**Task:** Use an IDE (like Cursor) to refactor the Community Manager Agent code using just natural language 'vibes' to improve modularity.",
        "**Task:** Write a natural language prompt that generates PyTest cases for your 'Calculator' tool. Then use Gemini to fix any failing tests.",
        "**Task:** Design the architecture for a web-based version of the Community Manager Agent. Draw a mermaid.js diagram using Gemini.",
        "**Task:** Prompt Gemini to generate a complete React/Vite (or simple HTML/JS) frontend UI for interacting with your agent.",
        "**Task:** Connect your generated UI to your Python agent backend via a simple Flask or FastAPI REST server.",
        "**Task:** Add an 'Assemble Video' tool to your agent and update the UI to visually display the generated script, image storyboards, and audio track.",
        "**Task:** Deploy your backend to a free service (e.g., Render) and your UI to GitHub Pages. Test the live agent in production!"
    ]
}

fr_exercises = {
    "week1": [
        "",
        "**Tâche :** Écrivez un prompt en langage naturel qui agit comme un mentor 'Vibe Coding'. Demandez à Gemini de vous expliquer un algorithme de tri complexe comme si vous faisiez du 'pair programming'.",
        "**Tâche :** Utilisez le 'few-shot prompting' et le 'chain-of-thought' pour résoudre un puzzle logique complexe avec Gemini. Fournissez au moins 3 exemples dans votre prompt.",
        "**Tâche :** Forcez Gemini à générer un schéma JSON strict pour un 'Profil Utilisateur' incluant nom, âge et profession en utilisant le paramètre `response_schema`.",
        "**Tâche :** Passez l'image d'un croquis d'interface utilisateur (UI) fait à la main à Gemini et demandez-lui de générer le code HTML/CSS correspondant.",
        "**Tâche :** Écrivez un script Python utilisant le SDK Gemini qui prend une requête utilisateur et renvoie une réponse. Chargez vos clés API en toute sécurité en utilisant `dotenv`.",
        "**Tâche :** Créez un générateur de flashcards en ligne de commande. L'utilisateur fournit un sujet, Gemini génère 5 paires de Q/R au format JSON, et votre script interroge l'utilisateur de manière interactive.",
        "**Tâche :** Réfléchissez sur la Semaine 1. Refactorez votre générateur de flashcards pour améliorer le prompt, ajouter une gestion robuste des erreurs et gérer un score."
    ],
    "week2": [
        "",
        "**Tâche :** Définissez une fonction Python qui obtient la météo actuelle (simulée). Envoyez un prompt à Gemini et observez comment il construit une requête d'appel de fonction au lieu d'une réponse textuelle.",
        "**Tâche :** Créez un schéma de 'tool' de style OpenAPI pour une fonction 'Calculatrice'. Passez-le à Gemini et testez-le avec une requête mathématique complexe.",
        "**Tâche :** Écrivez un script où Gemini peut appeler le 'tool' Calculatrice, exécuter la fonction localement, renvoyer le résultat à Gemini, et formuler une réponse finale.",
        "**Tâche :** Implémentez un tableau de boucle de discussion (chat loop) qui stocke les messages Utilisateur et Modèle, en passant tout l'historique à Gemini à chaque tour pour maintenir le contexte.",
        "**Tâche :** Concevez un workflow avec un agent Planificateur (qui décompose une tâche) et un agent Exécuteur (qui écrit le code). Exécutez-les en séquence.",
        "**Tâche :** Construisez le cœur de l'Agent Community Manager : donnez-lui des 'tools' pour appeler Gemini (scénario), Imagen (images) et Google TTS (voix off). Testez-le avec un prompt d'auteur de romance.",
        "**Tâche :** Passez en revue les logs d'exécution des 'tools' de l'Agent. Ajoutez une gestion des erreurs pour les cas où l'agent atteint une limite de quota API ou un blocage de modération de contenu."
    ],
    "week3": [
        "",
        "**Tâche :** Utilisez un IDE (comme Cursor) pour refactorer le code de l'Agent Community Manager en utilisant uniquement des instructions en langage naturel ('vibes') afin d'améliorer la modularité.",
        "**Tâche :** Écrivez un prompt en langage naturel qui génère des cas de test PyTest pour votre 'tool' Calculatrice. Utilisez ensuite Gemini pour corriger les tests qui échouent.",
        "**Tâche :** Concevez l'architecture d'une version web de l'Agent Community Manager. Dessinez un diagramme mermaid.js en utilisant Gemini.",
        "**Tâche :** Demandez à Gemini de générer une interface utilisateur frontend complète en React/Vite (ou simplement HTML/JS) pour interagir avec votre agent.",
        "**Tâche :** Connectez l'interface générée au backend Python de votre agent via un simple serveur REST Flask ou FastAPI.",
        "**Tâche :** Ajoutez un 'tool' 'Assembler la Vidéo' à votre agent et mettez à jour l'interface pour afficher visuellement le scénario généré, les images du storyboard et la piste audio.",
        "**Tâche :** Déployez votre backend sur un service gratuit (ex: Render) et votre UI sur GitHub Pages. Testez l'agent en production !"
    ]
}
