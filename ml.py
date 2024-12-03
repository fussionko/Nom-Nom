
import gymnasium as gym
from agent_env import AgentEnv


options = {'display': <contest.capture_graphics_display.PacmanGraphics object at 0x7fcf50f05720>, 'red_team_name': 'Red', 'blue_team_name': 'Blue', 'agents': [<baseline_team.OffensiveReflexAgent object at 0x7fcf50d17f10>, <my_team.OffensiveReflexAgent object at 0x7fcf50d8d420>, <baseline_team.DefensiveReflexAgent object at 0x7fcf50d8c130>, <my_team.DefensiveReflexAgent object at 0x7fcf50d8d660>], 'layouts': [<contest.layout.Layout object at 0x7fcf50d8d690>], 'length': 1200, 'num_games': 1, 'num_training': 0, 'record': False, 'catch_exceptions': False, 'delay_step': 0.03, 'match_id': 0, 'contest_name': 'default'}




gym.register(
    id='AgentEnv-v0',
    entry_point='agent_env:AgentEnv',
    max_episode_steps=1000,
    kwargs={'options':options}
)
# gym.envs.register(
#      id='AgentEnv-v0',
#      entry_point='gym.envs.classic_control:AgentEnv',
#      max_episode_steps=1000,
# )

def create_rl():
    env = gym.make("AgentEnv-v0")
    print(env.action_space)
    print(env.get_action_meanings())

create_rl()