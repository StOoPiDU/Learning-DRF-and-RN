import React, { useState, useEffect } from 'react';
import { View, Text, FlatList, StyleSheet } from 'react-native';
import axios from 'axios';

const API_URL = 'http://127.0.0.1:8000/fgfposts/';

const FGFPostList = () => {
  const [fgfPosts, setPosts] = useState([]);

  useEffect(() => {
    fetchPosts();
  }, []);

  const fetchPosts = async () => {
    try {
      const response = await axios.get(API_URL);
      setPosts(response.data);
    } catch (error) {
      console.error('Error fetching DRF FGF posts:', error);
    }
  };

  const renderItem = ({ item }) => (
    <View style={styles.postItem}>
      <Text style={styles.title}>{item.title}</Text>
      <Text style={styles.author}>Author: {item.author}</Text>
      <a href="https://freegamefindings.ca"><Text>Reddit_id: https://redd.it/{item.reddit_id}</Text></a>
    </View>
  );

  return (
    <FlatList
      data={fgfPosts}
      renderItem={renderItem}
      keyExtractor={(item) => item.id.toString()}
    />
  );
};

const styles = StyleSheet.create({
  postItem: {
    padding: 15,
    borderBottomWidth: 1,
    borderBottomColor: '#ccc',
  },
  title: {
    fontSize: 18,
    fontWeight: 'bold',
  },
  author: {
    fontStyle: 'italic',
  },
});

export default FGFPostList;