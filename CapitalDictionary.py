print("CAPITAL DICTIONARY")
print('Type a country in Asia:')

country = input()
Asia = {'Afghanistan': 'Kabul', 'Armenia': 'Yerevan', 'Azerbaijan': 'Baku', 'Bahrain': 'Manama', 'Bangladesh': 'Dhaka', 'Bhutan': 'Thimphu', 'Brunei': 'Bandar Seri Begawan', 'Cambodia':'Phnom Penh',  
        'China': 'Beijing', 'Cyprus': 'Nicosia', 'Georgia': 'Tbilisi', 'India': 'New Delhi', 'Indonesia': 'Jakarta', 'Iran': 'Tehran', 'Iraq': 'Baghdad', 'Israel': 'Jerusalem', 'Japan': 'Tokyo', 'Jordan': 'Amman', 'Kazakhstan': 'Astana', 'Kuwait': 'Kuwait City', 'Kyrgyzstan':'Bishkek',
        'Laos': 'Vientiane', 'Lebanon': 'Beirut', 'Malaysia': 'Kuala Lumpur', 'Maldives': 'Male', 'Mongolia': 'Ulaanbaatar', 'Myanmar':'Naypyidaw', 'Nepal': 'Kathmandu', 'North Korea': 'Pyongyang', 'Oman': 'Muscat', 'Pakistan': 'Isamabad', 'Palestine' : 'Jerusalem(East)', 'Philippines': 'Manila', 'Qatar': 'Doha',
        'Russia' : 'Moscow', 'Saudi Arabia': 'Riyadh', 'Singapore': 'Singapore', 'South Korea': 'Seoul', 'Sri Lanka': 'Sri Jayawardenepura Kotte', 'Syria': 'Damascus', 'Taiwan': 'Taipei', 'Tajikistan': 'Dushanbe', 'Thailand': 'Bangkok', 'Timor-Leste': 'Dili', 'Turkey': 'Ankara', 'Turkmenistan':'Ashgabat', 'United Arab Emirates': 'Abu Dhabi', 'Uzbekistan': 'Tashkent', 'Vietnam':'Hanoi',
        'Yemen': "Sana'a" }

cap = Asia[country]

print("The country's capital: " + cap)