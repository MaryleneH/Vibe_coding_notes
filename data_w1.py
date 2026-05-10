en_concepts_w1 = {
    1: """
::: {.panel-tabset}
## The Paradigm Shift
Welcome to the **Vibe Coding** mindset. Traditional software engineering demands that you type every single line of code, handle every semicolon, and construct logic manually. "Vibe coding" represents a paradigm shift where you transition from being a *typist* to a *director*.

You are no longer writing the code; you are defining the intent, the constraints, and the "vibe" of the application, while an AI model acts as your ultra-fast pair programmer. 

## The Role of the Director
Think of a movie director. They don't hold the camera or record the audio themselves. Instead, they provide the vision. In vibe coding:
1. **You provide the context:** "We are building a web server."
2. **You define the rules:** "It must use FastAPI and run on port 8000."
3. **The AI executes the vision:** It generates the code instantly.

## Why "Vibe"?
The term "vibe" refers to the intuition and high-level understanding of a system's architecture. Because models like Gemini are incredibly adept at pattern matching, they don't need you to explicitly define every variable. If you give them the right "vibe"—the architectural blueprint and the goal—they will synthesize the correct implementation.
:::
""",
    2: """
::: {.panel-tabset}
## Beyond Simple Questions
Many beginners treat AI like a search engine: "How do I reverse a string in Python?" While this works, it barely scratches the surface of what Large Language Models (LLMs) can do. Advanced Prompt Engineering is about structuring your instructions to maximize reasoning and accuracy.

## Few-Shot Prompting
LLMs are few-shot learners. This means that instead of just giving an instruction, you provide **examples** of the input and the expected output.
By providing examples, you constrain the model's output format and give it a "pattern" to follow, drastically reducing hallucinations.

## Chain-of-Thought (CoT)
"Chain-of-Thought" is a technique where you force the model to explain its reasoning step-by-step *before* it outputs the final answer.
For example, instead of asking "Is 5423 prime?", you prompt: "Think step-by-step. First, check if the number is even. Then, check divisibility up to its square root. Finally, state if it is prime." This drastically improves logical accuracy in complex coding tasks.
:::
""",
    3: """
::: {.panel-tabset}
## The Chaos of Text
LLMs naturally output unstructured text (Markdown, conversational filler, etc.). If you are building an application, you cannot programmatically parse a response that says: "Sure! Here is the data you requested: [data]". You need predictable, parsable data structures like JSON.

## Forcing JSON with Gemini
The Gemini API allows you to explicitly enforce a response schema. This means you can guarantee that the model will return a perfectly formatted JSON object that matches your exact specifications.

## Why this is a Superpower
Structured outputs are the bridge between AI and traditional software. Once an AI outputs JSON, you can:
- Save it to a database.
- Render it in a React UI.
- Pass it as arguments to another Python function.
This is the foundational step toward building autonomous agents!
:::
""",
    4: """
::: {.panel-tabset}
## Seeing the World
Gemini isn't just a text model; it is natively multimodal. It can "see" images, "listen" to audio, and "watch" video. This unlocks entirely new workflows for vibe coding.

## Image-to-Code
One of the most powerful vibe coding techniques is drawing a user interface on a whiteboard or a piece of paper, taking a picture, and asking Gemini to write the HTML/CSS/JS for it. 

## Beyond Images
You can also feed architectural diagrams to the model and ask it to generate the foundational boilerplate code. This bridges the gap between high-level system design and low-level implementation faster than ever before.
:::
""",
    5: """
::: {.panel-tabset}
## Moving to the IDE
Until now, you've likely been using web interfaces like Google AI Studio. Today, we transition to your Local Development Environment (IDE) like VS Code or Cursor.

## The Gemini SDK
To build real applications, your code needs to talk to the AI programmatically. We do this using the `google-generativeai` Python SDK. 

## Environment Variables
The most critical part of this transition is security. **Never hardcode your API keys.** You will learn how to use `.env` files to securely load your credentials, ensuring that when you push your code to GitHub, your keys remain safe.
:::
""",
    6: """
::: {.panel-tabset}
## Putting it Together
Today is about synthesis. You will combine your knowledge of the Gemini SDK, Prompt Engineering, and Structured Outputs to build a complete, functioning CLI (Command Line Interface) application.

## The Objective
You are no longer just writing snippets; you are architecting a loop. The application must:
1. Accept user input.
2. Formulate a prompt based on that input.
3. Call the Gemini API and enforce a JSON schema.
4. Parse the JSON and display it beautifully to the user.
:::
""",
    7: """
::: {.panel-tabset}
## The Power of Iteration
A core tenet of Vibe Coding is that your first draft is rarely your final draft. Because code generation is so fast, the cost of refactoring drops to near zero.

## Reviewing your Architecture
Look at the CLI app you built yesterday. How does it handle API timeouts? What if the user inputs gibberish? 
Today, your goal is to use Gemini to *critique* your own code and generate a more robust, error-handled version.
:::
"""
}

fr_concepts_w1 = {
    1: """
::: {.panel-tabset}
## Le Changement de Paradigme
Bienvenue dans l'état d'esprit **Vibe Coding**. L'ingénierie logicielle traditionnelle exige que vous tapiez chaque ligne de code, gériez chaque point-virgule et construisiez la logique manuellement. Le "vibe coding" représente un changement de paradigme où vous passez du rôle de *dactylographe* à celui de *réalisateur*.

Vous n'écrivez plus le code ; vous définissez l'intention, les contraintes et la "vibe" (l'ambiance/la direction) de l'application, tandis qu'un modèle d'IA agit comme votre binôme de programmation ultra-rapide.

## Le Rôle du Réalisateur
Pensez à un réalisateur de cinéma. Ils ne tiennent pas la caméra eux-mêmes. Au lieu de cela, ils fournissent la vision. Dans le vibe coding :
1. **Vous fournissez le contexte :** "Nous construisons un serveur web."
2. **Vous définissez les règles :** "Il doit utiliser FastAPI et s'exécuter sur le port 8000."
3. **L'IA exécute la vision :** Elle génère le code instantanément.

## Pourquoi "Vibe" ?
Le terme "vibe" fait référence à l'intuition et à la compréhension de haut niveau de l'architecture d'un système. Étant donné que les modèles comme Gemini sont incroyablement doués pour la reconnaissance de modèles, ils n'ont pas besoin que vous définissiez explicitement chaque variable. Si vous leur donnez la bonne "vibe", ils synthétiseront l'implémentation correcte.
:::
""",
    2: """
::: {.panel-tabset}
## Au-delà des Questions Simples
Beaucoup de débutants traitent l'IA comme un moteur de recherche. Bien que cela fonctionne, cela effleure à peine ce que les LLMs (Large Language Models) peuvent faire. L'Ingénierie de Prompt avancée (Prompt Engineering) consiste à structurer vos instructions pour maximiser le raisonnement et la précision.

## Few-Shot Prompting
Les LLMs sont capables d'apprendre avec peu d'exemples ("few-shot learners"). Cela signifie qu'au lieu de donner une simple instruction, vous fournissez des **exemples** d'entrées et de sorties attendues. Cela contraint le format de sortie du modèle et réduit considérablement les hallucinations.

## Chain-of-Thought (CoT)
La "Chaîne de Pensée" (Chain-of-Thought) est une technique où vous forcez le modèle à expliquer son raisonnement étape par étape *avant* de produire la réponse finale. Cela améliore considérablement la précision logique dans les tâches de codage complexes.
:::
""",
    3: """
::: {.panel-tabset}
## Le Chaos du Texte
Les LLMs produisent naturellement du texte non structuré (Markdown, remplissage conversationnel, etc.). Si vous construisez une application, vous ne pouvez pas analyser de manière programmatique une réponse de ce type. Vous avez besoin de structures de données prévisibles comme JSON.

## Forcer le JSON avec Gemini
L'API Gemini vous permet d'imposer explicitement un schéma de réponse ("Structured Outputs"). Cela signifie que vous pouvez garantir que le modèle renverra un objet JSON parfaitement formaté qui correspond à vos spécifications exactes.

## Pourquoi c'est un Superpouvoir
Les sorties structurées sont le pont entre l'IA et le logiciel traditionnel. Une fois qu'une IA produit du JSON, vous pouvez :
- Le sauvegarder dans une base de données.
- Le rendre dans une interface React.
- Le passer comme argument à une autre fonction Python.
:::
""",
    4: """
::: {.panel-tabset}
## Voir le Monde
Gemini n'est pas seulement un modèle textuel ; il est nativement multimodal. Il peut "voir" des images, "écouter" de l'audio et "regarder" des vidéos. Cela débloque de tout nouveaux workflows pour le vibe coding.

## De l'Image au Code
L'une des techniques de vibe coding les plus puissantes consiste à dessiner une interface utilisateur (UI) sur un tableau blanc, à prendre une photo et à demander à Gemini d'écrire le HTML/CSS/JS correspondant.

## Au-delà des Images
Vous pouvez également fournir des diagrammes architecturaux au modèle et lui demander de générer le code de base (boilerplate). Cela comble le fossé entre la conception système de haut niveau et l'implémentation de bas niveau plus rapidement que jamais.
:::
""",
    5: """
::: {.panel-tabset}
## Passage à l'IDE
Jusqu'à présent, vous avez probablement utilisé des interfaces web comme Google AI Studio. Aujourd'hui, nous passons à votre environnement de développement local (IDE) comme VS Code ou Cursor.

## Le SDK Gemini
Pour créer de vraies applications, votre code doit communiquer avec l'IA de manière programmatique. Nous faisons cela en utilisant le SDK Python `google-generativeai`.

## Variables d'Environnement
La partie la plus critique de cette transition est la sécurité. **Ne codez jamais vos clés API en dur.** Vous apprendrez à utiliser des fichiers `.env` pour charger vos informations d'identification en toute sécurité.
:::
""",
    6: """
::: {.panel-tabset}
## Tout Rassembler
Aujourd'hui est consacré à la synthèse. Vous allez combiner vos connaissances du SDK Gemini, de l'Ingénierie de Prompt et des Sorties Structurées pour créer une application CLI (Interface en Ligne de Commande) complète et fonctionnelle.

## L'Objectif
L'application doit :
1. Accepter l'entrée de l'utilisateur.
2. Formuler un prompt basé sur cette entrée.
3. Appeler l'API Gemini et imposer un schéma JSON.
4. Analyser le JSON et l'afficher joliment à l'utilisateur.
:::
""",
    7: """
::: {.panel-tabset}
## Le Pouvoir de l'Itération
Un principe fondamental du Vibe Coding est que votre premier jet est rarement votre jet final. Parce que la génération de code est si rapide, le coût du "refactoring" (remaniement du code) chute à presque zéro.

## Révision de votre Architecture
Aujourd'hui, votre objectif est d'utiliser Gemini pour *critiquer* votre propre code d'hier et générer une version plus robuste, avec une meilleure gestion des erreurs.
:::
"""
}
