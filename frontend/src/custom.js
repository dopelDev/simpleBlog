const baseUrl = 'http://localhost:8181/api/v1/';

async function fetchApi(endpoint, options = {}) {
    const url = `${baseUrl}${endpoint}`; // Usar template string con acento grave

    try {
        const response = await fetch(url, options);
        if (!response.ok) {
            throw new Error(`Error ${response.status}`); // Usar template string para el mensaje de error
        }
        return await response.json();
    } catch (error) {
        console.error('Error:', error);
        throw error;
    }
}

export { fetchApi };

