import ApplicationDataModel

class TwitterDataModel(ApplicationDatamodel):
    def __init__(self):
        pass

    @property
    def app_id(self):
        return 'APP_ID'

    @property
    def app_secret(self):
        return 'APP_SECRET'

    @property
    def oauth_token(self):
        return 'OAUTH_TOKEN'

    @property
    def oauth_secret(self):
        return 'OAUTH_SECRET'
