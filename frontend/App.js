import React from 'react';
import { NavigationContainer } from '@react-navigation/native';
import { createStackNavigator } from '@react-navigation/stack';
import FGFPostList from './components/FGFPostList';

const Stack = createStackNavigator();

export default function App() {
  return (
    <NavigationContainer>
      <Stack.Navigator>
        {/* Holy shit this is so much easier than it was in Jetpack */}
        <Stack.Screen
          name="FGFPosts"
          component={FGFPostList}
          options={{ title: 'FGF Posts' }}
        />
      </Stack.Navigator>
    </NavigationContainer>
  );
}