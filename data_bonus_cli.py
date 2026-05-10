en_bonus_cli = """
# Gemini CLI: Zero to Hero Masterclass

<img src="../../assets/gemini_cli_hero.png" alt="Gemini CLI Hero" style="width: 100%; max-width: 400px; border-radius: 12px; margin-bottom: 20px; display: block; box-shadow: 0 4px 15px rgba(0,0,0,0.2);" />

Welcome to the ultimate guide to the **Gemini Command Line Interface (CLI)**. Over the next 6-8 hours, you will transition from learning what the CLI is, to orchestrating complex, automated workflows directly from your terminal.

### The Power of the CLI
The Gemini CLI is a powerful tool designed to bring advanced AI capabilities directly into your terminal. 

**Why is it useful?** It allows developers and system administrators to automate repetitive tasks, analyze local files, and chain AI commands together without having to write full Python or Node.js applications. It's incredibly fast, requires zero boilerplate code, and integrates perfectly with your existing Bash or PowerShell scripts.

**When to use it:** 
- Quick, one-off tasks (e.g., "Summarize this error log").
- Automating local workflows (e.g., "Translate all markdown files in this folder").
- Piping output from other terminal tools directly into the AI.

**When NOT to use it:**
- Building user-facing, full-stack applications (use the Gemini API instead).
- Iterating on complex prompt design (Google AI Studio is better for visual prototyping).
- Handling large-scale, distributed requests where database state and complex logic are required.

**Key steps to mastery:**
1. Master standard input/output (piping) to feed data to the model.
2. Understand how to inject context using the `--media` flag.
3. Learn to enforce structured outputs (JSON) so your scripts can safely parse the AI's response.
4. Seamlessly integrate the CLI into standard Shell scripting (loops, variables, conditionals).

---

## A. Introduction to Gemini CLI

### What is Gemini?
Gemini is Google's most capable AI model family, designed to be natively multimodal (understanding text, code, images, and audio). 

### What is the CLI used for?
The Gemini CLI brings the power of Gemini directly into your terminal. Instead of writing a full Python script to interact with the API, or clicking through a web interface, you can pass files, stream responses, and pipe outputs directly in your shell.

### When to use CLI vs API vs Studio?

::: {.callout-tip}
- **Google AI Studio:** Best for prototyping, testing prompts visually, and tweaking hyperparameters.
- **Gemini CLI:** Best for fast, daily automation (e.g., summarizing local files, writing quick shell scripts, analyzing logs).
- **Gemini API (Python/Node):** Best for building full-stack applications with custom logic and persistent databases.
:::

```{mermaid}
flowchart LR
    A[User] -->|Quick Tasks| B(Gemini CLI)
    A -->|Prototyping| C(Google AI Studio)
    A -->|App Building| D(Gemini API)
    B --> E[Google Cloud / Models]
    C --> E
    D --> E
```

---

## B. Installation & Setup

### Installing the CLI
To install the Gemini CLI globally via `npm` (Node Package Manager), run:

```bash
npm install -g @google/generative-ai-cli
```

### Authenticating with Google
The CLI requires an API key. Get your key from [Google AI Studio](https://aistudio.google.com/), then export it as an environment variable:

```bash
# On Mac/Linux
export GEMINI_API_KEY="your-api-key-here"

# On Windows (PowerShell)
$env:GEMINI_API_KEY="your-api-key-here"
```

### Architecture Overview

```{mermaid}
sequenceDiagram
    participant Terminal
    participant CLI as Gemini CLI
    participant API as Gemini API
    Terminal->>CLI: "gemini --prompt 'Hello'"
    CLI->>API: HTTP POST Request + API Key
    API-->>CLI: Streaming Response
    CLI-->>Terminal: Console Output
```

---

## C. First Steps with Gemini CLI

### Running your first command
Let's run a simple prompt:

```bash
gemini --prompt "Explain quantum computing in one sentence."
```

**Output:**
> Quantum computing uses the principles of quantum mechanics to process information in ways that allow it to solve certain complex problems exponentially faster than classical computers.

### Using text prompts and standard input
You can pipe output from other commands directly into Gemini:

```bash
echo "Translate 'Hello World' to French" | gemini
```

### Using files as input
Want to summarize a local file? Use the `--media` flag:

```bash
gemini --prompt "Summarize this log file" --media error_log.txt
```

---

## D. Advanced Prompting with the CLI

### System Instructions
System instructions set the behavior of the model for the entire session.

```bash
gemini --prompt "Write a function" --system-instruction "You are a senior Python developer. Only output raw code, no markdown formatting."
```

### Structured Outputs
You can force Gemini to return JSON, which is essential for scripting.

```bash
gemini --prompt "List 3 colors" --response-mime-type application/json
```

```{mermaid}
flowchart TD
    Prompt[Raw Text Prompt] --> System[System Instructions Applied]
    System --> Format[JSON Format Enforced]
    Format --> Model[Gemini 1.5 Pro]
    Model --> Out[Clean JSON Output]
```

---

## E. Working with Files, Images, and Audio

Gemini 1.5 Pro has a massive context window. You can pass images and audio directly from your hard drive!

### Image Understanding
```bash
gemini --prompt "What framework is this UI using?" --media screenshot.png
```

### Audio Transcription
```bash
gemini --prompt "Transcribe this meeting and list action items." --media meeting.mp3
```

> [!WARNING]
> Safety Considerations: The CLI adheres to Google's safety guidelines. If you pass an image that violates these policies, the API will return a `FinishReason.SAFETY` block.

---

## F. Building Small Tools with Gemini CLI

The real power of the CLI is automation. You can wrap CLI commands inside Bash or PowerShell scripts.

### Example: Summarizing all files in a folder
Create a `summarize.sh` script:

```bash
#!/bin/bash
for file in *.md; do
  echo "Summarizing $file..."
  gemini --prompt "Summarize this file in 1 bullet point" --media "$file" >> summaries.txt
done
```

---

## G. Mini-Project 1: The Command-Line Research Assistant

**Goal:** Build a script that reads a PDF document, generates key insights, and saves a final markdown report.

### Step 1: The Script
Create `research.sh`:

```bash
#!/bin/bash
FILE=$1
echo "# Research Report: $FILE" > report.md
echo "Generating insights..."
gemini --prompt "Analyze this document and extract the top 3 insights." --media "$FILE" >> report.md
echo "Report generated!"
```

### Step 2: Execution
```bash
chmod +x research.sh
./research.sh annual_report.pdf
```

```{mermaid}
stateDiagram-v2
    [*] --> ReadPDF
    ReadPDF --> GeminiAnalysis
    GeminiAnalysis --> GenerateMarkdown
    GenerateMarkdown --> [*]
```

---

## H. Mini-Project 2: Content Generator

**Goal:** Build an advanced CLI workflow that creates an Instagram script based on a trending topic.

### The Workflow
1. User provides a topic.
2. Gemini CLI generates a script.
3. The script is formatted using JSON to separate the "Visual" and "Audio" columns.

```bash
gemini --prompt "Write an Instagram reel script about AI tools. Provide the output as JSON with an array of 'scenes' containing 'visual' and 'audio'." --response-mime-type application/json > script.json
```

### Expected Output
```json
{
  "scenes": [
    {
      "visual": "Person looking stressed at computer.",
      "audio": "Tired of repetitive coding tasks?"
    }
  ]
}
```

---

## I. Best Practices & Optimization

- **Reduce Hallucinations:** Use the `--temperature 0` flag for factual, analytical tasks.
- **Debugging:** If the CLI fails, add `--debug` to see the raw HTTP request/response.
- **Workflow Structure:** Keep your system instructions in a separate text file and read them via `cat system.txt | gemini ...` to keep your commands clean.

```{mermaid}
flowchart LR
    A[Draft Prompt] --> B{Factual?}
    B -->|Yes| C[Set Temp = 0]
    B -->|No| D[Set Temp = 0.7]
    C --> E[Execute]
    D --> E
```

---

## J. Final Quiz + Recap

### Recap
You have learned how to install the Gemini CLI, pipe data, use system instructions, process multimodal files, and build automated Bash scripts.

### Quiz
1. **What flag is used to pass a local image file to the CLI?**
   - A) `--file`
   - B) `--media`
   - C) `--image`
   
<details>
<summary><strong>View Solution</strong></summary>
*Solution: B*
</details>

2. **How do you force the CLI to return JSON?**
   - A) `--json`
   - B) `--format json`
   - C) `--response-mime-type application/json`
   
<details>
<summary><strong>View Solution</strong></summary>
*Solution: C*
</details>
"""

fr_bonus_cli = """
# Gemini CLI : Masterclass de Zéro à Héros

<img src="../../assets/gemini_cli_hero.png" alt="Gemini CLI Hero" style="width: 100%; max-width: 400px; border-radius: 12px; margin-bottom: 20px; display: block; box-shadow: 0 4px 15px rgba(0,0,0,0.2);" />

Bienvenue dans le guide ultime de la **Command Line Interface (CLI) Gemini**. Au cours des 6 à 8 prochaines heures, vous passerez de la découverte de la CLI à l'orchestration de workflows automatisés complexes directement depuis votre terminal.

### La Puissance de la CLI
La CLI Gemini est un outil puissant conçu pour apporter des capacités d'IA avancées directement dans votre terminal.

**Pourquoi est-ce utile ?** Cela permet aux développeurs et aux administrateurs système d'automatiser des tâches répétitives, d'analyser des fichiers locaux et d'enchaîner des commandes d'IA sans avoir à écrire des applications complètes en Python ou Node.js. C'est incroyablement rapide, ne nécessite aucun boilerplate (code de base), et s'intègre parfaitement avec vos scripts Bash ou PowerShell existants.

**Quand l'utiliser :**
- Tâches rapides et ponctuelles (ex: "Résume ce fichier log d'erreur").
- Automatisation de workflows locaux (ex: "Traduire tous les fichiers markdown de ce dossier").
- Redirection (piping) de la sortie d'autres outils du terminal directement vers l'IA.

**Quand NE PAS l'utiliser :**
- Création d'applications full-stack destinées aux utilisateurs (utilisez l'API Gemini).
- Itération sur la conception de prompts complexes (Google AI Studio est meilleur pour le prototypage visuel).
- Gestion de requêtes à grande échelle et distribuées nécessitant un état en base de données et une logique complexe.

**Étapes clés vers la maîtrise :**
1. Maîtriser l'entrée/sortie standard (piping) pour fournir des données au modèle.
2. Comprendre comment injecter du contexte en utilisant le paramètre `--media`.
3. Apprendre à imposer des sorties structurées (JSON) pour que vos scripts puissent analyser la réponse de l'IA en toute sécurité.
4. Intégrer de manière transparente la CLI dans le scripting Shell standard (boucles, variables, conditions).

---

## A. Introduction à Gemini CLI

### Qu'est-ce que Gemini ?
Gemini est la famille de modèles d'IA la plus performante de Google, conçue pour être nativement multimodale (comprenant le texte, le code, les images et l'audio).

### À quoi sert la CLI ?
La CLI Gemini apporte la puissance de Gemini directement dans votre terminal. Au lieu d'écrire un script Python complet pour interagir avec l'API, ou de cliquer dans une interface web, vous pouvez passer des fichiers, streamer des réponses et rediriger les sorties (pipe) directement dans votre shell.

### Quand utiliser la CLI vs l'API vs Studio ?

::: {.callout-tip}
- **Google AI Studio :** Idéal pour le prototypage, tester visuellement les prompts et ajuster les hyperparamètres.
- **Gemini CLI :** Idéal pour l'automatisation quotidienne rapide (ex: résumer des fichiers locaux, écrire des scripts shell rapides, analyser des logs).
- **Gemini API (Python/Node) :** Idéal pour construire des applications full-stack avec une logique personnalisée et des bases de données.
:::

```{mermaid}
flowchart LR
    A[Utilisateur] -->|Tâches Rapides| B(Gemini CLI)
    A -->|Prototypage| C(Google AI Studio)
    A -->|Création d'App| D(Gemini API)
    B --> E[Google Cloud / Modèles]
    C --> E
    D --> E
```

---

## B. Installation & Configuration

### Installation de la CLI
Pour installer la CLI Gemini globalement via `npm` (Node Package Manager), exécutez :

```bash
npm install -g @google/generative-ai-cli
```

### Authentification avec Google
La CLI nécessite une clé API. Obtenez votre clé depuis [Google AI Studio](https://aistudio.google.com/), puis exportez-la comme variable d'environnement :

```bash
# Sur Mac/Linux
export GEMINI_API_KEY="votre-cle-api-ici"

# Sur Windows (PowerShell)
$env:GEMINI_API_KEY="votre-cle-api-ici"
```

### Aperçu de l'Architecture

```{mermaid}
sequenceDiagram
    participant Terminal
    participant CLI as Gemini CLI
    participant API as Gemini API
    Terminal->>CLI: "gemini --prompt 'Bonjour'"
    CLI->>API: Requête HTTP POST + Clé API
    API-->>CLI: Streaming de la Réponse
    CLI-->>Terminal: Sortie Console
```

---

## C. Premiers Pas avec Gemini CLI

### Exécuter votre première commande
Lançons un prompt simple :

```bash
gemini --prompt "Explique l'informatique quantique en une phrase."
```

**Sortie :**
> L'informatique quantique utilise les principes de la mécanique quantique pour traiter l'information de manière à résoudre certains problèmes complexes exponentiellement plus vite que les ordinateurs classiques.

### Utiliser des prompts texte et l'entrée standard
Vous pouvez rediriger (pipe) la sortie d'autres commandes directement vers Gemini :

```bash
echo "Traduire 'Hello World' en Français" | gemini
```

### Utiliser des fichiers comme entrée
Vous voulez résumer un fichier local ? Utilisez le paramètre `--media` :

```bash
gemini --prompt "Résume ce fichier log" --media error_log.txt
```

---

## D. Prompting Avancé avec la CLI

### Instructions Système
Les instructions système définissent le comportement du modèle pour toute la session.

```bash
gemini --prompt "Écris une fonction" --system-instruction "Tu es un développeur Python senior. Ne sors que du code brut, pas de formatage markdown."
```

### Sorties Structurées
Vous pouvez forcer Gemini à retourner du JSON, ce qui est essentiel pour le scripting.

```bash
gemini --prompt "Liste 3 couleurs" --response-mime-type application/json
```

```{mermaid}
flowchart TD
    Prompt[Prompt Texte Brut] --> System[Instructions Système Appliquées]
    System --> Format[Format JSON Forcé]
    Format --> Model[Gemini 1.5 Pro]
    Model --> Out[Sortie JSON Propre]
```

---

## E. Travailler avec Fichiers, Images et Audio

Gemini 1.5 Pro dispose d'une fenêtre de contexte massive. Vous pouvez passer des images et de l'audio directement depuis votre disque dur !

### Compréhension d'Images
```bash
gemini --prompt "Quel framework cette UI utilise-t-elle ?" --media screenshot.png
```

### Transcription Audio
```bash
gemini --prompt "Transcrire cette réunion et lister les actions à mener." --media reunion.mp3
```

> [!WARNING]
> Considérations de Sécurité : La CLI respecte les règles de sécurité de Google. Si vous passez une image qui viole ces politiques, l'API retournera un bloc `FinishReason.SAFETY`.

---

## F. Construire de Petits Outils avec Gemini CLI

La vraie puissance de la CLI est l'automatisation. Vous pouvez encapsuler les commandes CLI dans des scripts Bash ou PowerShell.

### Exemple : Résumer tous les fichiers d'un dossier
Créez un script `resume.sh` :

```bash
#!/bin/bash
for file in *.md; do
  echo "Résumé de $file..."
  gemini --prompt "Résume ce fichier en 1 point" --media "$file" >> resumes.txt
done
```

---

## G. Mini-Projet 1 : L'Assistant de Recherche en Ligne de Commande

**Objectif :** Construire un script qui lit un document PDF, génère des insights clés et sauvegarde un rapport markdown final.

### Étape 1 : Le Script
Créez `recherche.sh` :

```bash
#!/bin/bash
FILE=$1
echo "# Rapport de Recherche : $FILE" > rapport.md
echo "Génération des insights..."
gemini --prompt "Analyse ce document et extrais les 3 insights principaux." --media "$FILE" >> rapport.md
echo "Rapport généré !"
```

### Étape 2 : Exécution
```bash
chmod +x recherche.sh
./recherche.sh rapport_annuel.pdf
```

```{mermaid}
stateDiagram-v2
    [*] --> LirePDF
    LirePDF --> AnalyseGemini
    AnalyseGemini --> GenererMarkdown
    GenererMarkdown --> [*]
```

---

## H. Mini-Projet 2 : Générateur de Contenu

**Objectif :** Construire un workflow CLI avancé qui crée un script Instagram basé sur un sujet tendance.

### Le Workflow
1. L'utilisateur fournit un sujet.
2. Gemini CLI génère un script.
3. Le script est formaté en JSON pour séparer les colonnes "Visuel" et "Audio".

```bash
gemini --prompt "Écris un script de Réel Instagram sur les outils IA. Fournis la sortie en JSON avec un tableau 'scenes' contenant 'visuel' et 'audio'." --response-mime-type application/json > script.json
```

### Sortie Attendue
```json
{
  "scenes": [
    {
      "visuel": "Personne stressée devant un ordinateur.",
      "audio": "Fatigué des tâches de codage répétitives ?"
    }
  ]
}
```

---

## I. Bonnes Pratiques & Optimisation

- **Réduire les Hallucinations :** Utilisez le paramètre `--temperature 0` pour les tâches factuelles et analytiques.
- **Débogage :** Si la CLI échoue, ajoutez `--debug` pour voir la requête/réponse HTTP brute.
- **Structure du Workflow :** Gardez vos instructions système dans un fichier texte séparé et lisez-les via `cat system.txt | gemini ...` pour garder vos commandes propres.

```{mermaid}
flowchart LR
    A[Brouillon de Prompt] --> B{Factuel ?}
    B -->|Oui| C[Temp = 0]
    B -->|Non| D[Temp = 0.7]
    C --> E[Exécuter]
    D --> E
```

---

## J. Quiz Final + Récapitulatif

### Récapitulatif
Vous avez appris à installer la CLI Gemini, rediriger des données, utiliser des instructions système, traiter des fichiers multimodaux et construire des scripts Bash automatisés.

### Quiz
1. **Quel paramètre est utilisé pour passer un fichier image local à la CLI ?**
   - A) `--file`
   - B) `--media`
   - C) `--image`
   
<details>
<summary><strong>Voir la solution</strong></summary>
*Solution : B*
</details>

2. **Comment forcer la CLI à retourner du JSON ?**
   - A) `--json`
   - B) `--format json`
   - C) `--response-mime-type application/json`
   
<details>
<summary><strong>Voir la solution</strong></summary>
*Solution : C*
</details>
"""
