
from email.mime.text import MIMEText
from abc import ABC, abstractmethod


class Email(object):
    """
    This class is the base class from which all email inherit; It is an abstract class
    That should not be instantiated. Instead, you should inherit it to create new types of emails;


    Args:
        object (_type_): _description_
    """

    def __init__(self, lang: str, data: dict):
        self.subject = "default"
        self.data = data
        self.lang = lang

    @staticmethod
    @abstractmethod
    def get_message():
        """
        Creates somethin cool

        Raises:
            NotImplementedError: _description_
        """
        raise NotImplementedError(
            "get message must be implemented on all email Instances Email")

    @staticmethod
    @abstractmethod
    def get_subject():
        raise NotImplementedError(
            "get subject must be implemented on all email Instances of Email")

    @staticmethod
    @abstractmethod
    def get_authority_email():
        raise NotImplementedError(
            "get subject must be implemented on all email Instances of Email")
