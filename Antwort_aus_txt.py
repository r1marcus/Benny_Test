import holmes_extractor as holmes
import pickle 

class Antwort_aus_txt:
    
    def __init__(self, datei_name):
        self.dateiname = datei_name
        self.holmes_manager = holmes.Manager(model='de_core_news_md')
        
    def lade_datei(self):
        datei = open(self.dateiname, 'r')
        """Öffnen und Laden der txt-Datei mit Holmes"""
        print('Lade deutsches Sprachmodel')
        
        print('Lade txt-Datei: ', self.dateiname)
        #self.holmes_manager.parse_and_register_document(datei.read(),label='1')
        #test= self.holmes_manager.serialize_document('1')
        #print(test)
        
        #file_pi = open('knowledgde.obj', 'wb') 
        #pickle.dump(self.holmes_manager.serialize_document('1'), file_pi)
        
        file_pi2 = open('knowledgde.obj', 'rb') 
        test = pickle.load(file_pi2)
        self.holmes_manager.deserialize_and_register_document(test, label='1')

    def get_Antwort(self, eingabe):
        such_text = eingabe
        
        """Suchen nach der Frage im Text"""
        such_text = such_text.strip(' ').strip('?')
        topic_match_dicts = \
            self.holmes_manager.topic_match_documents_returning_dictionaries_against(
                text_to_match=such_text,
                number_of_results = 1,
                only_one_result_per_document=True,
                sideways_match_extent=20,
                maximum_number_of_single_word_matches_for_relation_matching =100,
                maximum_number_of_single_word_matches_for_embedding_matching =10)
    
        for index, topic_match_dict in enumerate(topic_match_dicts):
            output = ''.join((
                topic_match_dict['rank'],
                '. Document ',
                topic_match_dict['document_label'],
                '; sentences at character indexes ',
                str(topic_match_dict['sentences_character_start_index_in_document']),
                '-',
                str(topic_match_dict['sentences_character_end_index_in_document']),
                '; score ',
                str(topic_match_dict['score']),
                ':'
            ))
        return (topic_match_dict['text'])
    
    def get_Score(self, eingabe):
        such_text = eingabe
        
        """Suchen nach der Frage im Text"""
        such_text = such_text.strip(' ').strip('?')
        topic_match_dicts = \
            self.holmes_manager.topic_match_documents_returning_dictionaries_against(
                text_to_match=such_text,
                number_of_results = 1,
                only_one_result_per_document=True,
                maximum_number_of_single_word_matches_for_relation_matching =100,
                maximum_number_of_single_word_matches_for_embedding_matching =10)
            
            
        print(topic_match_dicts)
        for index, topic_match_dict in enumerate(topic_match_dicts):
            output = ''.join((
                topic_match_dict['rank'],
                '. Document ',
                topic_match_dict['document_label'],
                '; sentences at character indexes ',
                str(topic_match_dict['sentences_character_start_index_in_document']),
                '-',
                str(topic_match_dict['sentences_character_end_index_in_document']),
                '; score ',
                str(topic_match_dict['score']),
                ':'
            ))
            if topic_match_dict['score']>4:
                score=topic_match_dict['score']
                print (score)
                return (score)