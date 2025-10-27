# File: experiments/pid_vs_rl/main.py
import gymnasium as gym
import numpy as np
from stable_baselines3 import PPO
from stable_baselines3.common.evaluation import evaluate_policy
import matplotlib.pyplot as plt

class PIDController:
    def __init__(self, Kp, Ki, Kd):
        self.Kp, self.Ki, self.Kd = Kp, Ki, Kd
        self.integral = 0
        self.prev_error = 0
    
    def control(self, error, dt=0.02):
        self.integral += error * dt
        derivative = (error - self.prev_error) / dt
        self.prev_error = error
        return self.Kp * error + self.Ki * self.integral + self.Kd * derivative

def run_pid(env, controller, episodes=100):
    rewards = []
    for ep in range(episodes):
        obs, _ = env.reset()
        total_reward = 0
        done = False
        while not done:
            angle, angular_vel = obs[2], obs[3]
            error = -angle  # Keep pole upright
            action_continuous = controller.control(error)
            action = 1 if action_continuous > 0 else 0
            obs, reward, terminated, truncated, _ = env.step(action)
            total_reward += reward
            done = terminated or truncated
        rewards.append(total_reward)
    return np.array(rewards)

def run_rl(env, timesteps=50000, episodes=100):
    model = PPO("MlpPolicy", env, verbose=0)
    model.learn(total_timesteps=timesteps)
    mean_reward, std_reward = evaluate_policy(model, env, n_eval_episodes=episodes)
    return mean_reward, std_reward

# Main experiment
env = gym.make("CartPole-v1")
pid = PIDController(Kp=10, Ki=0.01, Kd=50)
pid_rewards = run_pid(env, pid, episodes=100)
print(f"PID: Mean={pid_rewards.mean():.2f}, Std={pid_rewards.std():.2f}")

rl_mean, rl_std = run_rl(env, timesteps=50000, episodes=100)
print(f"RL (PPO): Mean={rl_mean:.2f}, Std={rl_std:.2f}")

# Save results
results = {
    "PID": {"mean": float(pid_rewards.mean()), "std": float(pid_rewards.std())},
    "RL": {"mean": float(rl_mean), "std": float(rl_std)}
}
import json
with open("results.json", "w") as f:
    json.dump(results, f, indent=2)

def plot_results(pid_rewards, rl_mean, rl_std):
    fig, axes = plt.subplots(1, 2, figsize=(12, 5))
    
    # Plot 1: Episode rewards (PID)
    ax = axes[0]
    ax.plot(pid_rewards, 'b-', alpha=0.7, label='PID')
    ax.axhline(y=np.mean(pid_rewards), color='b', linestyle='--', 
               label=f'Mean={np.mean(pid_rewards):.1f}')
    ax.set_xlabel('Episode')
    ax.set_ylabel('Reward')
    ax.set_title('PID Controller: Episode Rewards')
    ax.legend()
    ax.grid(True, alpha=0.3)
    
    # Plot 2: Comparison bar chart
    ax = axes[1]
    methods = ['PID', 'RL (PPO)']
    means = [np.mean(pid_rewards), rl_mean]
    stds = [np.std(pid_rewards), rl_std]
    x = np.arange(len(methods))
    ax.bar(x, means, yerr=stds, capsize=5, alpha=0.7, color=['blue', 'orange'])
    ax.set_ylabel('Mean Reward')
    ax.set_title('Performance Comparison')
    ax.set_xticks(x)
    ax.set_xticklabels(methods)
    ax.grid(True, alpha=0.3, axis='y')
    
    # Add value labels
    for i, (mean, std) in enumerate(zip(means, stds)):
        ax.text(i, mean + std + 10, f'{mean:.1f}', ha='center', va='bottom')
    
    plt.tight_layout()
    plt.savefig('plots.png', dpi=150, bbox_inches='tight')
    print(f"Plots saved to plots.png")
    plt.close()

plot_results(pid_rewards, rl_mean, rl_std)
