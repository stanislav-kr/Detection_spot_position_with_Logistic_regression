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
Of course, this project could have been made much shorter using the sky_learn library, but that wouldn't be interesting. It was decided to write a full-fledged logistic regression model from scratch.
As for the data — it comes from foot sensors; these are the input features. The logic is as follows:
- If the pressure on the front legs is greater than on the back legs, the robot is going downstairs.
- If the pressure on the back legs is greater than on the front legs, the robot is going upstairs.
- If the pressure is roughly equal on all legs, the robot is likely on flat ground.

Therefore, among all available technologies, only numpy, pandas, and PyQt libraries were used.


---
## Illustrations_and_example_of_work



---
## Conclusion



---
## License
