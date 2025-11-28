# EON — Evolutionary Organism Network

EON is a computational evolution engine that simulates how digital organisms behave, mutate, compete, adapt, and evolve over many generations.
It models organism traits, mutation mechanics, selective pressure, environmental rules, and evolutionary trajectories — giving you a complete evolutionary sandbox.

This project is part of a larger 6-project evolution research portfolio built independently.

## 📌 Features

Simulates digital organisms with customizable genetic traits

Models mutation, adaptation, fitness, and survival pressure

Runs population-wide evolutionary simulations

Tracks best-performing organisms over generations

Generates visualizations such as fitness curves

Modular code structure (organism model, evolution engine, simulation runner)

## 📁 Project Structure
EON/
│
├── eon_engine.py             # Core evolution engine (mutation, selection, reproduction)
├── organism.py               # Organism class with traits, fitness evaluation, mutation logic
├── run_eon_simulation.py     # Main script to run full evolutionary simulations
├── eon_fitness_curve.png     # Fitness curve visualization output

## 🚀 How to Run
### 1. Install dependencies

EON uses only standard Python libraries.
Optional (for plotting):

pip install matplotlib

### 2. Run the simulation

From inside the EON folder:

python run_eon_simulation.py

### 3. Output

After running, you will get:

Simulation logs in the console

A fitness curve image saved as eon_fitness_curve.png

Best-performing organism traits printed at the end

## 🔬 Core Concepts
Digital Organisms

Each organism has parameters such as:

genome (custom structure)

mutation rate

fitness score

behavioral or adaptive traits

Evolution Engine

Handles:

mutation operations

natural selection

reproduction logic

generation cycle management

Fitness Visualization

Tracks:

average fitness

best fitness

evolutionary trends over time

## 📦 Use Cases

Evolution research

Algorithmic evolution demos

Genetic algorithm experimentation

Trait optimization visualizations

Biology-inspired computing projects

## 🧠 Author

Developed individually as part of a 6-project evolutionary computation research portfolio.

## ⭐ If you use this project

You may cite or reference this GitHub repository in your academic or portfolio submissions.

## 🔗 Portfolio Link  
Complete 6-project evolution research collection:  
https://west-route-a3b.notion.site/BioGraph-Evolution-Research-Portfolio-2b69325d1ab1804dab15f731b8af6581?source=copy_link
