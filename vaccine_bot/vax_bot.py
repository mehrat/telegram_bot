import schedule
import time
import datetime;
import requests
import json

def job():
  print("I'm working...")
  print(datetime.datetime.now())
  # response = requests.request("GET", "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin?pincode=250004&date=01-05-2021")
  # print(response.text)
  # vaccine_data = json.loads(response.text)
  vaccine_data = {
    "centers": [
      {
        "center_id": 692599,
        "name": "CCS UNIVERSITY HOSPIT 18 TO 44",
        "state_name": "Uttar Pradesh",
        "district_name": "Meerut",
        "block_name": "Medical PPC",
        "pincode": 250004,
        "lat": 28,
        "long": 77,
        "from": "12:00:00",
        "to": "17:00:00",
        "fee_type": "Free",
        "sessions": [
          {
            "session_id": "8288af1b-edc1-40a6-94df-0c6d7fa9ddc9",
            "date": "01-05-2021",
            "available_capacity": 0,
            "min_age_limit": 18,
            "vaccine": "",
            "slots": [
              "12:00PM-01:00PM",
              "01:00PM-02:00PM",
              "02:00PM-03:00PM",
              "03:00PM-05:00PM"
            ]
          }
        ]
      },
      {
        "center_id": 692566,
        "name": "LLRM CENTRAL LIBRARY A18 To 44",
        "state_name": "Uttar Pradesh",
        "district_name": "Meerut",
        "block_name": "Medical PPC",
        "pincode": 250004,
        "lat": 28,
        "long": 77,
        "from": "12:00:00",
        "to": "17:00:00",
        "fee_type": "Free",
        "sessions": [
          {
            "session_id": "625f8aca-40dc-4c30-8024-af0fb5abd370",
            "date": "01-05-2021",
            "available_capacity": 0,
            "min_age_limit": 18,
            "vaccine": "",
            "slots": [
              "12:00PM-01:00PM",
              "01:00PM-02:00PM",
              "02:00PM-03:00PM",
              "03:00PM-05:00PM"
            ]
          }
        ]
      },
      {
        "center_id": 558457,
        "name": "LLRM MEDICAL NEW OPD",
        "state_name": "Uttar Pradesh",
        "district_name": "Meerut",
        "block_name": "Medical PPC",
        "pincode": 250004,
        "lat": 28,
        "long": 77,
        "from": "09:00:00",
        "to": "17:00:00",
        "fee_type": "Free",
        "sessions": [
          {
            "session_id": "822ea462-2ddc-4aa1-86f6-ffb3dd24e14d",
            "date": "01-05-2021",
            "available_capacity": 24,
            "min_age_limit": 45,
            "vaccine": "",
            "slots": [
              "09:00AM-11:00AM",
              "11:00AM-01:00PM",
              "01:00PM-03:00PM",
              "03:00PM-05:00PM"
            ]
          }
        ]
      },
      {
        "center_id": 560136,
        "name": "UPHC KASERU BAXER",
        "state_name": "Uttar Pradesh",
        "district_name": "Meerut",
        "block_name": "Rajpura",
        "pincode": 250004,
        "lat": 29,
        "long": 78,
        "from": "09:00:00",
        "to": "17:00:00",
        "fee_type": "Free",
        "sessions": [
          {
            "session_id": "db1c42e1-9c4f-4f4f-a1b7-f73ee404356d",
            "date": "01-05-2021",
            "available_capacity": 75,
            "min_age_limit": 45,
            "vaccine": "",
            "slots": [
              "09:00AM-11:00AM",
              "11:00AM-01:00PM",
              "01:00PM-03:00PM",
              "03:00PM-05:00PM"
            ]
          }
        ]
      },
      {
        "center_id": 670881,
        "name": "LLRM ONLINE CENTRAL LIBRARY",
        "state_name": "Uttar Pradesh",
        "district_name": "Meerut",
        "block_name": "Medical PPC",
        "pincode": 250004,
        "lat": 28,
        "long": 77,
        "from": "09:00:00",
        "to": "17:00:00",
        "fee_type": "Free",
        "sessions": [
          {
            "session_id": "7ef43179-56c0-4aa8-af6f-84eeed1c00fc",
            "date": "01-05-2021",
            "available_capacity": 76,
            "min_age_limit": 45,
            "vaccine": "",
            "slots": [
              "09:00AM-11:00AM",
              "11:00AM-01:00PM",
              "01:00PM-03:00PM",
              "03:00PM-05:00PM"
            ]
          }
        ]
      },
      {
        "center_id": 692541,
        "name": "LLRM CENTRAL LIBRARY B18 To 44",
        "state_name": "Uttar Pradesh",
        "district_name": "Meerut",
        "block_name": "Medical PPC",
        "pincode": 250004,
        "lat": 28,
        "long": 77,
        "from": "12:00:00",
        "to": "17:00:00",
        "fee_type": "Free",
        "sessions": [
          {
            "session_id": "ac09c2dd-a164-435c-88e4-d40bf9e90079",
            "date": "01-05-2021",
            "available_capacity": 0,
            "min_age_limit": 18,
            "vaccine": "",
            "slots": [
              "12:00PM-01:00PM",
              "01:00PM-02:00PM",
              "02:00PM-03:00PM",
              "03:00PM-05:00PM"
            ]
          }
        ]
      },
      {
        "center_id": 569386,
        "name": "CHC BHAWANPUR",
        "state_name": "Uttar Pradesh",
        "district_name": "Meerut",
        "block_name": "Rajpura",
        "pincode": 250004,
        "lat": 28,
        "long": 77,
        "from": "09:00:00",
        "to": "17:00:00",
        "fee_type": "Free",
        "sessions": [
          {
            "session_id": "03a213be-16cc-4718-9713-35f50efb60fc",
            "date": "01-05-2021",
            "available_capacity": 127,
            "min_age_limit": 45,
            "vaccine": "",
            "slots": [
              "09:00AM-11:00AM",
              "11:00AM-01:00PM",
              "01:00PM-03:00PM",
              "03:00PM-05:00PM"
            ]
          }
        ]
      },
      {
        "center_id": 629800,
        "name": "NUTEMA HOSPITAL",
        "state_name": "Uttar Pradesh",
        "district_name": "Meerut",
        "block_name": "Meerut",
        "pincode": 250004,
        "lat": 28,
        "long": 77,
        "from": "12:00:00",
        "to": "16:00:00",
        "fee_type": "Paid",
        "sessions": [
          {
            "session_id": "9e1fe189-4fb8-43de-955c-e3b12d6137db",
            "date": "03-05-2021",
            "available_capacity": 26,
            "min_age_limit": 45,
            "vaccine": "COVISHIELD",
            "slots": [
              "12:00PM-01:00PM",
              "01:00PM-02:00PM",
              "02:00PM-03:00PM",
              "03:00PM-04:00PM"
            ]
          },
          {
            "session_id": "e97e5653-ac4d-4cda-beb9-764c98deeb90",
            "date": "04-05-2021",
            "available_capacity": 0,
            "min_age_limit": 45,
            "vaccine": "COVISHIELD",
            "slots": [
              "12:00PM-01:00PM",
              "01:00PM-02:00PM",
              "02:00PM-03:00PM",
              "03:00PM-04:00PM"
            ]
          },
          {
            "session_id": "9ced6b53-ebf4-4eff-8892-a4ffc84242e4",
            "date": "05-05-2021",
            "available_capacity": 0,
            "min_age_limit": 45,
            "vaccine": "COVISHIELD",
            "slots": [
              "12:00PM-01:00PM",
              "01:00PM-02:00PM",
              "02:00PM-03:00PM",
              "03:00PM-04:00PM"
            ]
          }
        ],
        "vaccine_fees": [
          {
            "vaccine": "COVISHIELD",
            "fee": "250"
          }
        ]
      }
    ]
  }
  for vd in vaccine_data["centers"]:
    for ses in vd["sessions"]:
      if ses['min_age_limit']==45 and ses['available_capacity'] > 0:
        print (vd['name'])
        print (vd['pincode'])
        print (ses['date'])
        sendTelegramNotification(vd['name'], vd['pincode'], ses['date'])

def sendTelegramNotification(name, pincode, vcdate):
  bot_token = ''
  bot_chatID =extract_chat_id()

  send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + str(bot_chatID) + '&parse_mode=Markdown&text=' + "I am bot!!"
  print (send_text)
  response = requests.get(send_text)

def extract_chat_id():
  bot_token = ''
  message_url = 'https://api.telegram.org/'+ bot_token +'/getUpdates'
  print (message_url)
  message_response = requests.get(message_url)
  print (message_response)
  mes = json.loads(message_response.text)
  return mes["result"][0]["message"]["from"]["id"]



job()

# schedule.every(10).seconds.do(job)
#
#
# while True:
#     schedule.run_pending()
