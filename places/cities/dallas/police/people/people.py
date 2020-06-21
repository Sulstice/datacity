
import pandas as pd
import json
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

# Useful debugging code
# ---------------------------

# Match a value
# print(government_master[government_master['incidentnum'].str.match(search_param)])
#
# print (government_master.shape)
# print (people_master.shape)
#
# government_cases_reported = government_master[government_master['incidentnum'].isin(incident_numbers)]
# print ("Government Cases Reported: ")
#
# incident_numbers_found = government_cases_reported['incidentnum'].to_list()
# print ("Incident Numbers Found: " + str(len(incident_numbers_found)))
#
#
# incident_numbers_not_reported = list(set(incident_numbers) - set(incident_numbers_found))
# print ()
# print ("Incident Numbers Not Reported: " + str(len(incident_numbers_not_reported)))
#
#
# cases_not_reported = people_master[people_master[1].isin(incident_numbers_not_reported)]
# print ("Cases Not Reported: " )
# print (cases_not_reported)

# ---------------------------

HEADERS = {
    0: "Class",
    1: "Incident",
    2: "Crime",
    3: "Date/Time",
    4: "Location",
    5: "Address",
    6: "Accuracy",
    7: "Agency"
}

# Constants
# ---------
BEGINNING_DATE = "2020-06-08"
ENDING_DATE = "2020-06-15"

if __name__ == '__main__':


    import os

    # Load People
    dataframes = []
    for filename in os.listdir('./'):
        if filename.endswith(".htm"):
            dataframes.extend(pd.read_html(filename, match='Dallas Police Department'))
            continue
        else:
            continue

    people_master = pd.concat(dataframes, ignore_index=True)
    people_master[1] = people_master[1].map(lambda x: "-".join(x.split('-')[0:2]))
    community_map_incident_numbers = people_master[1].tolist()

    payload = {}

    # Government
    government_master = pd.read_csv('./dallas_police_government2.csv')
    government_incident_numbers = government_master["incidentnum"].tolist()

    community_crime_map_missing_incidents = list(set(government_incident_numbers) - set(community_map_incident_numbers))
    government_missing_incidents = list(set(community_map_incident_numbers) - set(government_incident_numbers))

    # Prepare payload
    payload["query_beginning_date"] = BEGINNING_DATE
    payload["query_ending_date"] = ENDING_DATE
    payload["city"] = "dallas"
    payload["state"] = "TX"
    payload["country"] = "United States of America"
    payload["community_crime_map_incidents_reported"] = len(community_map_incident_numbers)
    payload["government_incidents_reported"] = len(government_incident_numbers)
    payload["incident_count_difference"] = government_master.shape[0] - people_master.shape[0]
    payload["community_crime_map_missing_incident_numbers"] = community_crime_map_missing_incidents
    payload["government_missing_incident_numbers"] = government_missing_incidents

    with open("government_community_crime_map_incident_payload.json", "w") as outfile:
        json.dump(payload, outfile,  indent=4, sort_keys=True)

