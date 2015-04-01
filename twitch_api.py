import urllib.request
import json
import sys
import webbrowser

# GitHub-Doku der Twitch-API
# https://github.com/justintv/Twitch-API

base_url = 'https://api.twitch.tv/kraken/'


def requesting_json_object(url):
    data = urllib.request.urlopen(url)
    inhalt = data.read().decode('utf-8')
    json_object = json.loads(inhalt)
    return json_object

def pruefe_channel(channel_name):
    url = base_url + 'streams/' + channel_name
    try:
        json_object = requesting_json_object(url)
    except:
        print('Channel ' + channel_name + ' existiert nicht.\n')
        return False
    if json_object['stream'] == None:
        print(channel_name + " ist offline.\n")
        return False
    else:
        gib_channel_infos_aus(json_object)
        return channel_name

def gib_channel_infos_aus(json_object):
    print(json_object['stream']['channel']['name'] + " online: ")
    print("|\tViewer: " + str(json_object['stream']['viewers']))
    # print("|\tPreview-Pic: " + str(json_object['stream']['preview']['large']))
    try:
        print("|\tStatus: " + json_object['stream']['channel']['status'])
    except:
        print("|\tStatus: Status nicht lesbar.")
    print("|\tGame: " + json_object['stream']['channel']['game'])
    print("|\tURL: " + json_object['stream']['channel']['url'])
    print("|_____________________________\n")
    

def channel_liste_checken(channel_namen):
    print("Folgende Channels sind on:\n")
    channels_online = []
    for channel in channel_namen:
        tmp = pruefe_channel(channel)
        if tmp != False:
            channels_online.append(tmp)
    return channels_online
    

def lade_channel_liste_von_file():
    try:
        datei = open('channels.txt', 'r')
        inhalt = datei.read().strip().rstrip(',').split(',')
        ergebnis = []
        for i in inhalt:
            ergebnis.append(i.strip())
        return ergebnis
    except:
        print('Fehler in der channels.txt (nicht vorhanden?). Beachte, dass die Channelnamen mit: , voneinander getrennt sein muessen.')
        a = input("<Return> zum beenden")
        sys.exit()

def channels_im_browser_oeffnen(channels_online):
    print("\n-----------------------------------------------------------------")
    print("Ziffer + <Return> zum Oeffnen im Browser, nur <Return> zum beenden")
    print("-----------------------------------------------------------------\n")
    for idx, val in enumerate(channels_online):
        print("{}: {}".format(idx, val))
    eingabe = input("")
    if eingabe == "":
        sys.exit()
    else:
        try:
            webbrowser.open_new_tab('http://twitch.tv/' + channels_online[int(eingabe)])
        except:
            print("Zu doof um ne richtige Zahl einzugeben!")
            a = input("<Return> zum beenden")

liste = lade_channel_liste_von_file()
channels_online = channel_liste_checken(liste)
channels_im_browser_oeffnen(channels_online)

