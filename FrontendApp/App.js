import React from 'react';
import { StyleSheet, View } from 'react-native';
import AutomobileView from './View/AutomobileView';

export default function App() {
  return (
    <View style={styles.container}>
      <AutomobileView />
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#fff',
  },
});
