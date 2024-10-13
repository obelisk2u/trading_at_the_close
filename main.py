import roles
from search import scrape_google
import autogen
import openai
from autogen import ConversableAgent
from autogen.coding import LocalCommandLineCodeExecutor
from autogen import GroupChatManager
from autogen import GroupChat
from autogen import UserProxyAgent
#===============================================================================

agents = roles.agents()
WORKING_DIR = "/home/jdstout/projects/multi_agent/trading_at_the_close/working_dir"
config_list = {	
        'api_key': '',
	    'model':'gpt-3.5-turbo'
}

search_agent = ConversableAgent(
    "search_agent", 
    llm_config = config_list,
    system_message = agents.search_message
)

summary_agent = ConversableAgent(
    "summary_agent",
    llm_config = config_list,
    system_message = agents.summary_message,
)

search_agent.register_for_llm(name="scrape_google", description="input string of topic")(scrape_google)

chat_result=summary_agent.initiate_chat(
    search_agent,
    message=agents.instructions
)
#===============================================================================
"""
code_executor_agent = ConversableAgent(
    "code_executor_agent",
    llm_config=False,  
    code_execution_config={"executor":executor},  
    human_input_mode="ALWAYS"
)

code_writer_agent = ConversableAgent(
    "code_writer_agent",
    system_message=code_writer_system_message,
    llm_config={"config_list":config_list_writer},
    code_execution_config={'executor':executor}
)

manager_agent = ConversableAgent(
    "manager_agent",
    llm_config={"config_list":config_list_writer},
    code_execution_config={'executor':executor},
    system_message = manager_message
)

user_proxy = UserProxyAgent(
    "user_proxy",
    default_auto_reply = "ok",
    human_input_mode="NEVER",
    code_execution_config=False
)

group_chat = GroupChat(
    agents=[manager_agent, code_writer_agent],
    max_round=100,
    messages=[]
)

group_chat_manager = GroupChatManager(
    groupchat=group_chat,
    llm_config={"config_list":config_list_writer},
    code_execution_config=False
)

with open('instructions.txt', 'r') as file:
    instructions = file.read().replace('\n', ' ') 

chat_result=code_writer_agent.initiate_chat(
    manager_agent,
    message=instructions
)
"""
