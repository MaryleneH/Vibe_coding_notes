import os
import shutil

from data_meta import (
    en_home, fr_home,
    en_titles, fr_titles,
    en_exercises, fr_exercises
)
from data_w1 import en_concepts_w1, fr_concepts_w1
from data_w2 import en_concepts_w2, fr_concepts_w2
from data_w3 import en_concepts_w3, fr_concepts_w3
from data_bonus_cli import en_bonus_cli, fr_bonus_cli

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

# Dictionary mappings for concepts
en_concepts = {
    "week1": en_concepts_w1,
    "week2": en_concepts_w2,
    "week3": en_concepts_w3
}

fr_concepts = {
    "week1": fr_concepts_w1,
    "week2": fr_concepts_w2,
    "week3": fr_concepts_w3
}

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
        - section: "Bonus"
          contents:
            - text: "Gemini - CLI"
              href: en/bonus/cli.qmd
            - text: "Google AI Studio"
              href: en/bonus/studio.qmd
            - text: "Antigravity"
              href: en/bonus/antigravity.qmd

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
        - section: "Bonus"
          contents:
            - text: "Gemini - CLI"
              href: fr/bonus/cli.qmd
            - text: "Google AI Studio"
              href: fr/bonus/studio.qmd
            - text: "Antigravity"
              href: fr/bonus/antigravity.qmd

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
  --code-bg: #1e1e1e;
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
  background-color: var(--inline-code-bg) !important;
  color: var(--inline-code-color) !important;
  border-radius: 4px;
  padding: 0.15em 0.3em;
}
pre code {
  background-color: transparent !important;
  color: inherit !important;
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
for lang, home_content, titles, exercises, concepts in [
    ("en", en_home, en_titles, en_exercises, en_concepts),
    ("fr", fr_home, fr_titles, fr_exercises, fr_concepts)
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
            concept_text = concepts[week].get(day, "*(Detailed explanation coming soon)*")
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

{concept_text}

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
            
    # Generate Bonus Section
    bonus_dir = os.path.join(lang_dir, "bonus")
    bonus_intro = "*(Detailed content coming soon)*" if lang == "en" else "*(Contenu détaillé à venir)*"
    cli_content = en_bonus_cli if lang == "en" else fr_bonus_cli
    create_file(os.path.join(bonus_dir, "cli.qmd"), cli_content)
    create_file(os.path.join(bonus_dir, "studio.qmd"), f"---\ntitle: 'Google AI Studio'\n---\n\n{bonus_intro}\n")
    create_file(os.path.join(bonus_dir, "antigravity.qmd"), f"---\ntitle: 'Antigravity'\n---\n\n{bonus_intro}\n")

print("Bootstrapped successfully.")
