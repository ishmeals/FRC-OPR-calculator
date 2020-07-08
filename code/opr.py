import numpy as np
import pickle
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import os


id = '1tBf0YKXdqrcKlKkN4dv1hALj7ZQSP9wOv6X00jebCD8'
creds = None
scopes = ['https://www.googleapis.com/auth/spreadsheets']

if os.path.exists('token.pickle'):
    with open('token.pickle', 'rb') as token:
        creds = pickle.load(token)
if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
        creds.refresh(Request())
    else:
        flow = InstalledAppFlow.from_client_secrets_file('creds.json', scopes)
        creds = flow.run_local_server(port=0)
    with open('token.pickle', 'wb') as token:
        pickle.dump(creds, token)

service = build('sheets', 'v4', credentials=creds)
sheet = service.spreadsheets()


def update():
    result = sheet.values().get(spreadsheetId=id, range='Results!B2:I').execute()['values']
    keys = []

    try:
        for row in result:
            for i in range(6):
                team = int(row[i])
                if team not in keys:
                    keys.append(team)

        n = len(keys)
        m = len(result)

        matches = np.zeros((m * 2, n))
        scores = np.zeros(m * 2)

        for row in range(m):
            scores[row * 2] = int(result[row][6])
            scores[row * 2 + 1] = int(result[row][7])

            matches[row * 2][keys.index(int(result[row][0]))] = 1
            matches[row * 2][keys.index(int(result[row][1]))] = 1
            matches[row * 2][keys.index(int(result[row][2]))] = 1
            matches[row * 2 + 1][keys.index(int(result[row][3]))] = 1
            matches[row * 2 + 1][keys.index(int(result[row][4]))] = 1
            matches[row * 2 + 1][keys.index(int(result[row][5]))] = 1
    except ValueError:
        print('ValueError')
        return
    except IndexError:
        print('IndexError')
        return

    opr = np.linalg.solve(np.dot(matches.T, matches), np.dot(matches.T, scores))

    body = {
            "range": "OPR!A2",
            "majorDimension": "COLUMNS",
            "values": [
                list(keys),
                list(opr)
            ]
    }

    sheet.values().update(spreadsheetId=id, range='OPR!A2', valueInputOption='USER_ENTERED', body=body).execute()


update()
