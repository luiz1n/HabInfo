from json.decoder import JSONDecodeError
import requests, json

class HabboAPI:

    def __init__(self):
        self.hotel = None
        self.globalUrl = None
        self.apiurl = None

        self.habbo = ""
        self.apiUsers = ""

    def setHotel(self, hotel):
        '''
            .com.br
            .com
            .fr
            .es
            .nl
            .it
            .de
        '''
        self.hotel=hotel
        if hotel != "sandbox":
            self.globalUrl=f"https://www.habbo{hotel}"
            self.apiUsers=f"{self.globalUrl}/api/public/users?name={self.habbo}"
        else:
            self.globalUrl="https://www.sandbox.habbo.com"

    def setHabbo(self, username):
        self.habbo = username

    def getFigureString(self):
        data = json.loads(requests.get(self.apiUsers).text)
        try:
            if "figureString" in data:
                return data["figureString"]
            else:
                return data
        except KeyError:
            return data

    def getUniqueId(self):
        data = json.loads(requests.get(self.apiUsers).text)
        try:
            if "uniqueId" in data:
                return data["uniqueId"]
            else:
                return 
        except KeyError:
            return data

    def getMotto(self):
        data = json.loads(requests.get(self.apiUsers).text)
        try:
            if "motto" in data:
                return data["motto"]
            else:
                return data
        except KeyError:
            return data

    def isOnline(self):
        data = json.loads(requests.get(self.apiUsers).text)
        try:
            if "online" in data:
                return data["online"]
            else:
                return data
        except KeyError:
            return data

    def getLastAccessTime(self):
        data = json.loads(requests.get(self.apiUsers).text)
        try:
            if "lastAccessTime" in data:
                return data["lastAccessTime"]
            else:
                return data
        except KeyError:
            return data

    def getMemberSince(self):
        data = json.loads(requests.get(self.apiUsers).text)
        try:
            if "memberSince" in data:
                return data["memberSince"]
            else:
                return data
        except KeyError:
            return data

    def getProfileVisible(self):
        data = json.loads(requests.get(self.apiUsers).text)
        try:
            if "profileVisible" in data:
                return data["profileVisible"]
            else:
                return data
        except KeyError:
            return data

    def getLevel(self):
        data = json.loads(requests.get(self.apiUsers).text)
        try:
            if "currentLevel" in data:
                return data["currentLevel"]
            else:
                return data
        except KeyError:
            return data

    def getCurrentLevelCompletePercent(self):
        data = json.loads(requests.get(self.apiUsers).text)
        try:
            if "currentLevelCompletePercent" in data:
                return data["currentLevelCompletePercent"]
            else:
                return data
        except KeyError:
            return data
    def getTotalExperience(self):
        data = json.loads(requests.get(self.apiUsers).text)
        try:
            if "totalExperience" in data:
                return data["totalExperience"]
            else:
                return data
        except KeyError:
            return data

    def getStarGem(self):
        data = json.loads(requests.get(self.apiUsers).text)
        try:
            if "starGemCount" in data:
                return data["starGemCount"]
            else:
                return data
        except KeyError:
            return data 

    def getBadges(self, key=""):
        badges = []
        data = json.loads(requests.get(self.apiUsers).text)
        try:
            for badge in data['selectedBadges']:
                badges.append(badge[key] if key != "" else badge)
            return badges
        except KeyError:
            return data

    def getPhotos(self, key=""):
        profileId = self.getUniqueId()

        users_likes = []

        photosUrl = f'{self.globalUrl}/extradata/public/users/{profileId}/photos'
        data = json.loads(requests.get(photosUrl).text)
        for d in data:
            if key == "likes":
                for likes in d['likes']:
                    users_likes.append(likes)
                return users_likes
            else:
                try:
                    return d[key] if key != "" else d
                except KeyError:
                    return data

    def getGroups(self, groupid="", key=""):
        groupUrl = f'{self.globalUrl}/api/public/groups/{groupid}'
        data = json.loads(requests.get(groupUrl).text)
        for d in data:
            try:
                return d[key] if key != "" else d
            except KeyError:
                return data

    def getProfile(self, key="", tip=""):
        profileId = self.getUniqueId()
        urlProfile = f'{self.globalUrl}/api/public/users/{profileId}/profile'
        data = json.loads(requests.get(urlProfile).text)

        try:
            if key.lower() == "friends":
                friends=[]
                for friend in data['friends']:
                    friends.append(friend[tip] if tip != "" else friend)
                return friends

            elif key.lower() == "groups":
                groups = []
                for group in data['groups']:
                    groups.append(group[tip] if tip != "" else group)
                return groups

            elif key.lower() == "rooms":
                rooms=[]
                for room in data['rooms']:
                    rooms.append(room[tip] if tip != "" else room)
                return rooms

            elif key.lower() == "badges":
                badges=[]
                for badge in data['badges']:
                    badges.append(badge[tip] if tip != "" else badges)
                return badges
        except KeyError:
            return data
        else:
            return data
