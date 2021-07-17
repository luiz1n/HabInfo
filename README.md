# HabInfo
Get Habbo Info by Discord


## Usage API

Get Started
```python
from hbapi import hbapi

api = HabboAPI()

api.setHabbo("test") # Set account Username
api.setHotel(".com.br") # Set hotel for api. | .com.br | .com | .de | .it | .fr | .es | .nl
```

### Get Info from User
Badges
```python
badgeName = api.getBadges("name")
badgeDescription = api.getBadges("description")
badgeCode = api.getBadges("code")
```
Photos
```python
photoPreviewUrl = api.getPhotos("previewUrl")
creatorId = api.getPhotos("creator_uniqueId")
creatorName = api.getPhotos("creator_name")
time_unix = api.getPhotos("time")
room_id = api.getPhotos("room_id")
photo_id = api.getPhotos("id")
```
Other Info
```python
api.getStarGem() # Get the user total star gem
api.getTotalExperience() # Get total experience
api.getCurrentLevelCompletePercent() # Get the user CurrentLevelCompletePercent
api.getLevel() # Get level from user
api.getProfileVisible() # Get if the user profile is visible
api.getMemberSince() # Get user account creation date
api.getLastAccessTime() # Get the date the user last accessed
api.isOnline() # Get if the user is currently online
api.getMotto() # Get the user motto
api.getUniqueId() # Get the user UniqueId
api.getFigureString() # Get the user figurestring
```
