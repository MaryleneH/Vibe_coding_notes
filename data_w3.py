en_concepts_w3 = {
    1: """
::: {.panel-tabset}
## The Copilot Paradigm
Up to this point, you have been writing your own Python code to manage the Gemini SDK. Now, we reverse the paradigm: you will use AI (like Cursor, GitHub Copilot, or Gemini in your IDE) to write the code *for* you.

## Writing Code with Natural Language
Instead of thinking about syntax (`for i in range()`), you must think about architecture. AI-assisted coding requires you to write extensive comments describing the input, the logic, and the expected output. The AI acts as your hands, typing out the implementation while you review and guide.
:::
""",
    2: """
::: {.panel-tabset}
## Test-Driven Vibe Coding
When AI writes your code, the biggest danger is silent failure. The code might look correct but contain subtle logic bugs. To counter this, we use Test-Driven Development (TDD) combined with Vibe Coding.

## The Workflow

1. You write a natural language prompt asking the AI to generate a PyTest file for a specific function (even if the function doesn't exist yet).
2. You ask the AI to generate the function.
3. You run the tests.
4. If they fail, you simply pass the error log back to the AI and ask it to fix the code. You loop this until all tests pass!
:::
""",
    3: """
::: {.panel-tabset}
## System Architecture
An Agent script running in your terminal is cool, but a real product needs a robust architecture. Today, we step back and design a full-stack system.

## Visualizing with Mermaid.js
Mermaid is a markdown-based diagramming tool. Because LLMs are text-native, they are incredibly good at generating Mermaid code. You can prompt Gemini: "Generate a Mermaid sequence diagram showing a user interacting with a React frontend, which calls a FastAPI backend, which triggers the Community Manager Agent." This allows you to rapidly prototype system designs.
:::
""",
    4: """
::: {.panel-tabset}
## Generating User Interfaces
Frontend development often involves hours of tweaking CSS and HTML. With Vibe Coding, you can bypass this completely.

## The Workflow
You can take a screenshot of an existing app you like, or draw a wireframe, and prompt Gemini: "Build a responsive React component using Tailwind CSS that looks like this image. Ensure it has a chat input box and a message history area."
You are moving from a Backend Engineer to a Full-Stack Engineer by leveraging the AI's vast knowledge of UI components.
:::
""",
    5: """
::: {.panel-tabset}
## Connecting the Stack
Now you have a Python Agent backend and an AI-generated frontend UI. Today is about bridging the gap.

## The API Layer
You will use a lightweight framework like Flask or FastAPI to wrap your Community Manager Agent. You will expose a REST endpoint (e.g., `POST /generate_video`) that accepts the user's prompt from the UI, passes it to the Agent loop, and returns the Agent's finalized video assets (script, images, audio) back to the frontend.
:::
""",
    6: """
::: {.panel-tabset}
## Final Project Polish
A great product is all about the details. Your Community Manager Agent works, but how is the User Experience (UX)?

## Exposing the "Thoughts"
When an Agent executes tools (like generating an image or synthesizing audio), it can take several seconds. If the UI is static, the user thinks the app is broken. You will update your Agent to yield its "internal thoughts" (e.g., 'Calling Imagen to generate background...') and display them in the UI as a loading state. This dramatically improves the UX.
:::
""",
    7: """
::: {.panel-tabset}
## Deploying to Production
It's time to share your creation with the world! A local app is a toy; a deployed app is a product.

## Free Hosting Solutions
You will learn how to deploy your FastAPI backend to services like Render or Heroku, and how to host your frontend UI on GitHub Pages or Vercel. 
Congratulations! You have completed the Vibe Coding Mastery curriculum. You have transformed from a traditional coder into an Agentic AI Architect.
:::
"""
}

fr_concepts_w3 = {
    1: """
::: {.panel-tabset}
## Le Paradigme du Copilote
Jusqu'à présent, vous avez écrit votre propre code Python pour gérer le SDK Gemini. Maintenant, nous inversons le paradigme : vous allez utiliser l'IA (comme Cursor ou GitHub Copilot) pour écrire le code *pour* vous.

## Écrire du Code en Langage Naturel
Au lieu de penser à la syntaxe, vous devez penser à l'architecture. Le codage assisté par l'IA exige que vous écriviez des commentaires détaillés décrivant l'entrée, la logique et la sortie attendue. L'IA agit comme vos mains, tapant l'implémentation pendant que vous guidez.
:::
""",
    2: """
::: {.panel-tabset}
## Vibe Coding Dirigé par les Tests (TDD)
Lorsque l'IA écrit votre code, le plus grand danger est l'échec silencieux (des bugs logiques subtils). Pour contrer cela, nous utilisons le Développement Dirigé par les Tests (TDD) combiné au Vibe Coding.

## Le Workflow

1. Demandez à l'IA de générer des tests PyTest pour une fonction.
2. Demandez à l'IA de générer la fonction.
3. Exécutez les tests. S'ils échouent, passez le journal d'erreurs à l'IA pour qu'elle corrige le code. Bouclez jusqu'à ce que tout passe !
:::
""",
    3: """
::: {.panel-tabset}
## Architecture Système
Un script d'Agent exécuté dans votre terminal est génial, mais un vrai produit a besoin d'une architecture robuste.

## Visualisation avec Mermaid.js
Parce que les LLMs sont natifs du texte, ils sont incroyablement doués pour générer du code Mermaid (un outil de diagramme basé sur Markdown). Vous pouvez prototyper rapidement des conceptions de systèmes en demandant à Gemini de générer des diagrammes de séquence illustrant un utilisateur interagissant avec un frontend React, qui appelle un backend FastAPI, qui déclenche l'Agent Community Manager.
:::
""",
    4: """
::: {.panel-tabset}
## Génération d'Interfaces Utilisateur (UIs)
Le développement Frontend implique souvent des heures de réglages CSS. Avec le Vibe Coding, vous pouvez contourner cela.

## Le Workflow
Vous pouvez prendre une capture d'écran d'une application que vous aimez et demander à Gemini : "Construisez un composant React réactif utilisant Tailwind CSS qui ressemble à cette image."
Vous passez d'Ingénieur Backend à Ingénieur Full-Stack grâce à l'IA.
:::
""",
    5: """
::: {.panel-tabset}
## Connecter la Stack
Vous avez maintenant un backend Agent Python et une UI frontend générée par l'IA. Aujourd'hui, il s'agit de faire le pont.

## La Couche API
Vous utiliserez un framework léger comme Flask ou FastAPI pour envelopper votre Agent Community Manager. Vous exposerez un point de terminaison REST qui accepte le prompt de l'utilisateur, le transmet à la boucle de l'Agent et renvoie les assets vidéo finalisés (scénario, images, audio) au frontend.
:::
""",
    6: """
::: {.panel-tabset}
## Finalisation du Projet
Un bon produit se joue dans les détails. Votre Agent Community Manager fonctionne, mais comment est l'Expérience Utilisateur (UX) ?

## Exposer les "Pensées"
Lorsqu'un Agent exécute des outils (comme générer une image ou synthétiser de l'audio), cela peut prendre plusieurs secondes. Vous mettrez à jour votre Agent pour qu'il transmette ses "pensées internes" (ex: 'Appel d'Imagen pour générer l'arrière-plan...') et les afficher dans l'UI comme état de chargement.
:::
""",
    7: """
::: {.panel-tabset}
## Déploiement en Production
Il est temps de partager votre création avec le monde ! Une application locale est un jouet ; une application déployée est un produit.

## Solutions d'Hébergement Gratuit
Vous apprendrez comment déployer votre backend FastAPI sur des services comme Render et comment héberger votre interface UI sur GitHub Pages.
Félicitations ! Vous avez terminé le programme Vibe Coding Mastery. Vous êtes passé d'un codeur traditionnel à un Architecte IA Agentique.
:::
"""
}
