# 🤖 Detection of Spot Robot Position using Logistic Regression

This project focuses on predicting the **position of Boston Dynamics' Spot robot** using **logistic regression** and pressure sensor data.

---
## 📂 Project Structure
- [About](#about)
- [Technologies](#technologies)
- [Illustrations_and_example_of_work](#illustrations_and_example_of_work)
- [Conclusion](#conclusion)
- [License](#license)

---
## About
Machine learning, especially neural networks, is increasingly used beyond data science, particularly in automation and robotics. Boston Dynamics, known for robots like Spot the robot dog, builds highly accurate robots capable of navigating complex environments using sensors combined with machine learning models. The main goal of this project is to determine the robot’s position using sensor data — for example, to simply identify whether the robot is on a flat surface. This project is not intended as a complete solution (since sensors typically handle such tasks), but rather reflects the author’s personal interest in exploring machine learning possibilities.

---
## Technologies
Of course, this project could have been made much shorter using the `sky_learn` library, but that wouldn't be interesting. Instead, a full-fledged logistic regression model was written from scratch.  
Input data comes from foot pressure sensors. The logic is:
- If front-leg pressure > back-leg pressure, the robot is **going downstairs**.
- If back-leg pressure > front-leg pressure, the robot is **going upstairs**.
- If pressure is roughly equal across all legs, the robot is on **flat ground**.  

Only the following technologies were used:
- `numpy`
- `pandas`
- `PyQt`



---
## Illustrations_and_example_of_work



---
## Conclusion



---
## License
