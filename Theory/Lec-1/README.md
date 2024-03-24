# Artificial Intelligence (AI)
Artificial Intelligence (AI) refers to the simulation of human intelligence processes by machines, typically through the creation of algorithms and models that enable computers to perform tasks that would normally require human intelligence. These tasks include learning, reasoning, problem-solving, perception, understanding natural language, and interacting with the environment. AI aims to create systems that can autonomously perceive, analyze, and act upon information to achieve specific goals.

# Machine Learning and Deep Learning Concepts

## Machine Learning (ML)

Machine Learning (ML) is a subset of artificial intelligence (AI) that focuses on teaching machines to learn from data and make predictions or decisions without being explicitly programmed for each task.

### Types of Machine Learning:

1. **Supervised Learning:**
   - Involves training a model on labeled data, where the algorithm learns to map input data to output labels.
   - Examples: Regression, Classification.

2. **Unsupervised Learning:**
   - Deals with finding patterns or hidden structures in unlabeled data.
   - Examples: Clustering, Dimensionality Reduction.

3. **Semi-supervised Learning:**
   - Combination of supervised and unsupervised learning, where models are trained on a small amount of labeled data and a large amount of unlabeled data.
   
4. **Reinforcement Learning:**
   - Concerned with training agents to make sequential decisions by interacting with an environment and receiving feedback in the form of rewards or penalties.
   - Examples: Game playing, Robotics.

### Applications of Machine Learning:

- Recommendation Systems
- Fraud Detection
- Spam Filtering
- Medical Diagnosis
- Natural Language Processing (NLP)
- Computer Vision

## Deep Learning (DL)

Deep Learning is a specialized subset of machine learning that utilizes artificial neural networks with multiple layers (deep neural networks) to learn representations of data.

### Key Concepts:

1. **Neural Networks:**
   - Basic building blocks of deep learning, inspired by the structure of the human brain.
   - Consist of interconnected nodes organized in layers (input layer, hidden layers, output layer).

2. **Convolutional Neural Networks (CNNs):**
   - Particularly effective for processing grid-like data, such as images.
   - Utilize convolutional layers to automatically learn spatial hierarchies of features.

3. **Recurrent Neural Networks (RNNs):**
   - Designed to handle sequential data, where connections between nodes can form loops.
   - Suitable for tasks like natural language processing and time series analysis.

### Popular Deep Learning Frameworks:

- TensorFlow
- PyTorch
- Keras

### Applications of Deep Learning:

- Image Recognition
- Speech Recognition
- Natural Language Processing
- Autonomous Vehicles
- Robotics

## Programming vs Training

### Programming:

**Definition**: Programming is like giving instructions to a computer to do certain tasks. It's like following a recipe where you know exactly what ingredients you have and what steps to take to make a dish.

**Purpose**: The main aim of programming is to create software or programs that can perform specific tasks on a computer. You write code to tell the computer what to do, and it follows those instructions precisely.


### Training in Machine Learning:

**Definition**: Training in machine learning is like teaching a computer to learn from examples. Instead of giving specific instructions, you show the computer lots of examples and let it figure out the patterns on its own.

**Purpose**: The goal of training in machine learning is to help the computer recognize patterns and relationships in data so that it can make predictions or decisions in new situations. It's like teaching a machine to recognize cats by showing it many pictures of cats until it can identify them on its own.


| Comparison                       | Hard Computing                                               | Soft Computing                                                           |
|---------------------------------|--------------------------------------------------------------|--------------------------------------------------------------------------|
| **Analytical Model**           | Requires a precisely stated analytical model                  | Tolerant of imprecision, uncertainty, partial truth, and approximation |
| **Role Model**                 | Role model is precise, akin to a machine                       | Role model is the human mind                                             |
| **Logic**                      | Based on binary logic and crisp systems                        | Based on fuzzy logic, neural nets, and probabilistic reasoning          |
| **Programming**                | Requires explicit programming                                   | Can evolve its own programs                                             |
| **Logic Type**                 | Uses two-valued logic                                           | Can use multivalued or fuzzy logic                                       |
| **Determinism**                | Deterministic                                                   | Incorporates stochasticity                                                |
| **Data Input**                 | Requires exact input data                                       | Can deal with ambiguous and noisy data                                   |
| **Execution**                  | Strictly sequential                                             | Allows parallel computations                                             |
| **Output Precision**           | Produces precise answers                                        | Can yield approximate answers                                           |


## Reactive Machines
Imagine you have a machine that reacts to things happening around it, kind of like how you react when someone calls your name. You don't wait for a specific instruction to respond; you just react when you hear your name. In the same way, a Reactive Machine responds to events or changes in its environment without needing a step-by-step plan. It's like a machine that's always on alert, ready to react whenever something happens. A reactive machine cannot store a memory and as a result cannot rely on past experiences to inform decision making in real-time.

## Limited Memory

Limited memory artificial intelligence has the ability to store previous data and predictions when gathering information and weighing potential decisions — essentially looking into the past for clues on what may come next. Limited memory artificial intelligence is more complex and presents greater possibilities than reactive machines.

Limited memory AI is created when a team continuously trains a model in how to analyze and utilize new data or an AI environment is built so models can be automatically trained and renewed. When utilizing limited memory AI in machine learning, **six steps** must be followed: 
- Training data must be created,
- the machine learning model must be created,
- the model must be able to make predictions,
- the model must be able to receive human or environmental feedback,
- that feedback must be stored as data, and these steps must be reiterated as a cycle.






