import re
from geopy.geocoders import Nominatim
import enchant

class Qoute_validation:
    def __init__(self, qoute):
        self.qoute = qoute
        self.sanskrit_to_normal_char_map = {
            'ã': 'a', 'ñ': 'n', 'õ': 'o', 'ā': 'a', 'ć': 'c', 'ē': 'e',
            'ĩ': 'i', 'ī': 'i', 'ō': 'o', 'ś': 's', 'ũ': 'u', '।': '।',
            '॥': '॥', '़': 'o', 'ū': 'u', 'ḍ': 'd', 'ḏ': 'd', 'ḥ': 'h',
            'ḷ': 'l', 'ḹ': 'l', 'ḻ': 'l', 'ḿ': 'm', 'ṁ': 'm', 'ṃ': 'm',
            'ṅ': 'n', 'ṇ': 'n', 'ṉ': 'n', 'ṙ': 'r', 'ṛ': 'r', 'ṝ': 'r',
            'ṣ': 's', 'ṥ': 's', 'ṭ': 't', 'ẖ': 'h', 'ẽ': 'e'
        }
        self.noun = [
            'krishna', 'krsna', 'caitanya', 'mahaprabhu', 'radharani',
            'sadasiva', "jayapataka", 'advaita', 'gosani', 'maha-visnu',
            'srila', 'das', 'dasa', 'maharaj', 'swami', 'bhaktisiddhanta',
            'thakura','hh','madhava', 'dukhis', 'siromani', 'laxmi', 'india',
            'grhastha', 'subhadra-devi', 'vaisnavas', 'purnima.normally', 'srimad-bhagavatam',
            'bhaktivedanta', '19.170', 'raghunatha', '1971', 'devatas', 'narasimha', 'nitai',
            'kaha', 'caitanya’s', 'jagannatha', 'gopi', 'artha', 'misra', 'visakha', 'travelling',
            'haya—krsnera', 'saba', 'bhagavatam', 'dekha', 'caitanya.\\n', 'parama', 'paramahamsas',
            'gandha', 'prabhu', 'dhama', '3-mile', 'hana', 'thako', 'mora', 'devotee!\\n', 'krsna-prasada',
            'aparadha', "dasa's", 'moksa', 'nama', 'malati', 'ekadasi', 'india\\n', 'sarvopadhi-vinirmuktam',
            'siksa', 'avatara-sara', 'krsna-prema', 'prasada', 'london', 'founder-acarya', 'madhai',
            'uttara', 'yata', 'dako', 'bhaktivinoda', 'ganges', 'ucyate',
            'karo-krsna-siksa', 'sarasvati', 'mahato', 'krsna’-upadesa',
            'yamadutas', 'pracara', 'jagai', 'bhayat', 'fide', 'bhakti',
            'gaura-ganoddesa-dipika', 'doing.\\n', 'govinda', 'bhakta-vatsala',
            'offence', 'tirumala', 'draupadi', '100-times', 'sridhara', 'grhasthas',
            'bhisma-pancaka', 'vedas', 'bhakti-vaibhava', 'vrndavana', '7.128',
            'paramahamsa', 'diksa', 'carnegie', '100', 'krsna-upadesa', 'pancaka',
            'avatara', 'pranama', 'bhajo-krsna', 'benefitted', 'grhe',
            'yudhisthira', 'kunti', 'daru-brahman', 'hare!\\nwhy', 'brahmanas',
            'prema', 'prthivite', 'worshipable', 'krsna-lila', 'duhkhi',
            'helencha', 'kirtana', 'pahu', 'prasadam', 'krsna’s', 'extetrnal',
            'ksatriyas', 'kolkata', 'prabhupada', 'bharata-varsa', '3000',
            'svarupa', 'panchagavya', 'sadhana', 'panca-gavya', 'raya.\\n',
            'damodara', 'bhakti-yoga', 'kama', 'prabhupada’s', 'harinama',
            'nagaradi-grama', 'supersoul', 'rama', 'tirupati', 'souls\\n',
            'sankirtana', 'kali', 'caitanya-candra', '1000', 'tara', 'dvaraka',
            'hrsikesa-sevanam', "caitanya's", 'caitanya-caritamrta', 'gur', 'maya',
            'vipralamba', 'dui', 'visnu', 'ramananda', 'candala', 'narasimhadeva',
            'maha-bhagavata', 'ajnaya', 'brahmana', 'nirmatsaranam', 'pradyumna',
            'puris', 'ananda-kanda', 'yuga', 'gurumaharaj', 'bhakti-sarvabhauma',
            'amu', 'gauranga', '50', 'maha-prasada', 'preyas', 'ei', 'madhya', 'gopis',
            'asya', 'gosvami', 'apy', 'gauracandra', 'bhakta-avatara', 'mayapur', 'sanatana',
            'gaur', 'iskcon', 'puri', 'vairagis', 'bhakti-vedanta', 'nescience', 'non-different',
            'maharaja', 'sudra', 'mahaprabhu’s', 'nitya-dasa', 'nilacale-candra', '2022', 'sloka',
            'svalpam', 'balaji’s', 'bona', 'karuna', 'difference.\\n', 'tarpana', 'sannyasi',
            'dec', 'self-satisfied', 'vaisyas', 'nanda', 'dasis', 'chaitanya', 'japa-mala', 'raya’s',
            'brahma', 'enquired', 'avataras', 'sannyasa', 'prahlada', 'raya', 'aryan', 'vedic', 'bhaktir',
            'argya', 'trayate', 'narayana', 'amara', 'bhagavad-gita', 'atmarama', 'havishyanna', 'advented',
            'perfectional', 'sarvatra', 'vaisnavis', 'kali-yuga', 'sada', 'navadvipa', 'vaisnava', 'sudras',
            'guru-parampara', 'yajna', 'havisyanna', 'sthanu-narasimha', 'maha-mantra', 'desa', 'knower', 'literatures',
            'catur-yugas', 'uttarayana', 'sastra', 'radha', 'kevala', 'devi', 'bilwa',
            'bolo-krsna', 'yare', 'acaryas', 'jana', 'non-veg', 'bhisma', 'gundica', 'suci',
            'haibe', 'brahmacari', 'haridasa', 'ratha-yatra', 'nityananda', "krsna's", 'bhismadeva',
            'nilacala', 'krsnacandra', 'hari', 'dharmasya', 'hrsikena', 'siva', 'high-tech',
            'jivera', 'ship.we', 'parampara', 'sri', 'goloka']


        self.is_valid = self.check_validity()


    def check_validity(self):
        try:
            self.title,self.body,self.reference,self.date,self.place,self.name = self.qoute_parsing()
            print("title: ","\n","--------","\n",self.title,"\n")
            print("body: ","\n","--------","\n",self.body,"\n")
            print("reference: ","\n","--------","\n",self.reference,"\n")
            print("date: ","\n","--------","\n",self.date,"\n")
            print("place: ","\n","--------","\n",self.place, "\n")
            if self.body_and_name_validity_check(self.body):
                var1 = True
                print("aa")
            else:
                print("a")
                var1 = False
          
            if self.date_validity_check(self.date):
                var2 = True
                print("bb")
            else:
                print("b")
                var2 = False
            if self.title_validity_check(self.title):
                var3 = True
                print(f"cc")
            else:
                print("c")
                var3 = False
        
            if self.place_validity_check(self.place):
                var4 = True
                print("dd")
            else:
                print("d")
                var4 = False
            if var1 and var2 and var3 and var4:
               
                return True
            else:
                return False
        except Exception as e:
            print(f"An error occurred during validation: {e}")
            return False



    def to_normal_text(self,text):
        return ''.join(self.sanskrit_to_normal_char_map.get(char, char) for char in text)

    def body_and_name_validity_check(self,body_text):
        body_words = re.findall(r'\b\S+\b', body_text)
        min_num_of_words = 10
        max_num_of_words = 1000
        if (len(body_words) >= min_num_of_words and len(body_words) <= max_num_of_words):
            return True
        
        else:
            return False

    def date_validity_check(self,input_date):
        # Define multiple patterns for different date formats
        patterns = [
            r'\b\d{1,2}/\d{1,2}/\d{4}\b',  # MM/DD/YYYY
            r'\b\d{1,2}-\d{1,2}-\d{4}\b',  # DD-MM-YYYY
            r'\b\d{4}/\d{1,2}/\d{1,2}\b',  # YYYY/MM/DD
            r'\b\d{4}-\d{1,2}-\d{1,2}\b',  # YYYY-MM-DD
            r'\b\d{1,2}\s(?:January|February|March|April|May|June|July|August|September|October|November|December)\s\d{4}\b',  # DD Month YYYY
            r'\b(?:January|February|March|April|May|June|July|August|September|October|November|December)\s\d{1,2},\s\d{4}\b',  # Month DD, YYYY
            r'\b\d{1,2}\s(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\s\d{4}\b'  # DD Abbrev. Month YYYY
        ]

        # Find and print matches
        for pattern in patterns:
            matches = re.findall(pattern, input_date)
            if matches:
                return True
        return False


    def title_validity_check(self,input_string):
        pattern = r'^SQ\s*\d+$'
        if re.search(pattern, input_string):
            return True
        else:
            return False

    def qoute_parsing(self):
        lines = self.qoute.split('\n')
        ans=[]
        for line in lines:
            if line.strip():
                ans.append(line.strip())

        pattern1 = r'^His Holiness'
        pattern2 = r'^>>> Ref.'
        pattern3 = r'^HH'
        pattern4 = r'^Jayapataka'
        for i in range(len(ans)-1,-1,-1):
            if re.search(pattern4, ans[i]) or re.search(pattern3, ans[i]) or re.search(pattern1, ans[i]) or re.search(pattern2, ans[i])  :
                break
        body =""
        for j in range(1,i):
            if len(body) !=0:
                body +='\n'
            body +=ans[j]
        title = ans[0]
        reference = ans[i:]
        #print(reference)
        if len(reference) == 1:
            name, tmp = reference[0].split("on")[0].strip(),reference[0].split("on")[1].split("in")
            date = tmp[0].strip()
            add = tmp[1].strip()
            reference = reference[0]
        elif len(reference) == 3:
            name = reference[0].strip()
            date = reference[1].split(":")[-1].strip()
            add = reference[2].split(":")[-1].strip()
            tmp_ref = reference
            reference = ""
            for j in range(0,3):
                if j != 0:
                    reference += '\n'
                reference += tmp_ref[j]
        return title,body,reference,date,add,name

# Function to validate a location
    def place_validity_check(self,location_name):
        geolocator = Nominatim(user_agent="location_validator",timeout=10)
        location = geolocator.geocode(location_name)
        if location:
            #print(f"Valid location: {location.address}")
            return True
        else:
            return False



qoute1 = """SQ 123
Raghunatha dāsa informed Svarūpa Dāmodara and Govinda about his desire, so in this way if one informs the spiritual master then they can get their answers. Like this, Raghunatha dāsa was getting his answers from Lord Caitanya.

His Holiness Jayapataka Swami
Date: 22 December 2022
Place: Sri Mayapur"""

qoute2="""
SQ 123
At the time of initiation one takes vows, promises that cannot be neglected.

His Holiness Jayapataka Swami on 21 Aug 2022 
in Hyderabad, India
"""

qoute_object = Qoute_validation(qoute1)
print(qoute_object.is_valid)
if qoute_object.is_valid == True:
        print("title: ","\n","--------","\n",qoute_object.title,"\n")
        print("body: ","\n","--------","\n",qoute_object.body,"\n")
        print("reference: ","\n","--------","\n",qoute_object.reference,"\n")
        print("date: ","\n","--------","\n",qoute_object.date,"\n")
        print("place: ","\n","--------","\n",qoute_object.place, "\n")