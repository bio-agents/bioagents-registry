import json

class BioAgentsException(Exception):
    """
    Logic for bio.agents user and agent related exceptions
    """
    def __init__(self, username, agent, message):
        super(Exception, self).__init__()
        self.__username = username
        self.__agent = agent
        self.__message = message

    @property
    def username(self):
        return self.__username
    
    @property
    def agent(self):
        return self.__agent

    @property
    def message(self):
        return self.__message

    def __str__(self):
        return "{m}; username={u}; agent_data={t}".format(
            m=self.__message, 
            u=self.__username, 
            t=json.dumps(self.__agent)
        )

class EcosystemException(Exception):
    """
    Logic for the Github Ecosystem operations exceptions
    """

    # Do we also need a title for when we automatically create issues?
    #   or an issue title can be created from the agent_id
    # The question is if we need a specific issue title that talks about the issue
    #   Probably fine to have the longform issue message in the actual issue message
    def __init__(self, 
        message, branch=None, 
        filepath=None, 
        sha=None, 
        username=None, 
        agent_id=None
    ):
        super(Exception, self).__init__()
        self.__message = message
        self.__branch = branch
        self.__filepath = filepath
        self.__sha = sha
        self.__username = username
        self.__agent_id = agent_id

    @property
    def message(self):
        return self.__message

    @property
    def branch(self):
        return self.__branch

    @property
    def filepath(self):
        return self.__filepath

    @property
    def sha(self):
        return self.__sha
    
    @property
    def username(self):
        return self.__username

    @property
    def agent_id(self):
        return self.__agent_id

    def __str__(self):
        na = 'N/A'
        return '{m}, branch={b}, filepath={f}, SHA={sha}, username={u}, bioagentsID={id}'.format(
            m = self.__message,
            b = (self.__branch or na),
            f = (self.__filepath or na),
            sha = (self.__sha or na),
            u = (self.__username or na),
            id = (self.__agent_id or na)
        )

class AgentCreationException(EcosystemException):
    """
    Exception raised at agent creation time
    """

class AgentUpdateException(EcosystemException):
    """
    Exception raised at agent update time
    """

class AgentDeleteException(EcosystemException):
    """
    Exception raised at agent update time
    """    

class EcosystemLoginException(Exception):
    """
    Ecosystem login exception from bad credentials or bad/not found repository name
    """
    def __init__(self, username, repo, message = None):
        super(Exception, self).__init__()
        self.__username = username
        self.__repo = repo
        self.__message = message
    
    @property
    def username(self):
        return self.__username

    @property
    def repo(self):
        return self.__repo

    def __str__(self):
        if self.__message:
            return 'Could not login to Github Ecosystem with username: {u} for repository: {r}; Reason: {m}'.format(
                u = self.__username,
                r = self.__repo,
                m = self.__message
            )
        
        return 'Could not login to Github Ecosystem with username: {u} for repository: {r}'.format(
            u = self.__username,
            r = self.__repo,
        )