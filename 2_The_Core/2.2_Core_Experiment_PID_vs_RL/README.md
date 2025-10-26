# PID vs. Reinforcement Learning Control Experiment

This experiment compares the performance of a classic PID controller against a modern Reinforcement Learning (RL) agent on the CartPole-v1 benchmark task.

## Description

The `main.py` script implements both a `PIDController` class and a Proximal Policy Optimization (PPO) RL agent using the `stable-baselines3` library. The experiment evaluates and compares their ability to balance the pole on the cart.

## Installation

To run this experiment, you need to install the dependencies listed in the main `requirements.txt` file.

```bash
pip install -r ../../requirements.txt
```

## Running the Experiment

To run the experiment, execute the `main.py` script from within this directory:

```bash
python main.py
```

## Expected Results

The script will output the following files:

*   `results.json`: A JSON file containing the numerical results of the comparison, including mean and standard deviation of rewards.
*   `comparison_plots.png`: A PNG image visualizing the performance of the PID controller and the RL agent.

You can interpret the results by examining the generated plot and the console output, which will show the mean reward for both the PID and RL controllers. The RL agent is expected to achieve a significantly higher mean reward.

## Troubleshooting

If you encounter any issues, please ensure that all the required packages are installed correctly and that you are running the script from the `experiments/pid_vs_rl` directory.
