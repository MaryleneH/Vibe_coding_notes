import os

def create_file(path, content):
    os.makedirs(os.path.dirname(path) if os.path.dirname(path) else '.', exist_ok=True)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content.strip() + '\n')

base_dir = r"c:\Users\maryl\2 - Side work\11 - My resume\vibe_coding_notes"

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
        text: Home
      - href: week1/index.qmd
        text: Week 1
      - href: week2/index.qmd
        text: Week 2
      - href: week3/index.qmd
        text: Week 3
  
  sidebar:
    style: "docked"
    search: true
    collapse-level: 1
    contents:
      - section: "Week 1: Foundations"
        href: week1/index.qmd
        contents:
          - week1/day1.qmd
          - week1/day2.qmd
          - week1/day3.qmd
          - week1/day4.qmd
          - week1/day5.qmd
          - week1/day6.qmd
          - week1/day7.qmd
      - section: "Week 2: Agents"
        href: week2/index.qmd
        contents:
          - week2/day1.qmd
          - week2/day2.qmd
          - week2/day3.qmd
          - week2/day4.qmd
          - week2/day5.qmd
          - week2/day6.qmd
          - week2/day7.qmd
      - section: "Week 3: Advanced & Deploy"
        href: week3/index.qmd
        contents:
          - week3/day1.qmd
          - week3/day2.qmd
          - week3/day3.qmd
          - week3/day4.qmd
          - week3/day5.qmd
          - week3/day6.qmd
          - week3/day7.qmd

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

index_qmd = """---
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

week_titles = {
    "week1": ["Foundations", "The Vibe Coding Mindset", "Advanced Prompt Engineering & Reasoning", "Structured Outputs", "Multimodal Magic", "Transitioning to Code", "Mini-Project 1", "Review & Rest"],
    "week2": ["Agents", "Introduction to Function Calling", "Defining Tools", "Building your First Agent", "Context & Memory", "Agentic Workflows", "Mini-Project 2: Sacristan Agent", "Review & Rest"],
    "week3": ["Advanced & Deploy", "AI-Assisted Coding", "Test-Driven Vibe Coding", "System Architecture", "Generating UIs", "Integrating the Sacristan Agent", "Final Project Polish", "Deploying & Wrap-up"]
}

create_file(os.path.join(base_dir, "_quarto.yml"), quarto_yml)
create_file(os.path.join(base_dir, "index.qmd"), index_qmd)
create_file(os.path.join(base_dir, "styles.scss"), styles_scss)
create_file(os.path.join(base_dir, "progress.html"), progress_html)

daily_exercises = {
    "week1": [
        "", # index 0 is not used
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

for week in ["week1", "week2", "week3"]:
    week_dir = os.path.join(base_dir, week)
    titles = week_titles[week]
    
    # Create week index
    index_content = f"""---
title: "{week.capitalize()}: {titles[0]}"
---

# {titles[0]} Overview

Welcome to {week.capitalize()} of the Vibe Coding Mastery journey! 

This week, we will focus on **{titles[0]}**. You'll explore how to guide AI models effectively and translate natural language instructions into functional code and tools.

### What to Expect
- **Daily Mini-Lessons:** 2-hour segments focusing on a specific concept.
- **Hands-on Practice:** End-of-day challenges to apply what you've learned.
- **Project Building:** We culminate the week with a mini-project.

Let's dive into [Day 1: {titles[1]}](day1.qmd)!
"""
    create_file(os.path.join(week_dir, "index.qmd"), index_content)
    
    for day in range(1, 8):
        day_title = titles[day]
        exercise_desc = daily_exercises[week][day]
        next_day = titles[day+1] if day < 7 else 'the next week’s foundational topics'
        
        day_content = f"""---
title: "Day {day}: {day_title}"
---

# {day_title}

Welcome to **Day {day}**. Today, we are diving deep into **{day_title}**.

## 🎯 Learning Objectives

By the end of this session, you will be able to:
1. Understand the core principles behind {day_title.lower()}.
2. Implement these concepts using the Google Gemini ecosystem.
3. Successfully complete today's hands-on exercise.

## 📖 Core Concepts

*(Replace this section with your detailed lecture notes, theory, and explanations regarding {day_title})*

### Key Topic 1
Explain the first major concept here. Use examples and diagrams where possible.

### Key Topic 2
Provide code snippets or prompts to demonstrate the idea:

```python
# Example: Setting up the Gemini SDK
import google.generativeai as genai

genai.configure(api_key="YOUR_API_KEY")
model = genai.GenerativeModel('gemini-1.5-pro')
response = model.generate_content("Explain {day_title} in one sentence.")
print(response.text)
```

## 💻 Hands-on Exercise

It's time to put theory into practice! Spend the next 45 minutes on the following challenge:

{exercise_desc}

**Requirements:**
- Use the Gemini SDK or AI Studio.
- Ensure the output is well-formatted and handles errors gracefully.
- Test it with at least two different edge cases.

## ✅ Wrap-up

Today we covered {day_title}. This forms a crucial building block for our final Sacristan Agent project. Tomorrow, we will build upon this by exploring **{next_day}**.

Make sure to click "Mark as Complete" below to track your progress!
"""
        create_file(os.path.join(week_dir, f"day{day}.qmd"), day_content)

print("Bootstrapped successfully.")
