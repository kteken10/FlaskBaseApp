import React, { useEffect, useState } from 'react';
import { StyleSheet, Text, View ,Image} from 'react-native';
import axios from 'axios';

const AutomobileView = () => {
  const [automobiles, setAutomobiles] = useState([]);

  useEffect(() => {
    fetchAutomobiles();
  }, []);

  const fetchAutomobiles = async () => {
    try {
      const response = await axios.get('http://192.168.178.175:5000/automobiles'); // Remplacez par l'URL réelle de votre API Flask
      setAutomobiles(response.data);
    } catch (error) {
      console.error('Erreur lors de la récupération des automobiles:', error);
    }
  };

  return (
    <View style={styles.container}>
      <Text style={styles.title}>Informations sur l'automobile</Text>
      {automobiles.map((automobile) => (
        <View key={automobile.id}>
          <Text>Marque: {automobile.marque}</Text>
          <Text>Prix: {automobile.prix}</Text>
          <Text>Duree: {automobile.duree}</Text>
          <Image source={{ uri: automobile.image }} style={styles.image} /> 
          <View style={styles.separator} />
        </View>
      ))}
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    padding: 16,
  },
  title: {
    fontSize: 20,
    fontWeight: 'bold',
    marginBottom: 16,
  },
  separator: {
    borderBottomWidth: 1,
    borderBottomColor: '#ccc',
    marginVertical: 16,
  },
  image: {
    width: 200,
    height: 200,
    resizeMode: 'contain',
    marginBottom: 16,
  }
  
});

export default AutomobileView;
