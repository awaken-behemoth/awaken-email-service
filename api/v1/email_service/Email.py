

class Email(object):

    def __init__(self,template, lang):
        self.subject = "default"
        self.template = template
        self.lang = lang
        
    def get_message(self):
        return self.template