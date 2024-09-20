from .ecosystem_exceptions import BioAgentsException
import json
# We can maybe add here a delete flag
#   Because we don't technically need the bioagents.tech JSON data when we delete the agent
#   But we still need the agent id
#   We could pass the agent id in a different way, but technically we can still obtain the full agent JSON
#       even if we delete the agent
# 
class BioAgentsData(object):
    __ID_KEY = 'bioagentsID'
    def __init__(self, username, agent_json_string, delete = False, agent_id = None):

        # We can look in bioagents.tech for this username if we really want to make sure
        #   but since this code is for now called from bioagents.tech backend we don't really have to
        if not(username):
            raise BioAgentsException(username, agent_json_string, 'No valid bioagents.tech username was provided.')

        # TODO decide if we use the @delete parameter. If we use it we need to maybe also add a delete @property
        # TODO decide if we use the @agent_id parameter
        
        self.__username = username

        if not(agent_json_string):
            raise BioAgentsException(username, agent_json_string, 'Missing agent JSON data.')

        try:
            self.__agent = json.loads(agent_json_string)
        except ValueError as v:
            raise BioAgentsException(username, agent_json_string, 'Invalid agent JSON structure. ' + str(v))
        
        self.__agent_json_string = agent_json_string
        
        if not(self.validate_agent()):
            raise BioAgentsException(username, agent_json_string, 'Invalid agent data.')

        self.__agent_id = self.__agent.get(self.__ID_KEY)

    def validate_agent(self):
        # TODO validation
        # This should already be valid since it gets called
        #   from bioagents.tech after validation has been done
        
        if self.__agent.get(self.__ID_KEY) == None:
            raise BioAgentsException(self.__username, self.__agent_json_string, 'Missing agent id.')

        return True
    
    @property
    def username(self):
        return self.__username

    @property
    def agent_json(self):
        return self.__agent_json_string

    @property
    def agent_id(self):
        return self.__agent.get(self.__ID_KEY)

    # @property
    # def delete(self):
    #     return self.__delete
