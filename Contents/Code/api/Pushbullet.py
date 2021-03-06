import ssl
import urllib2
import traceback

PUSHBULLET_API_URL = "https://api.pushbullet.com/v2/"

PUSHBULLET_API_KEY = ""

def setAPI(api):
    global PUSHBULLET_API_KEY
    PUSHBULLET_API_KEY = api

def send(title, body, pb_type='note', channel="", device_iden=""):
    api_header = {'Authorization': 'Bearer ' + PUSHBULLET_API_KEY,
                  'Content-Type': 'application/json'
                  }
    data = {'type': pb_type, 'title': title, 'body': body}
    if device_iden:
        data['device_iden'] = device_iden
    if channel:
        data['channel_tag'] = channel
    values = JSON.StringFromObject(data)
    ctx = ssl.SSLContext(ssl.PROTOCOL_TLSv1)
    try:
        pushbulletrequest = urllib2.Request(PUSHBULLET_API_URL + "pushes", data=values, headers=api_header)
        return urllib2.urlopen(pushbulletrequest, context=ctx)
    except Exception as e:
        Log.Debug("Error in send: " + e.message)
        Log.Error(str(traceback.format_exc()))  # raise last error
    return
