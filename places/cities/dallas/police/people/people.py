
import pandas as pd
import json
import fuzzy_pandas as fpd

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


    # ----------------------------------------SECTION 1 ------------------------------------------------

    import os

    # ------------ LOAD COMMUNITY MAP -----------
    dataframes = []
    for filename in os.listdir('./'):
        if filename.endswith(".htm"):
            dataframes.extend(pd.read_html(filename, match='Dallas Police Department'))
            continue
        else:
            continue
    people_master = pd.concat(dataframes, ignore_index=True)
    people_master[1] = people_master[1].map(lambda x: "-".join(x.split('-')[0:2]))

    # ------------ SPOT CRIME MAP -----------
    spotcrime_master = pd.read_json('./spot_crime.json')
    spotcrime_master["lon"] = spotcrime_master["lon"].astype(str)
    spotcrime_master["lat"] = spotcrime_master["lat"].astype(str)
    mask = (spotcrime_master['date'] > BEGINNING_DATE) & (spotcrime_master['date'] <= ENDING_DATE)
    spotcrime_master = spotcrime_master.loc[mask]

    spotcrime_incidents = spotcrime_master["cdid"].to_list()

    # ------------ GOVERNMENT ---------------
    government_master = pd.read_csv('./dallas_police_government2.csv')
    government_master["lat"] = government_master["geocoded_column"].map(lambda x: json.loads(x.replace("'", '!!!').replace('"', "'").replace('!!!', '"')))
    government_master["lon"] = government_master["geocoded_column"].map(lambda x: json.loads(x.replace("'", '!!!').replace('"', "'").replace('!!!', '"')))

    lat_list = government_master["lat"].to_list()
    lon_list = government_master["lon"].to_list()

    lat_list_new = []
    lon_list_new = []

    for i in lat_list:
        if 'latitude' in i:
            lat_list_new.append(str(i["latitude"]))
            lon_list_new.append(str(i["longitude"]))
        else:
            lat_list_new.append('na')
            lon_list_new.append('na')

    government_master["lat"] = lat_list_new
    government_master["lon"] = lon_list_new

    date_list = government_master["date1"].to_list()
    time_list = government_master["time1"].to_list()

    new_date_column = []
    for i in range(0, len(date_list)):
        fixed_date = date_list[i].replace("00:00", str(time_list[i]), 1)
        new_date_column.append(fixed_date)

    government_master["date"] = new_date_column

    # government_master["lon"] = government_master["geocoded_column"].map(lambda x: x)


    # -------------------------------------------------------------------------------------------------

    community_map_incident_numbers = people_master[1].tolist()
    payload = {}

    # Government
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
    payload["spot_crime_incident_numbers"] = len(spotcrime_incidents)

    government_master["date1"] = government_master["date1"].astype(str)
    spotcrime_master["date"] = spotcrime_master["date"].astype(str)


    # Fuzzy Matching

    matches = fpd.fuzzy_merge(government_master, spotcrime_master,
                              left_on=['incident_address', 'lat', 'lon', 'date'],
                              right_on=['address', 'lat', 'lon', 'date'],
                              ignore_case=True,
                              # method='levenshtein',
                              method='bilenko',
                              threshold=0.40)

    missing = list(set(spotcrime_master['cdid'].to_list()) - set(matches['cdid'].to_list()))
    payload["spot_crime_missing_incident_numbers"] = len(missing)

    with open("../../../../../data/government_community_crime_map_incident_payload.json", "w") as outfile:
        json.dump(payload, outfile,  indent=4, sort_keys=True)
