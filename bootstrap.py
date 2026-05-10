import os

def create_file(path, content):
    os.makedirs(os.path.dirname(path) if os.path.dirname(path) else '.', exist_ok=True)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)

base_dir = r"c:\Users\maryl\2 - Side work\11 - My resume\vibe_coding_notes"

quarto_yml = """project:
  type: website
  output-dir: docs

website:
  title: "Vibe Coding Mastery"
  description: "Learn to vibe code real apps and AI agents in 3 weeks using Google tools."
  site-url: "https://your-github-username.github.io/vibe_coding_notes"
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
      light: [cosmo, styles.scss]
      dark: [cyborg, styles.scss]
    css: styles.scss
    toc: true
    toc-depth: 3
    code-copy: true
    highlight-style: github
    include-after-body: progress.html
"""

index_qmd = """---
title: "Vibe Coding Mastery"
subtitle: "Learn to vibe code real apps and AI agents in 3 weeks using Google tools."
---

# Welcome to Vibe Coding

This is a 21-day journey to becoming a "Vibe Coding" expert. You'll learn how to leverage Google AI Studio and the Gemini Python SDK to build real applications and AI agents from scratch.

## 🗺️ Curriculum Overview

- **[Week 1: Foundations](week1/index.qmd)** - Master advanced prompting and the Gemini API.
- **[Week 2: Agents](week2/index.qmd)** - Teach Gemini to use tools and build your Sacristan Assistant.
- **[Week 3: Advanced & Deploy](week3/index.qmd)** - AI-assisted coding, UIs, and deployment.

**Prerequisites:** 
- A basic understanding of logic. 
- Python installed on your machine.
- A Google account to access Google AI Studio.

Get started by navigating to [Week 1, Day 1](week1/day1.qmd).
"""

styles_scss = """/*-- scss:defaults --*/
$primary: #1a73e8; /* Google Blue */
$body-bg: #f8f9fa;
$font-family-sans-serif: 'Inter', 'Roboto', sans-serif;

/*-- scss:rules --*/
.navbar {
  box-shadow: 0 2px 4px rgba(0,0,0,0.1);
}

.sidebar {
  background-color: #ffffff;
  border-right: 1px solid #e0e0e0;
}

h1, h2, h3 {
  color: #202124;
  font-weight: 600;
}

.quarto-dark {
  h1, h2, h3 {
    color: #e8eaed;
  }
  .sidebar {
    background-color: #202124;
    border-right: 1px solid #3c4043;
  }
}
"""

progress_html = """<div id="progress-container" style="margin-top: 50px; padding: 20px; border-top: 1px solid #ddd; text-align: center;">
  <button id="mark-complete-btn" class="btn btn-primary" style="display:none;" onclick="toggleComplete()">Mark as Complete</button>
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
            btn.textContent = "✅ Completed";
            btn.classList.replace("btn-primary", "btn-success");
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
      btn.textContent = "Mark as Complete";
      btn.classList.replace("btn-success", "btn-primary");
    } else {
      localStorage.setItem("completed_" + path, "true");
      btn.textContent = "✅ Completed";
      btn.classList.replace("btn-primary", "btn-success");
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

for week in ["week1", "week2", "week3"]:
    week_dir = os.path.join(base_dir, week)
    titles = week_titles[week]
    
    # Create week index
    index_content = f"""---
title: "{week.capitalize()}: {titles[0]}"
---

# Overview

Welcome to {week.capitalize()}!

"""
    create_file(os.path.join(week_dir, "index.qmd"), index_content)
    
    for day in range(1, 8):
        day_title = titles[day]
        day_content = f"""---
title: "Day {day}: {day_title}"
---

# {day_title}

Content for {week}, Day {day} goes here.

```python
# Example python code block
def hello_vibe():
    print("Vibe Coding!")
```
"""
        create_file(os.path.join(week_dir, f"day{day}.qmd"), day_content)

print("Bootstrapped successfully.")
