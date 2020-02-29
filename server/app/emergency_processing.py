## load necessary modules
import re 

class EmergencyMessage(object):
    """
    preprocess text documents, and see whether it contains strings of emergency words
    
    """
    
    ### initialization--define a few rules
    def __init__(self):
        ## emergency message rules
        self.message=re.compile('([1-3]\d{2}|[4-9]\d)([.]\d{1})?\/([1-3]\d{2}|[4-9]\d)([.]\d{1})?')
        ## emergency message keywords
        self.message_keywords=['having chest pain', 'drooping of my face',
                               'unable to walk','short of breath at rest','tight chest pain',
                               'chest pain and nausea',
                               'having chest pains that have gotten increasingly worse',
                               'chest pains that have gotten worse','chest pain that has gotten worse',
                               'chest pain has gotten worse','passing out nonstop','passing out again']
        
    def split_emails(self, text):
        """
        split a text into different emails
        
        :params[in]: text, string, a piece of text made up of emails shooting back and forth
        
        :params[out]: a list of separate emails
        """
        patt1 = re.compile('----- Message -----')      # pattern of reply emails
        curr_utter = patt1.split(text)[0]              # current utterance after removing conversation logs
        return curr_utter
    
    @staticmethod
    def check_keywords_in(sentence, words):
        """
        check whether a sentence contains at least one word in a list
        :params[in]: sentence, a sentence
        :params[in]: words, a list of keywords\
    
        :params[out]: True/False
        """
        ## True/False of a sentence has at least one word
        res = any([k in sentence.lower() for k in words]) 
        return res 

    def check_emergency_message(self, text):
        """
        check whether a sentence contains a string of emergency terms/concepts
        :params[in]: text, a text
        :params[out]: True/False
        
        """
        last_=self.split_emails(text) ## remove chat history
        ## check keywords first by matching
        if self.check_keywords_in(last_, self.message_keywords):
            return True
        ## check whether has emergency phrases 
        elif re.search(self.message, last_)!=None:
            return True
        else:
            return False