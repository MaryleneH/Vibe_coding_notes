import os
import shutil

def create_file(path, content):
    os.makedirs(os.path.dirname(path) if os.path.dirname(path) else '.', exist_ok=True)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content.strip() + '\n')

base_dir = r"c:\Users\maryl\2 - Side work\11 - My resume\vibe_coding_notes"

# Clean up old root directories
for old_week in ["week1", "week2", "week3"]:
    old_path = os.path.join(base_dir, old_week)
    if os.path.exists(old_path):
        shutil.rmtree(old_path)

# --- QUARTO CONFIG ---
quarto_yml = """project:
  type: website
  output-dir: docs

website:
  title: "Vibe Coding Mastery"
  description: "Learn to vibe code real apps and AI agents in 3 weeks using Google tools."
  site-url: "https://maryleneh.github.io/Vibe_coding_notes/"
  search: true
  
  navbar:
    background: primary
    left:
      - href: index.qmd
        text: "🌍 Language / Langue"
  
  sidebar:
    - id: en
      title: "English Curriculum"
      style: "docked"
      search: true
      collapse-level: 1
      contents:
        - en/index.qmd
        - section: "Week 1: Foundations"
          href: en/week1/index.qmd
          contents:
            - en/week1/day1.qmd
            - en/week1/day2.qmd
            - en/week1/day3.qmd
            - en/week1/day4.qmd
            - en/week1/day5.qmd
            - en/week1/day6.qmd
            - en/week1/day7.qmd
        - section: "Week 2: Agents"
          href: en/week2/index.qmd
          contents:
            - en/week2/day1.qmd
            - en/week2/day2.qmd
            - en/week2/day3.qmd
            - en/week2/day4.qmd
            - en/week2/day5.qmd
            - en/week2/day6.qmd
            - en/week2/day7.qmd
        - section: "Week 3: Advanced & Deploy"
          href: en/week3/index.qmd
          contents:
            - en/week3/day1.qmd
            - en/week3/day2.qmd
            - en/week3/day3.qmd
            - en/week3/day4.qmd
            - en/week3/day5.qmd
            - en/week3/day6.qmd
            - en/week3/day7.qmd

    - id: fr
      title: "Programme Français"
      style: "docked"
      search: true
      collapse-level: 1
      contents:
        - fr/index.qmd
        - section: "Semaine 1 : Fondations"
          href: fr/week1/index.qmd
          contents:
            - fr/week1/day1.qmd
            - fr/week1/day2.qmd
            - fr/week1/day3.qmd
            - fr/week1/day4.qmd
            - fr/week1/day5.qmd
            - fr/week1/day6.qmd
            - fr/week1/day7.qmd
        - section: "Semaine 2 : Agents"
          href: fr/week2/index.qmd
          contents:
            - fr/week2/day1.qmd
            - fr/week2/day2.qmd
            - fr/week2/day3.qmd
            - fr/week2/day4.qmd
            - fr/week2/day5.qmd
            - fr/week2/day6.qmd
            - fr/week2/day7.qmd
        - section: "Semaine 3 : Avancé & Déploiement"
          href: fr/week3/index.qmd
          contents:
            - fr/week3/day1.qmd
            - fr/week3/day2.qmd
            - fr/week3/day3.qmd
            - fr/week3/day4.qmd
            - fr/week3/day5.qmd
            - fr/week3/day6.qmd
            - fr/week3/day7.qmd

  page-footer:
    center: "Vibe Coding Mastery - 3 Week Journey"

format:
  html:
    theme:
      dark: [darkly, styles.scss]
      light: [cosmo, styles.scss]
    css: styles.scss
    toc: true
    toc-depth: 3
    code-copy: true
    highlight-style: github-dark
    include-after-body: progress.html
"""

# --- LANGUAGE PORTAL ---
portal_qmd = """---
title: "Welcome to Vibe Coding Mastery"
page-layout: full
title-block-banner: true
---

:::{.grid}
:::{.g-col-12 .g-col-md-6 style="text-align: center; padding: 40px;"}
## 🇬🇧 English
**A 21-Day Journey to Agentic AI Mastery**

Learn to leverage Google AI Studio and the Gemini Python SDK to build powerful, real-world AI agents and applications.
<br><br>
<a href="en/index.qmd" class="btn btn-primary btn-lg" style="border-radius: 50px; padding: 15px 40px; font-weight: 600;">Enter English Site →</a>
:::

:::{.g-col-12 .g-col-md-6 style="text-align: center; padding: 40px;"}
## 🇫🇷 Français
**Un voyage de 21 jours vers la maîtrise de l'IA Agentique**

Apprenez à utiliser Google AI Studio et le SDK Python Gemini pour créer des agents IA et des applications concrètes et puissantes.
<br><br>
<a href="fr/index.qmd" class="btn btn-primary btn-lg" style="border-radius: 50px; padding: 15px 40px; font-weight: 600;">Entrer sur le site Français →</a>
:::
:::
"""

# --- DATA: ENGLISH ---
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
- **Week 3:** Build full-stack applications and deploy your intelligent Sacristan Agent.

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

en_titles = {
    "week1": ["Foundations", "The Vibe Coding Mindset", "Advanced Prompt Engineering & Reasoning", "Structured Outputs", "Multimodal Magic", "Transitioning to Code", "Mini-Project 1", "Review & Rest"],
    "week2": ["Agents", "Introduction to Function Calling", "Defining Tools", "Building your First Agent", "Context & Memory", "Agentic Workflows", "Mini-Project 2: Sacristan Agent", "Review & Rest"],
    "week3": ["Advanced & Deploy", "AI-Assisted Coding", "Test-Driven Vibe Coding", "System Architecture", "Generating UIs", "Integrating the Sacristan Agent", "Final Project Polish", "Deploying & Wrap-up"]
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
        "**Task:** Build the core of the Sacristan Agent: give it tools to read local files, list directories, and write small notes. Test it on a dummy directory.",
        "**Task:** Review the Sacristan Agent's tool execution logs. Add error handling for when the agent tries to read a non-existent file or write invalid data."
    ],
    "week3": [
        "",
        "**Task:** Use an IDE (like Cursor) to refactor the Sacristan Agent code using just natural language 'vibes' to improve modularity.",
        "**Task:** Write a natural language prompt that generates PyTest cases for your 'Calculator' tool. Then use Gemini to fix any failing tests.",
        "**Task:** Design the architecture for a web-based version of the Sacristan Agent. Draw a mermaid.js diagram using Gemini.",
        "**Task:** Prompt Gemini to generate a complete React/Vite (or simple HTML/JS) frontend UI for interacting with your agent.",
        "**Task:** Connect your generated UI to your Python agent backend via a simple Flask or FastAPI REST server.",
        "**Task:** Add an 'Export to Markdown' tool to your agent and update the UI to visually display the agent's internal thinking steps.",
        "**Task:** Deploy your backend to a free service (e.g., Render) and your UI to GitHub Pages. Test the live agent in production!"
    ]
}

# --- DATA: FRENCH ---
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
- **Semaine 3 :** Créer des applications full-stack et déployer votre "Agent Sacristain" intelligent.

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

fr_titles = {
    "week1": ["Fondations", "L'état d'esprit Vibe Coding", "Prompt Engineering Avancé & Raisonnement", "Structured Outputs", "Magie Multimodale", "Transition vers le Code", "Mini-Projet 1", "Révision & Repos"],
    "week2": ["Agents", "Introduction au Function Calling", "Définition de Tools", "Construire votre Premier Agent", "Contexte & Mémoire", "Workflows Agentiques", "Mini-Projet 2 : Agent Sacristain", "Révision & Repos"],
    "week3": ["Avancé & Déploiement", "Codage Assisté par l'IA", "Test-Driven Vibe Coding", "Architecture Système", "Génération d'Interfaces Utilisateur (UIs)", "Intégration de l'Agent Sacristain", "Finalisation du Projet", "Déploiement & Conclusion"]
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
        "**Tâche :** Construisez le cœur de l'Agent Sacristain : donnez-lui des 'tools' pour lire des fichiers locaux, lister des répertoires et écrire de petites notes. Testez-le sur un répertoire factice.",
        "**Tâche :** Passez en revue les logs d'exécution des 'tools' de l'Agent Sacristain. Ajoutez une gestion des erreurs pour les cas où l'agent essaie de lire un fichier inexistant ou d'écrire des données non valides."
    ],
    "week3": [
        "",
        "**Tâche :** Utilisez un IDE (comme Cursor) pour refactorer le code de l'Agent Sacristain en utilisant uniquement des instructions en langage naturel ('vibes') afin d'améliorer la modularité.",
        "**Tâche :** Écrivez un prompt en langage naturel qui génère des cas de test PyTest pour votre 'tool' Calculatrice. Utilisez ensuite Gemini pour corriger les tests qui échouent.",
        "**Tâche :** Concevez l'architecture d'une version web de l'Agent Sacristain. Dessinez un diagramme mermaid.js en utilisant Gemini.",
        "**Tâche :** Demandez à Gemini de générer une interface utilisateur frontend complète en React/Vite (ou simplement HTML/JS) pour interagir avec votre agent.",
        "**Tâche :** Connectez l'interface générée au backend Python de votre agent via un simple serveur REST Flask ou FastAPI.",
        "**Tâche :** Ajoutez un 'tool' 'Exporter vers Markdown' à votre agent et mettez à jour l'interface pour afficher visuellement les étapes de raisonnement interne de l'agent.",
        "**Tâche :** Déployez votre backend sur un service gratuit (ex: Render) et votre UI sur GitHub Pages. Testez l'agent en production !"
    ]
}

styles_scss = """/*-- scss:defaults --*/
$font-family-sans-serif: 'Outfit', 'Inter', 'Roboto', sans-serif;

/*-- scss:rules --*/
@import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;600;800&family=Inter:wght@400;600&display=swap');

body {
  font-family: $font-family-sans-serif;
  letter-spacing: -0.01em;
  line-height: 1.6;
}

/* Default Light Mode Colors */
:root {
  --glass-nav-bg: rgba(255, 255, 255, 0.85);
  --glass-sidebar-bg: rgba(250, 250, 250, 0.8);
  --glass-border: rgba(0, 0, 0, 0.05);
  --heading-gradient: -webkit-linear-gradient(45deg, #202124, #1a73e8);
  --title-gradient: -webkit-linear-gradient(45deg, #1a73e8, #9333ea, #ec4899);
  --callout-bg: rgba(0,0,0,0.02);
  --callout-border: rgba(0,0,0,0.05);
  --code-bg: #f8f9fa;
  --inline-code-bg: rgba(0, 0, 0, 0.05);
  --inline-code-color: #d63384;
  --hover-shadow: rgba(26, 115, 232, 0.4);
}

/* Dark Mode Colors */
[data-bs-theme="dark"], body.quarto-dark {
  --glass-nav-bg: rgba(18, 18, 18, 0.7);
  --glass-sidebar-bg: rgba(20, 20, 20, 0.6);
  --glass-border: rgba(255, 255, 255, 0.05);
  --heading-gradient: -webkit-linear-gradient(45deg, #e8eaed, #8ab4f8);
  --title-gradient: -webkit-linear-gradient(45deg, #ffffff, #8ab4f8, #c58af9);
  --callout-bg: rgba(255,255,255,0.03);
  --callout-border: rgba(255,255,255,0.08);
  --code-bg: #1e1e1e;
  --inline-code-bg: rgba(255, 255, 255, 0.1);
  --inline-code-color: #ff7eb6;
  --hover-shadow: rgba(138, 180, 248, 0.6);
}

/* Glassmorphism Navbar */
.navbar {
  background: var(--glass-nav-bg) !important;
  backdrop-filter: blur(12px);
  -webkit-backdrop-filter: blur(12px);
  border-bottom: 1px solid var(--glass-border);
  box-shadow: 0 4px 30px rgba(0, 0, 0, 0.05);
}

/* Glassmorphism Sidebar */
.sidebar {
  background: var(--glass-sidebar-bg) !important;
  backdrop-filter: blur(12px);
  -webkit-backdrop-filter: blur(12px);
  border-right: 1px solid var(--glass-border);
}

/* Typography & Colors */
h1, h2, h3, h4, h5 {
  font-family: 'Outfit', sans-serif;
  font-weight: 600;
  background: var(--heading-gradient);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  margin-bottom: 1rem;
}

/* Specific override for banner title to look amazing */
.quarto-title-block .title {
  font-weight: 800;
  font-size: 3rem;
  background: var(--title-gradient);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}

/* Modern Card/Callout styles */
.callout {
  border-radius: 12px;
  background: var(--callout-bg);
  border: 1px solid var(--callout-border);
  box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.05);
  backdrop-filter: blur(4px);
}

/* Code Blocks */
pre.sourceCode {
  border-radius: 12px;
  background-color: var(--code-bg) !important;
  border: 1px solid var(--glass-border);
}

code {
  background-color: var(--inline-code-bg);
  color: var(--inline-code-color);
  border-radius: 4px;
  padding: 0.15em 0.3em;
}
pre code {
  background-color: transparent;
  color: inherit;
}

/* Micro-animations */
a {
  transition: all 0.3s ease;
}
a:hover {
  text-shadow: 0 0 8px var(--hover-shadow);
}

.btn-primary {
  transition: transform 0.2s ease, box-shadow 0.2s ease;
}
.btn-primary:hover {
  transform: translateY(-2px);
  box-shadow: 0 6px 20px var(--hover-shadow) !important;
}
"""

progress_html = """<div id="progress-container" style="margin-top: 60px; padding: 30px; border-top: 1px solid rgba(255,255,255,0.1); text-align: center;">
  <button id="mark-complete-btn" class="btn btn-outline-primary" style="display:none; border-radius: 30px; padding: 10px 25px; font-weight: 600; transition: all 0.3s ease;" onclick="toggleComplete()">Mark as Complete</button>
</div>
<script>
  document.addEventListener("DOMContentLoaded", function() {
    const path = window.location.pathname;
    if (path.includes("day")) {
      const btn = document.getElementById("mark-complete-btn");
      if(btn) {
          btn.style.display = "inline-block";
          const isComplete = localStorage.getItem("completed_" + path);
          if (isComplete === "true") {
            btn.innerHTML = "✨ Completed";
            btn.classList.replace("btn-outline-primary", "btn-success");
            btn.style.boxShadow = "0 0 15px rgba(52, 168, 83, 0.4)";
          }
      }
    }
  });

  function toggleComplete() {
    const path = window.location.pathname;
    const isComplete = localStorage.getItem("completed_" + path) === "true";
    const btn = document.getElementById("mark-complete-btn");
    
    if (isComplete) {
      localStorage.setItem("completed_" + path, "false");
      btn.innerHTML = "Mark as Complete";
      btn.classList.replace("btn-success", "btn-outline-primary");
      btn.style.boxShadow = "none";
    } else {
      localStorage.setItem("completed_" + path, "true");
      btn.innerHTML = "✨ Completed";
      btn.classList.replace("btn-outline-primary", "btn-success");
      btn.style.boxShadow = "0 0 15px rgba(52, 168, 83, 0.4)";
    }
  }
</script>
"""

# Create Base Files
create_file(os.path.join(base_dir, "_quarto.yml"), quarto_yml)
create_file(os.path.join(base_dir, "index.qmd"), portal_qmd)
create_file(os.path.join(base_dir, "styles.scss"), styles_scss)
create_file(os.path.join(base_dir, "progress.html"), progress_html)

# Create Language Content
for lang, home_content, titles, exercises in [
    ("en", en_home, en_titles, en_exercises),
    ("fr", fr_home, fr_titles, fr_exercises)
]:
    lang_dir = os.path.join(base_dir, lang)
    create_file(os.path.join(lang_dir, "index.qmd"), home_content)
    
    w_str = "Week" if lang == "en" else "Semaine"
    overview_title = "Overview" if lang == "en" else "Aperçu"
    day_str = "Day" if lang == "en" else "Jour"
    learning_obj_title = "🎯 Learning Objectives" if lang == "en" else "🎯 Objectifs d'Apprentissage"
    core_concepts_title = "📖 Core Concepts" if lang == "en" else "📖 Concepts Clés"
    hands_on_title = "💻 Hands-on Exercise" if lang == "en" else "💻 Exercice Pratique"
    wrap_up_title = "✅ Wrap-up" if lang == "en" else "✅ Conclusion"
    
    for week in ["week1", "week2", "week3"]:
        week_dir = os.path.join(lang_dir, week)
        week_titles = titles[week]
        
        # Create week index
        week_num = week[-1]
        welcome_str = f"Welcome to {w_str} {week_num}" if lang == "en" else f"Bienvenue dans la {w_str} {week_num}"
        
        index_content = f"""---
title: "{w_str} {week_num}: {week_titles[0]}"
---

# {week_titles[0]} {overview_title}

{welcome_str} ! 

{"This week, we will focus on" if lang=="en" else "Cette semaine, nous allons nous concentrer sur"} **{week_titles[0]}**.

### {"What to Expect" if lang=="en" else "À quoi s'attendre"}

- **{"Daily Mini-Lessons" if lang=="en" else "Mini-Leçons Quotidiennes"}:** {"2-hour segments focusing on a specific concept." if lang=="en" else "Segments de 2 heures axés sur un concept spécifique."}
- **{"Hands-on Practice" if lang=="en" else "Pratique"}:** {"End-of-day challenges to apply what you've learned." if lang=="en" else "Défis en fin de journée pour appliquer ce que vous avez appris."}

{"Let's dive into" if lang=="en" else "Plongeons dans le"} [{day_str} 1: {week_titles[1]}](day1.qmd)!
"""
        create_file(os.path.join(week_dir, "index.qmd"), index_content)
        
        for day in range(1, 8):
            day_title = week_titles[day]
            exercise_desc = exercises[week][day]
            next_day = week_titles[day+1] if day < 7 else ('the next week’s topics' if lang=='en' else 'les sujets de la semaine prochaine')
            
            day_content = f"""---
title: "{day_str} {day}: {day_title}"
---

# {day_title}

{"Welcome to" if lang=="en" else "Bienvenue au"} **{day_str} {day}**. {"Today, we are diving deep into" if lang=="en" else "Aujourd'hui, nous plongeons dans"} **{day_title}**.

## {learning_obj_title}

{"By the end of this session, you will be able to:" if lang=="en" else "À la fin de cette session, vous serez capable de :"}

1. {"Understand the core principles behind" if lang=="en" else "Comprendre les principes fondamentaux derrière"} {day_title.lower()}.
2. {"Implement these concepts using the Google Gemini ecosystem." if lang=="en" else "Mettre en œuvre ces concepts via l'écosystème Google Gemini."}
3. {"Successfully complete today's hands-on exercise." if lang=="en" else "Terminer avec succès l'exercice pratique d'aujourd'hui."}

## {core_concepts_title}

*({"Replace this section with your detailed lecture notes, theory, and explanations" if lang=="en" else "Remplacez cette section par vos notes de cours détaillées, la théorie et les explications"})*

```python
# {"Example: Setting up the Gemini SDK" if lang=="en" else "Exemple : Configuration du SDK Gemini"}
import google.generativeai as genai

genai.configure(api_key="YOUR_API_KEY")
model = genai.GenerativeModel('gemini-1.5-pro')
response = model.generate_content("{"Explain" if lang=='en' else "Explique"} {day_title} {"in one sentence." if lang=='en' else "en une phrase."}")
print(response.text)
```

## {hands_on_title}

{"It's time to put theory into practice! Spend the next 45 minutes on the following challenge:" if lang=="en" else "Il est temps de mettre la théorie en pratique ! Passez les 45 prochaines minutes sur le défi suivant :"}

{exercise_desc}

**{"Requirements:" if lang=="en" else "Exigences :"}**

- {"Use the Gemini SDK or AI Studio." if lang=="en" else "Utilisez le SDK Gemini ou AI Studio."}
- {"Ensure the output is well-formatted and handles errors gracefully." if lang=="en" else "Assurez-vous que la sortie est bien formatée et gère les erreurs correctement."}
- {"Test it with at least two different edge cases." if lang=="en" else "Testez-le avec au moins deux cas limites différents."}

## {wrap_up_title}

{"Today we covered" if lang=="en" else "Aujourd'hui, nous avons couvert"} {day_title}. {"Tomorrow, we will build upon this by exploring" if lang=="en" else "Demain, nous nous appuierons sur cela en explorant"} **{next_day}**.

{"Make sure to click 'Mark as Complete' below to track your progress!" if lang=="en" else "Assurez-vous de cliquer sur 'Mark as Complete' ci-dessous pour suivre vos progrès !"}
"""
            create_file(os.path.join(week_dir, f"day{day}.qmd"), day_content)

print("Bootstrapped successfully.")
