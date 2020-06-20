
import pandas as pd

# Useful debugging code
# ---------------------------

# Match a value
# print(government_master[government_master['incidentnum'].str.match(search_param)])


# ---------------------------



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

    incident_numbers = people_master[1].tolist()
    print (len(incident_numbers))

    # incident_number = people_master.at[1, 1]
    # print ("People Incident Number: " + incident_number)

    # Government
    government_master = pd.read_csv('./dallas_police_government.csv')
    # government_incident_number = government_master.at[1, 'incidentnum']

    # search_param = "-".join(incident_number.split('-')[0:2])

    ###
    results = government_master[government_master['incidentnum'].isin(incident_numbers)]
    print (results)

    # result = pd.merge(government_master, people_master, left_on='incidentnum')



