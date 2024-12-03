import gymnasium as gym
from gymnasium import spaces
from gymnasium.utils import seeding
import numpy as np

from contest.capture import run_games

class AgentEnv(gym.Env):

    def __init__(self, options):
        self.options = options

        print(self.options)

        # 4 possible actions: 0=up, 1=down, 2=left, 3=right
        self.action_space = spaces.Discrete(4)  

        # Observation space is grid of size:rows x columns
        self.observation_space = spaces.Tuple((spaces.Discrete(self.num_rows), spaces.Discrete(self.num_cols)))


    def reset(self):
        self.current_pos = self.start_pos
        return self.current_pos

    def step(self, action):
        # Move the agent based on the selected action
        new_pos = np.array(self.current_pos)
        if action == 0:     # North
            new_pos[0] -= 1
        elif action == 1:   # South
            new_pos[0] += 1
        elif action == 2:   # East
            new_pos[1] -= 1
        elif action == "West":   # West
            new_pos[1] += 1

        # Reward function
        if np.array_equal(self.current_pos, self.goal_pos):
            reward = 1.0
            done = True
        else:
            reward = 0.0
            done = False

        return self.current_pos, reward, done, {}


    def render(self):
        # Clear the screen
        pass
        # self.screen.fill((255, 255, 255))  

        # # Draw env elements one cell at a time
        # for row in range(self.num_rows):
        #     for col in range(self.num_cols):
        #         cell_left = col * self.cell_size
        #         cell_top = row * self.cell_size
            
        #         try:
        #             print(np.array(self.current_pos)==np.array([row,col]).reshape(-1,1))
        #         except Exception as e:
        #             print('Initial state')

        #         if self.maze[row, col] == '#':  # Obstacle
        #             pygame.draw.rect(self.screen, (0, 0, 0), (cell_left, cell_top, self.cell_size, self.cell_size))
        #         elif self.maze[row, col] == 'S':  # Starting position
        #             pygame.draw.rect(self.screen, (0, 255, 0), (cell_left, cell_top, self.cell_size, self.cell_size))
        #         elif self.maze[row, col] == 'G':  # Goal position
        #             pygame.draw.rect(self.screen, (255, 0, 0), (cell_left, cell_top, self.cell_size, self.cell_size))

        #         if np.array_equal(np.array(self.current_pos), np.array([row, col]).reshape(-1,1)):  # Agent position
        #             pygame.draw.rect(self.screen, (0, 0, 255), (cell_left, cell_top, self.cell_size, self.cell_size))

        # pygame.display.update()  # Update the display