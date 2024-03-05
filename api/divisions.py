from django.db import models
from django.http import JsonResponse
# Create your models here.

DIVISIONS = (
    {
        'id': 0,
        'name': 'Barishal',
        'districts': (
            {
                'id': 0,
                'name': 'Barguna',
                'areas': (
                    'Amtali',
                    'Bamna',
                    'Barguna Sadar',
                    'Betagi',
                    'Patharghata',
                    'Taltali'
                )
            },
            {
                'id': 1,
                'name': 'Barishal',
                'areas': (
                    'Agailjhara',
                    'Babuganj',
                    'Barajalia',
                    'Barishal Sadar',
                    'Gournadi',
                    'Hizla',
                    'Mehendiganj',
                    'Muladi',
                    'Wazirpur'
                )
            },
            {
                'id': 2,
                'name': 'Bhola',
                'areas': (
                    'Bhola Sadar',
                    'Burhanuddin',
                    'Char Fasson',
                    'Daulatkhan',
                    'Lalmohan',
                    'Manpura',
                    'Tazumuddin'
                )
            },
            {
                'id': 3,
                'name': 'Jhalokati',
                'areas': (
                    'Jhalokati Sadar',
                    'Kathalia',
                    'Nalchity'
                )
            },
            {
                'id': 4,
                'name': 'Patuakhali',
                'areas': (
                    'Bauphal',
                    'Dashmina',
                    'Dumki',
                    'Galachipa',
                    'Kalapara',
                    'Mirzaganj',
                    'Patuakhali Sadar',
                    'Rangabali'
                )
            },
            {
                'id': 5,
                'name': 'Pirojpur',
                'areas': (
                    'Bhandaria',
                    'Kawkhali',
                    'Mathbaria',
                    'Nazirpur',
                    'Pirojpur Sadar',
                    'Nesarabad (Swarupkathi)'
                )
            }

        )
    },
    {
        'id': 1,
        'name': 'Chattogram',
        'districts': (
            {
                'id': 0,
                'name': 'Bandarban',
                'areas': (
                    'Ali Kadam',
                    'Bandarban Sadar',
                    'Lama',
                    'Rowangchhari',
                    'Ruma',
                    'Thanchi'
                )
            },
            {
                'id': 1,
                'name': 'Brahmanbaria',
                'areas': (
                    'Ashuganj',
                    'Bancharampur',
                    'Brahmanbaria Sadar',
                    'Kasba',
                    'Nasirnagar',
                    'Nabinagar',
                    'Sarail',
                    'Shahbazpur Town'
                )
            },
            {
                'id': 2,
                'name': 'Chandpur',
                'areas': (
                    'Chandpur Sadar',
                    'Faridganj',
                    'Haimchar',
                    'Haziganj',
                    'Kachua',
                    'Matlab Dakkhin',
                    'Matlab Uttar',
                    'Shahrasti'
                )
            },
            {
                'id': 3,
                'name': 'Chattogram',
                'areas': (
                    'Anwara',
                    'Banshkhali',
                    'Boalkhali',
                    'Chattogram Sadar',
                    'Fatikchhari',
                    'Hathazari',
                    'Lohagara',
                    'Mirsharai',
                    'Patiya',
                    'Rangunia',
                    'Raozan',
                    'Sandwip',
                    'Satkania'
                )
            },
            {
                'id': 4,
                'name': 'Cox\'s Bazar',
                'areas': (
                    'Chakaria',
                    'Cox\'s Bazar Sadar',
                    'Kutubdia',
                    'Maheshkhali',
                    'Ramu',
                    'Teknaf',
                    'Ukhia'
                )
            },
            {
                'id': 5,
                'name': 'Cumilla',
                'areas': (
                    'Barura',
                    'Brahmanpara',
                    'Burichang',
                    'Chandina',
                    'Cumilla Sadar',
                    'Daudkandi',
                    'Davidhar',
                    'Debidwar',
                    'Homna',
                    'Laksam',
                    'Monohorgonj',
                    'Muradnagar',
                    'Nangalkot',
                    'Titas'
                )
            }
        )
    },
    {
        'id': 2,
        'name': 'Dhaka',
        'districts': (
            {
                'id': 0,
                'name': 'Dhaka',
                'areas': (
                    'Dhamrai',
                    'Dohar',
                    'Keraniganj',
                    'Nawabganj',
                    'Savar',
                    'Dhaka Cantonment',
                    'Demra',
                    'Kadamtali',
                    'Khilgaon',
                    'Lalbagh',
                    'Mirpur',
                    'Mohammadpur',
                    'Motijheel',
                    'Pallabi',
                    'Ramna',
                    'Rampura',
                    'Sutrapur',
                    'Tejgaon',
                    'Uttara'
                )
            },
            {
                'id': 1,
                'name': 'Faridpur',
                'areas': (
                    'Alfadanga',
                    'Bhanga',
                    'Boalmari',
                    'Charbhadrasan',
                    'Faridpur Sadar',
                    'Madukhali',
                    'Nagarkanda',
                    'Sadarpur',
                    'Shriangan'
                )
            },
            {
                'id': 2,
                'name': 'Gazipur',
                'areas': (
                    'Gazipur Sadar',
                    'Kaliakair',
                    'Kaliganj',
                    'Kapasia',
                    'Sreepur'
                )
            },
            {
                'id': 3,
                'name': 'Gopalganj',
                'areas': (
                    'Gopalganj Sadar',
                    'Kashiani',
                    'Kotalipara',
                    'Muksudpur',
                    'Tungipara'
                )
            },
            {
                'id': 4,
                'name': 'Kishoreganj',
                'areas': (
                    'Austagram',
                    'Bajitpur',
                    'Bhairab',
                    'Hossainpur',
                    'Itna',
                    'Karimganj',
                    'Katiadi',
                    'Kishoreganj Sadar',
                    'Kuliarchar',
                    'Mithamain',
                    'Nikli',
                    'Pakundia',
                    'Tarail'
                )
            },
            {
                'id':5,
                'name': 'Madaripur',
                'areas': (
                    'Barhamganj',
                    'Kalkini',
                    'Madaripur Sadar',
                    'Rajoir'
                )
            },
            {
                'id': 6,
                'name': 'Manikganj',
                'areas': (
                    'Daulatpur',
                    'Ghior',
                    'Harirampur',
                    'Manikganj Sadar',
                    'Saturia',
                    'Shibalaya'
                )
            },
            {
                'id': 7,
                'name': 'Munshiganj',
                'areas': (
                    'Gazaria',
                    'Lohajang',
                    'Munshiganj Sadar',
                    'Sirajdikhan',
                    'Sreenagar',
                    'Tongibari'
                )
            },
            {
                'id': 8,
                'name': 'Narayanganj',
                'areas': (
                    'Araihazar',
                    'Bandar',
                    'Narayanganj Sadar',
                    'Rupganj',
                    'Sonargaon'
                )
            },
            {
                'id': 9,
                'name': 'Narsingdi',
                'areas': (
                    'Belabo',
                    'Monohardi',
                    'Narsingdi Sadar',
                    'Palash',
                    'Raipura',
                    'Shibpur'
                )
            },
            {
                'id': 10,
                'name': 'Rajbari',
                'areas': (
                    'Baliakandi',
                    'Goalandaghat',
                    'Pangsha',
                    'Rajbari Sadar'
                )
            },
            {
                'id': 11,
                'name': 'Shariatpur',
                'areas': (
                    'Bhedarganj',
                    'Damudya',
                    'Gosairhat',
                    'Naria',
                    'Shariatpur Sadar',
                    'Zajira'
                )
            },
            {
                'id': 12,
                'name': 'Tangail',
                'areas': (
                    'Basail',
                    'Bhuapur',
                    'Delduar',
                    'Dhanbari',
                    'Ghatail',
                    'Gopalpur',
                    'Kalihati',
                    'Madhupur',
                    'Mirzapur',
                    'Nagarpur',
                    'Sakhipur',
                    'Tangail Sadar'
                )
            },
            {
                'id': 13,
                'name': 'Narshingdi',
                'areas': (
                    'Narshingdi Sadar',
                    'Monohardi',
                    'Palash',
                    'Raipura',
                    'Shibpur'
                )
            }
        )
    },
    {
        'id': 3,
        'name': 'Khulna',
        'districts': (
            {
                'id': 0,
                'name': 'Bagerhat',
                'areas': (
                    'Bagerhat Sadar',
                    'Chitalmari',
                    'Fakirhat',
                    'Kachua',
                    'Mollahat',
                    'Mongla',
                    'Morrelganj',
                    'Rampal',
                    'Sarankhola'
                )
            },
            {
                'id': 1,
                'name': 'Chuadanga',
                'areas': (
                    'Alamdanga',
                    'Chuadanga Sadar',
                    'Damurhuda',
                    'Jibannagar'
                )
            },
            {
                'id': 2,
                'name': 'Jessore',
                'areas': (
                    'Abhaynagar',
                    'Bagherpara',
                    'Chaugachha',
                    'Jessore Sadar',
                    'Jhikargachha',
                    'Keshabpur',
                    'Manirampur',
                    'Sharsha'
                )
            },
            {
                'id': 3,
                'name': 'Jhenaidah',
                'areas': (
                    'Harinakunda',
                    'Jhenaidah Sadar',
                    'Kaliganj',
                    'Kotchandpur',
                    'Maheshpur',
                    'Shailkupa'
                )
            },
            {
                'id': 4,
                'name': 'Khulna',
                'areas': (
                    'Batiaghata',
                    'Dacope',
                    'Dighalia',
                    'Dumuria',
                    'Koyra',
                    'Paikgachha',
                    'Phultala',
                    'Rupsha',
                    'Terokhada'
                )
            },
            {
                'id': 5,
                'name': 'Kushtia',
                'areas': (
                    'Bheramara',
                    'Daulatpur',
                    'Khoksa',
                    'Kumarkhali',
                    'Kushtia Sadar',
                    'Mirpur'
                )
            },
            {
                'id': 6,
                'name': 'Magura',
                'areas': (
                    'Magura Sadar',
                    'Mohammadpur',
                    'Shalikha',
                    'Sreepur'
                )
            },
            {
                'id': 7,
                'name': 'Meherpur',
                'areas': (
                    'Gangni',
                    'Meherpur Sadar',
                    'Mujibnagar'
                )
            },
            {
                'id': 8,
                'name': 'Narail',
                'areas': (
                    'Kalia',
                    'Lohagara',
                    'Narail Sadar'
                )
            },
            {
                'id': 9,
                'name': 'Satkhira',
                'areas': (
                    'Assasuni',
                    'Debhata',
                    'Kalaroa',
                    'Kaliganj',
                    'Satkhira Sadar',
                    'Shyamnagar',
                    'Tala'
                )
            }
        )
    },
    {
        'id': 4,
        'name': 'Mymensingh',
        'districts': (
            {
                'id': 0,
                'name': 'Jamalpur',
                'areas': (
                    'Bakshiganj',
                    'Dewanganj',
                    'Islampur',
                    'Jamalpur Sadar',
                    'Melandaha',
                    'Sarishabari'
                )
            },
            {
                'id': 1,
                'name': 'Mymensingh',
                'areas': (
                    'Bhaluka',
                    'Dhobaura',
                    'Fulbaria',
                    'Gaffargaon',
                    'Gauripur',
                    'Haluaghat',
                    'Ishwarganj',
                    'Muktagachha',
                    'Mymensingh Sadar',
                    'Nandail',
                    'Phulpur',
                    'Trishal'
                )
            },
            {
                'id': 2,
                'name': 'Netrokona',
                'areas': (
                    'Atpara',
                    'Barhatta',
                    'Durgapur',
                    'Khaliajuri',
                    'Kalmakanda',
                    'Madan',
                    'Netrokona Sadar',
                    'Purbadhala'
                )
            },
            {
                'id': 3,
                'name': 'Sherpur',
                'areas': (
                    'Jhenaigati',
                    'Nakla',
                    'Nalitabari',
                    'Sherpur Sadar',
                    'Sreebardi'
                )
            }
        )
    },
    {
        'id': 5,
        'name': 'Rajshahi',
        'districts': (
            {
                'id': 0,
                'name': 'Bogra',
                'areas': (
                    'Adamdighi',
                    'Bogra Sadar',
                    'Dhunat',
                    'Dhupchanchia',
                    'Gabtali',
                    'Kahalu',
                    'Nandigram',
                    'Sariakandi',
                    'Shajahanpur',
                    'Sherpur',
                    'Shibganj',
                    'Sonatala'
                )
            },
            {
                'id': 1,
                'name': 'Joypurhat',
                'areas':(
                    'Akkelpur',
                    'Joypurhat Sadar',
                    'Kalai',
                    'Khetlal',
                    'Panchbibi'
                )
            },
            {
                'id': 2,
                'name': 'Naogaon',
                'areas': (
                    'Atrai',
                    'Badalgachhi',
                    'Dhamoirhat',
                    'Manda',
                    'Naogaon Sadar',
                    'Niamatpur',
                    'Patnitala',
                    'Porsha',
                    'Raninagar',
                    'Sapahar'
                )
            },
            {
                'id': 3,
                'name': 'Natore',
                'areas': (
                    'Bagatipara',
                    'Baraigram',
                    'Gurudaspur',
                    'Lalpur',
                    'Natore Sadar',
                    'Singra'
                )
            },
            {
                'id': 4,
                'name': 'Nawabganj',
                'areas': (
                    'Bholahat',
                    'Gomastapur',
                    'Nachole',
                    'Nawabganj Sadar',
                    'Shibganj'
                )
            },
            {
                'id': 5,
                'name': 'Pabna',
                'areas': (
                    'Atgharia',
                    'Bera',
                    'Bhangura',
                    'Chatmohar',
                    'Faridpur',
                    'Ishwardi',
                    'Pabna Sadar',
                    'Santhia',
                    'Sujanagar'
                )
            },
            {
                'id': 6,
                'name': 'Rajshahi',
                'areas': (
                    'Bagha',
                    'Bagmara',
                    'Charghat',
                    'Durgapur',
                    'Godagari',
                    'Mohanpur',
                    'Paba',
                    'Puthia',
                    'Tanore'
                )
            },
            {
                'id': 7,
                'name': 'Sirajganj',
                'areas': (
                    'Belkuchi',
                    'Chauhali',
                    'Kamarkhanda',
                    'Kazipur',
                    'Raiganj',
                    'Shahjadpur',
                    'Sirajganj Sadar',
                    'Tarash'
                )
            }
        )
    },
    {
        'id': 6,
        'name': 'Rangpur',
        'districts': (
            {
                'id': 0,
                'name': 'Dinajpur',
                'areas': (
                    'Birampur',
                    'Birganj',
                    'Bochaganj',
                    'Chirirbandar',
                    'Phulbari',
                    'Ghoraghat',
                    'Hakimpur',
                    'Kaharole',
                    'Khansama',
                    'Dinajpur Sadar',
                    'Nawabganj',
                    'Parbatipur'
                )
            },
            {
                'id': 1,
                'name': 'Gaibandha',
                'areas': (
                    'Fulchhari',
                    'Gaibandha Sadar',
                    'Gobindaganj',
                    'Palashbari',
                    'Sadullapur',
                    'Saghata',
                    'Sundarganj'
                )
            },
            {
                'id': 2,
                'name': 'Kurigram',
                'areas': (
                    'Bhurungamari',
                    'Char Rajibpur',
                    'Chilmari',
                    'Kurigram Sadar',
                    'Nageshwari',
                    'Phulbari',
                    'Raomari',
                    'Rajarhat',
                    'Ulipur'
                )
            },
            {
                'id': 3,
                'name': 'Lalmonirhat',
                'areas': (
                    'Aditmari',
                    'Hatibandha',
                    'Kaliganj',
                    'Lalmonirhat Sadar',
                    'Patgram'
                )
            },
            {
                'id': 4,
                'name': 'Nilphamari',
                'areas': (
                    'Dimla',
                    'Domar',
                    'Jaldhaka',
                    'Kishoreganj',
                    'Nilphamari Sadar',
                    'Saidpur'
                )
            },
            {
                'id': 5,
                'name': 'Panchagarh',
                'areas': (
                    'Atwari',
                    'Boda',
                    'Debiganj',
                    'Panchagarh Sadar',
                    'Tetulia'
                )
            },
            {
                'id': 6,
                'name':
                'Rangpur',
                'areas': (
                    'Badarganj',
                    'Gangachara',
                    'Kaunia',
                    'Mithapukur',
                    'Pirgachha',
                    'Pirganj',
                    'Rangpur Sadar',
                    'Taraganj'
                )
            },
            {
                'id': 7,
                'name': 'Thakurgaon',
                'areas': (
                    'Baliadangi',
                    'Haripur',
                    'Pirganj',
                    'Ranisankail',
                    'Thakurgaon Sadar'
                )
            }
        )
    },
    {
        'id': 7,
        'name': 'Sylhet',
        'districts': (
            {
                'id': 0,
                'name': 'Habiganj',
                'areas': (
                    'Ajmiriganj',
                    'Bahubal',
                    'Baniachong',
                    'Chunarughat',
                    'Habiganj Sadar',
                    'Lakhai',
                    'Madhabpur',
                    'Nabiganj'
                )
            },
            {
                'id': 1,
                'name': 'Moulvibazar',
                'areas': (
                    'Barlekha',
                    'Juri',
                    'Kamalganj',
                    'Kulaura',
                    'Moulvibazar Sadar',
                    'Rajnagar',
                    'Sreemangal'
                )
            },
            {
                'id': 2,
                'name': 'Sunamganj',
                'areas': (
                    'Bishwamvarpur',
                    'Chhatak',
                    'Dharampasha',
                    'Dowarabazar',
                    'Jamalganj',
                    'Shalla',
                    'Sunamganj Sadar',
                    'Tahirpur'
                )
            },
            {
                'id': 3,
                'name': 'Sylhet',
                'areas': (
                    'Balaganj',
                    'Beanibazar',
                    'Bishwanath',
                    'Fenchuganj',
                    'Golapganj',
                    'Gowainghat',
                    'Jaintiapur',
                    'Kanaighat',
                    'Zakiganj',
                    'Sylhet Sadar'
                )
            }
        )
    }
)


def get_divisions(request):
    return JsonResponse(DIVISIONS, safe=False)

def get_division_name(id):
    name =  DIVISIONS[int(id)]['name']
    if name:
        return name
    return ''

def get_district_name(division_id, district_id):
    name= DIVISIONS[int(division_id)]['districts'][int(district_id)]['name']
    if name:
        return name
    return ''

def get_districts(request):
    division_id = int(request.GET.get('division'))
    return JsonResponse(DIVISIONS[division_id]['districts'], safe=False)

def get_areas(request):
    division_id = int(request.GET.get('division'))
    district_id= int(request.GET.get('district'))
    return JsonResponse(DIVISIONS[division_id]['districts'][district_id]['areas'], safe=False)