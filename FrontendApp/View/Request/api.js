import axios from 'axios';

const API_URL = 'localhost:5000'; // Remplacez par l'URL de votre API Flask

export const getAutomobiles = async () => {
  try {
    const response = await axios.get(`${API_URL}/automobiles`);
    return response.data;
  } catch (error) {
    console.error('Erreur lors de la récupération des automobiles:', error);
    throw error;
  }
};
