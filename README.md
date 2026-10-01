# 🎮 Yahoshuva [Player 01] — Gaming Developer Portfolio

> **Class 11 — Builders Day Project**  
> **Course:** Group C Web Development (Scaler School of Technology)  
> **Theme:** Creative / Playful — Cyberpunk RPG Developer Interface  
> **Core Stack:** Semantic HTML5 + Handcrafted CSS3  
> **Bonus Challenge:** Tailwind CSS Edition (`tailwind.html`)  

---

## 📌 Deliverables & Live Quick Links

- **Single-File All-in-One Portfolio (Primary Submission):** [`index.html`](index.html) *(100% self-contained: HTML5 + inlined CSS + embedded Base64 images + embedded Bug Hunter arcade engine + Web Audio API synthesizer)*
- **Portable Copy:** [`portfolio-single.html`](portfolio-single.html) *(identical standalone file that can be moved or sent anywhere without any folders)*
- **Tailwind CSS Edition (Bonus Point):** [`tailwind.html`](tailwind.html)
- **Modular Stylesheet Reference:** [`style.css`](style.css)
- **GitHub Armory:** [github.com/Yahoshuva138](https://github.com/Yahoshuva138)
- **Summon Player (Email):** [yahoshuva138@gmail.com](mailto:yahoshuva138@gmail.com)

---

## 👤 Character Bio & Overview

**Player 01: Yahoshuva** is an undergraduate student pursuing a B.Tech in **Computer Science & Applied Artificial Intelligence** at **Scaler School of Technology (SST)** in Bengaluru, Karnataka.

- **Class:** Frontend Developer & Creative Technologist
- **Current Server:** Scaler School of Technology, Bengaluru
- **HP (Clean Code):** `100 / 100`
- **MP (CSS Grid & Flexbox):** `98 / 100`
- **EXP / Level:** `LVL 19` (Builders Day 2026 Boss Raid)
- **Philosophy:** *"Clean, readable code conquers complexity."*
- **Guilds:** Scaler Builders Cohort, Toastmasters International (Speechcraft & Leadership).

---

## 🛠️ Technologies & Concepts Demonstrated

### Core Technologies
- **HTML5:** Semantic architecture (`<header>`, `<nav>`, `<main>`, `<section>`, `<article>`, `<aside>`, `<footer>`, `<figure>`, `<form>`, `<label>`, `<input>`, `<button>`).
- **CSS3:** 
  - **CSS Box Model:** Precision margins, paddings, border radiuses, and universal `box-sizing: border-box`.
  - **CSS Grid:** 2D layout systems, asymmetric **Bento Grid** for the Skill Tree, fluid `auto-fit` responsive Quest cards with `minmax(min(100%, 350px), 1fr)`.
  - **CSS Flexbox:** 1D alignment, space distribution in the Gaming HUD navigation, HP/MP stat tracks, button groupings, and vertical centering.
  - **CSS Positioning:** Sticky navigation (`position: sticky`, `top: 0`, `z-index: 1000`, `backdrop-filter: blur(14px)`), absolute corner reticle brackets (`.corner-bracket`), floating badges (`.floating-card`), and relative containers.
  - **CSS Transitions & Transforms:** Smooth elevation on hover (`transform: translateY(-8px)`), scale effects on images (`transform: scale(1.05)`), and neon button scanline effects.
  - **CSS Keyframe Animations (`@keyframes`):**
    - `@keyframes floatTop` & `@keyframes floatBottom`: Floating RPG micro-badges on the hero visual.
    - `@keyframes pulseGreen`: Server online availability indicator pulsing.
    - Progress bar fill animations with custom linear gradients.
  - **CSS Custom Properties (Variables):** Theme tokens for neon cyan (`#00f0ff`), neon magenta (`#ff0055`), health emerald (`#00ff9d`), gold (`#ffd000`), typography, spacing, and glowing box-shadows.
  - **Responsive Web Design:** Mobile-first fluid scaling with `clamp()`, flexible percentages, and media queries (`1024px`, `768px`, `480px`).

### Bonus Point — Tailwind CSS
- Full standalone version available in [`tailwind.html`](tailwind.html).
- Implements Tailwind CSS utility classes:
  - **Grid & Flex:** `grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6`, `flex items-center justify-between`
  - **Responsive Prefixes:** `sm:`, `md:`, `lg:`, `xl:`
  - **Transitions & Transforms:** `transition-all duration-300 hover:-translate-y-2 hover:shadow-[0_0_25px_rgba(0,240,255,0.3)]`
  - **Gaming Accents:** Neon borders, glowing box shadows, and custom font extensions for `Orbitron` and `Press Start 2P`.

---

## 📂 Featured Completed Quests (Projects)

### 1. Smart Document Assistant (Rank: S-Tier)
- **Description:** An intelligent multi-stage guidance and readiness platform designed for citizen services in India (Indian Passport, Aadhaar Biometrics, Instant PAN via Form 49A, National Scholarship Portal). Includes a **Reverse Document Matcher** (*"What documents do I have?" → "What can I apply for?"*), interactive official portal walkthrough mockups, and text-to-speech voice narration.
- **Technologies:** React 19, TypeScript, Tailwind CSS, Web Speech API, LocalStorage.
- **Preview Asset:** [`images/project-1.png`](images/project-1.png)
- **Repository / Inquiries:** [GitHub @Yahoshuva138](https://github.com/Yahoshuva138)

### 2. Anime Explorer Directory & Vault (Rank: A-Tier)
- **Description:** A curated, high-performance catalog of 60+ top anime titles sourced from IMDb list `ls500222778`. Features instant client-side keyword search, genre category pills (Action, Sci-Fi, Drama, Psychological, Fantasy), IMDb rating badges, and responsive cards.
- **Technologies:** Semantic HTML5, CSS Grid, CSS Flexbox, Vanilla JavaScript (ES6+).
- **Preview Asset:** [`images/project-2.png`](images/project-2.png)
- **Data Source:** [IMDb List ls500222778](https://www.imdb.com/list/ls500222778/)

### 3. Interactive English Quiz Engine (Rank: A-Tier)
- **Description:** A timed interactive assessment web app designed for grammar, vocabulary, and technical language mastery. Features live countdown timers, instantaneous answer verification, score calculation, keyboard accessibility, and state tracking.
- **Technologies:** Modular HTML5, CSS Variables, Flexbox, Accessible Form Controls.
- **Preview Asset:** [`images/project-3.png`](images/project-3.png)

---

## 📝 Coursework & WebDev 101 Assignments

The portfolio features a dedicated **Coursework Gauntlet** (`#assignments`) with working hyperlinks to Yahoshuva's Scaler School of Technology lab assignments:

### 1. Assignment 01 — Interactive Student Portal & Registration Engine
- **Live Assignment Path:** [`webdev101_assignments/assignment_01_student_portal/student-portal.html`](webdev101_assignments/assignment_01_student_portal/student-portal.html)
- **Topics & Skills:** Semantic HTML5 structure, academic tables with row/column spans, weekly course timetable schedules, complete course registration form with inputs, dropdown menus, radio selectors, checkboxes, and CSS styling.
- **Student Profile:** Yahoshuva (B.Tech Computer Science & Applied AI, Scaler).

### 2. Assignment 02 — Flexbox Quest 2D Game Arena & HUD
- **Live Assignment Path:** [`webdev101_assignments/assignment_02_flexbox_quest/index.html`](webdev101_assignments/assignment_02_flexbox_quest/index.html)
- **Topics & Skills:** CSS Display model experiments (`block`, `inline`, `inline-block`, `flex`), retro platformer game arena with floating star collectibles, direction pad controller, 6-item inventory grid, and real-time quest progress tracker.

---

## 🕹️ Interactive Feature: Cyber Arcade Mini-Game ("Bug Hunter 2026")

Directly embedded in both `index.html` and `tailwind.html` is an interactive **3x3 Terminal Grid Arcade Game**:

- **Objective:** Defend the Scaler production server! Squash runtime bugs before time expires (20-second speed raid).
- **Enemies & Spawns:**
  - 🐛 **SyntaxError:** `+10 PTS` (Common)
  - 👾 **MergeConflict:** `+20 PTS` (Medium)
  - 🪲 **NullPointer:** `+30 PTS` (Advanced)
  - 🚀 **CleanDeploy:** `+50 PTS` (Rare powerup)
  - 💣 **ProdCrash:** `-20 PTS` (Hazard — avoid clicking!)
- **Hardware Simulation:**
  - **Retro CRT Screen:** Scanline overlays (`linear-gradient` at 4px intervals) and radial vignette masking.
  - **Arcade Marquee & Control Deck:** Beveled retro cabinet border, joystick, and arcade push buttons.
  - **Floating Combat Points:** Real-time damage numbers (`+10 PTS`, `-20 PTS`) animating upwards.
  - **Zero-Dependency 8-Bit Audio:** Synthesizes custom square, triangle, and sawtooth waves directly using the **Web Audio API** (`OscillatorNode` + `GainNode`), requiring no external MP3/WAV files and operating 100% offline.
  - **High Score Persistence:** Stores the player's personal best in HTML5 `localStorage`.

---

## 📁 Repository Structure

```text
PORTFOLIOX/
│
├── index.html                 # 🌟 Single-File Portfolio (100% self-contained: HTML5 + inlined CSS + base64 images + game)
├── portfolio-single.html      # Portable standalone copy of the single-file portfolio
├── style.css                  # Production-grade CSS stylesheet with gaming design tokens & arcade styles
├── tailwind.html              # Bonus Edition (100% Tailwind CSS Utility Classes + Bug Hunter Game)
│
├── webdev101_assignments/     # 📚 Coursework & Class Assignments
│   ├── assignment_01_student_portal/
│   │   └── student-portal.html    # Assignment 1: Student Portal & Registration
│   └── assignment_02_flexbox_quest/
│       ├── index.html             # Assignment 2: Flexbox Quest 2D Game Arena
│       └── style.css              # Flexbox Quest custom stylesheet
│
├── images/                    # Verified visual assets (also embedded as base64 in index.html)
│   ├── yahoshuva.png          # Real portrait photograph of Yahoshuva
│   ├── project-1.png          # Smart Document Assistant high-res UI preview
│   ├── project-2.png          # Anime Explorer Directory UI preview
│   ├── project-3.png          # Interactive Quiz Engine UI preview
│   └── gaming-bg.jpg          # 8-bit retro cyberpunk city wallpaper
│
├── DUAL/                      # Dual-edition folder (index.html & tailwind.html)
├── create_project_mockups.py  # Automation script for UI preview assets
└── README.md                  # Complete documentation and TA Viva Defense Guide
```

---

## 🧑‍🏫 TA Evaluation & Viva Defense Guide

Use this section to understand and defend every architectural choice made in this codebase:

### Q1: Why did you choose the Gaming / Creative & Playful theme?
> **Answer:** *"The Builders Day prompt encouraged picking a creative visual direction. I chose the Gaming / RPG Developer HUD theme because it turns a static portfolio into an interactive story: displaying skills as an RPG skill tree, projects as completed quests, and education as campaign history. It gave me the opportunity to demonstrate advanced CSS Grid, custom properties, neon box shadows, and keyframe animations in an engaging way."*

### Q2: Why did you use CSS Grid in the Skill Tree section?
> **Answer:** *"I used CSS Grid (`display: grid; grid-template-columns: repeat(3, 1fr); gap: 1.5rem;`) to build an asymmetric Bento Grid. Unlike Flexbox which is 1-dimensional, CSS Grid enables 2-dimensional alignment across rows and columns. This allowed me to give core attribute cards a 2-column span (`grid-column: span 2`) while keeping secondary cards single-width."*

### Q3: Why did you use Flexbox in the Navigation Bar and Cards?
> **Answer:** *"Flexbox is optimal for 1-dimensional item distribution along an axis. In the HUD navbar, `display: flex; justify-content: space-between; align-items: center;` places the player tag on the left, menu links centered, and the action button on the far right. In project cards, `display: flex; flex-direction: column;` with `flex: 1` ensures that the action buttons and tags remain aligned at the bottom across all cards, regardless of how long the description text is."*

### Q4: What does `position: sticky` and `z-index: 1000` do on the header?
> **Answer:** *"`position: sticky; top: 0;` allows the navigation bar to scroll naturally until it hits the top edge of the viewport, where it locks into place so the visitor never loses access to navigation links. `z-index: 1000` creates a stacking context higher than any page content, preventing elements (such as project images or cards) from sliding over the navigation bar during scroll. The `backdrop-filter: blur(14px)` adds a translucent glassmorphic effect so content subtly blurs underneath."*

### Q5: How did you implement the reticle corner brackets on the avatar?
> **Answer:** *"The avatar wrapper has four child elements (`.corner-bracket.corner-tl`, `.corner-tr`, etc.) positioned with `position: absolute;`. Each corner has 3px solid cyan border on two sides (e.g. top and left for top-left) with the other two sides set to `none`. This creates a clean camera targeting / gamer reticle around the photo."*

### Q6: How does the floating badge animation on the Hero image work?
> **Answer:** *"The floating badges are positioned relative to the `.hero-visual` wrapper using `position: absolute;`. I created a CSS `@keyframes floatTop` rule that interpolates `transform: translateY(0)` to `transform: translateY(-10px)` and back over `4.5s` with `ease-in-out` infinite iteration. For the opposite badge, `@keyframes floatBottom` moves `+10px` to create a natural, organic floating illusion."*

### Q7: What do your media queries do?
> **Answer:** *"We use mobile-first and responsive desktop breakpoints:
> 1. `@media (max-width: 1024px)`: Collapses the 2-column hero into a single centered column and adapts the 3-column bento grid to 2 columns.
> 2. `@media (max-width: 768px)`: Changes the navbar into an easily scrollable horizontal row, stacks the contact form inputs from 2 columns to 1, and reflows quest cards into a single column for comfortable phone viewing.
> 3. `@media (max-width: 480px)`: Hides decorative floating badges on small mobile screens to prevent horizontal overflow, scales arcade node dimensions, and stretches buttons to `width: 100%` for comfortable thumb tap targets."*

### Q8: If you used Tailwind CSS, how does it handle responsive design?
> **Answer:** *"Tailwind CSS uses a mobile-first responsive design pattern. Classes without a prefix (e.g. `grid-cols-1`) apply to mobile screens by default. Breakpoint prefixes like `md:grid-cols-2` and `lg:grid-cols-3` apply media queries at minimum widths (`768px` and `1024px` respectively)."*

### Q9: How is the arcade game built without breaking the CSS-focused requirement?
> **Answer:** *"The game arena is an interactive showcase of modern CSS layout and animation techniques: a 3x3 CSS Grid (`.arena-grid`), pseudo-CRT scanlines with CSS gradients, and `@keyframes` animations for bug appearances, squashes, and floating combat text. The lightweight JavaScript engine simply toggles classes and calculates points over a 20-second interval, demonstrating that clean CSS structures make dynamic frontend interactivity seamless."*

### Q10: How does the 8-bit sound work without audio files?
> **Answer:** *"Instead of relying on heavy MP3 or WAV files that could fail to load, I used the browser's native `AudioContext` API to synthesize 8-bit frequencies programmatically. A triangle wave at 580Hz-880Hz creates a chirp squashing effect, a square wave at 330Hz-660Hz creates the start fanfare, and a descending sawtooth wave creates a low explosion sound. It provides immediate retro feedback with zero network overhead."*

### Q11: How did you implement the CRT scanline effect in CSS?
> **Answer:** *"The `.crt-scanlines` overlay uses a repeating CSS linear gradient (`linear-gradient(rgba(18, 16, 16, 0) 50%, rgba(0, 0, 0, 0.35) 50%)`) with `background-size: 100% 4px;` and `pointer-events: none;`. Combined with a radial vignette gradient that darkens the screen borders, it accurately reproduces the visual warmth and texture of an old cathode-ray tube monitor."*

---

## 🏆 Checklist for Submission

- [x] Replaced profile image with real photo `images/yahoshuva.png`
- [x] Gaming / Cyberpunk RPG Developer HUD theme throughout
- [x] Embedded interactive arcade mini-game ("Bug Hunter 2026")
- [x] 8-bit sound synthesizer with Web Audio API (zero audio file dependencies)
- [x] LocalStorage high-score tracking & CRT monitor scanlines
- [x] Semantic HTML5 structure throughout
- [x] Organized, custom-property-driven CSS in `style.css`
- [x] Responsive on Mobile (375px+), Tablet (768px), and Desktop (1200px+)
- [x] Sticky navigation bar with blur effect & Arcade link
- [x] Hero section with punchy intro and animated visual
- [x] About section with real personal story and stats
- [x] Bento Grid skills section without fake percentages
- [x] 3 Real projects with high-resolution preview images
- [x] Accessible contact form and working email/GitHub links
- [x] CSS transitions (button hover, card lift, link underlines)
- [x] CSS keyframe animations (floating cards, glowing border, pulse dot, bug squash)
- [x] Tailwind CSS Bonus Version implemented in `tailwind.html`
- [x] Verified zero broken images and zero placeholder text

