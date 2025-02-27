# **♞ Knight's Tour Solver AI**  
### **Master 1 - Visual Computing, USTHB (2024/2025)**  

**Course:** Problem Solving - TP by *Dr. Meriem Sebai*  
<br>  

📄 **[Project Support (PDF)](./📄chess_knight_tour_ga_project.pdf)**  
<br>  

![♞ Knight's Tour Example](https://cdn.dribbble.com/userupload/19544331/file/original-35f99cb947a2deb51ff9ffd411d002bf.gif)  
<br>  

---

## **📌 About**  
The **Knight's Tour** is a classic chess puzzle where the knight must visit every square on the chessboard exactly once. This project solves the problem using a **Genetic Algorithm (GA)**, implementing chromosome representation, crossover, mutation, and fitness evaluation to find optimal solutions.  

---

## **🚀 Features**  
- ♟️ **Genetic Algorithm**: Solves the Knight's Tour problem using evolutionary techniques.  
- 🧬 **Chromosome Representation**: Encodes knight moves as genes for optimization.  
- 🔄 **Crossover & Mutation**: Combines and mutates genes to explore new solutions.  
- 🎯 **Fitness Evaluation**: Measures the success of each knight's path.  
- 📊 **Visualization**: Displays the optimal solution on a chessboard.  

---

## **⚙️ How It Works**  
### **1️⃣ Chromosome Class**  
- 🧬 Represents a sequence of knight moves (genes).  
- Implements **crossover** and **mutation** for genetic evolution.  

### **2️⃣ Knight Class**  
- ♞ Tracks the knight's position, path, and fitness.  
- ✅ Validates moves and evaluates fitness based on visited squares.  

### **3️⃣ Population Class**  
- 🌍 Manages a population of knights.  
- 🏆 Implements **tournament selection** and creates new generations.  

### **4️⃣ Genetic Algorithm**  
- 🔄 Evolves the population over generations to find the optimal solution.  

---

## **📦 Installation**  
1️⃣ Clone the repository:  
```bash  
git clone https://github.com/selma-Bentaiba/Chess-Knight-Tour-Genetic-Algorithm.git  
```  

2️⃣ Install dependencies:  
```bash  
pip install pygame  
```  

3️⃣ Run the solver:  
```bash  
python __main__.py  
```  

---

## **🧠 Genetic Algorithm for Knight's Tour**  
### **1️⃣ Chromosome Representation**  
- 🧬 Each chromosome represents a sequence of 63 moves (genes).  
- 🔢 Moves are encoded as integers (1-8) corresponding to the knight's possible directions.  

### **2️⃣ Crossover & Mutation**  
- 🔄 **Single-point crossover**: Combines genes from two parents to create offspring.  
- 🎲 **Mutation**: Randomly alters genes to explore new solutions.  

### **3️⃣ Fitness Evaluation**  
- 🎯 Fitness is calculated based on the number of squares visited.  
- 🏆 The maximum fitness is **64** (all squares visited).  

---

## **📜 Code Overview**

### **📂 `main.py`**  
- 🏁 Runs the Genetic Algorithm.  
- 📊 Displays the optimal solution and execution time.  

### **📂 `Chromosome.py`**  
- 🧬 Defines the chromosome structure and genetic operations (crossover, mutation).  

### **📂 `Knight.py`**  
- ♞ Manages the knight's position, path, and fitness evaluation.  

### **📂 `Population.py`**  
- 🌍 Handles the population of knights and evolves them over generations.  

---

## **🔮 Future Improvements**  
- ⚡ **Optimize Fitness Function**: Enhance the fitness evaluation for better performance.  
- ⚙️ **Parallel Processing**: Speed up the algorithm using parallel computation.  
- 🖥️ **Interactive GUI**: Create a more engaging visualization for the Knight's Tour.  

