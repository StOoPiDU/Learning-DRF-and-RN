# Learning-DRF-and-RN
 * Note: I have never had to start a project withexpo or node built already, so you need to build those on your own and I'm not completely positive that I did the install commands right lol

Showcasing some stuff from learning DNF and React Native. I didn't spend a lot of time on RN since I already have some experience in React.js, but not a lot in DRF.

Basic build and implementation of an API built in Django REST Framework, then linking to it with React Native.

Most of it is pretty boilerplate to be honest, but this at least shows that I can make the things and get them to places.

This houses a simple serializer, model, view and url page. Some edits to the settings.py file, and the slightest bit of adjustment to admin I guess. I included some slight authentication to force a user to be an admin to make a post, but the current build is capable of viewing everything. I didn't do anything with more user stuff but the auth is there for it.

Then I make a simple React Native setup using expo and link the API_URL to DRF (to do this, I just simply made it accept all cors connections > "CORS_ALLOW_ALL_ORIGINS = True"). I made a simple react component for the list on React Native (again lot of simple boilerplate stuff). I only tested in web, in case that was wondered.

> DRF commands: 

python -m venv env

env\Scripts\activate

cd backend

python manage.py runserver


> RN commands (maybe you can skip 1-4?):

npm install -g expo-cli

frontend cmd > expo start

npm install axios @react-navigation/native @react-navigation/stack

expo install react-native-screens react-native-safe-area-context

npx expo install react-native-web react-dom @expo/webpack-config

npx expo start

w
