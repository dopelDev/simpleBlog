const baseUrl = 'http://localhost:8181/api/v1/';

async function fetchApi(endpoint, options = {}) {
    const url = `${baseUrl}${endpoint}`;

    // Opciones por defecto están marcadas con *
    const defaultOptions = {
        method: 'GET', // *GET, POST, PUT, DELETE, etc.
        mode: 'cors', // no-cors, *cors, same-origin
        cache: 'no-cache', // *default, no-cache, reload, force-cache, only-if-cached
        credentials: 'same-origin', // include, *same-origin, omit
        headers: {
            'Content-Type': 'application/json',
            // 'Authorization': 'Bearer YOUR_JWT_TOKEN_HERE', // Si estás utilizando JWT, aquí puedes pasar el token
            // Asegúrate de reemplazar 'YOUR_JWT_TOKEN_HERE' con tu token real
        },
        redirect: 'follow', // manual, *follow, error
        referrerPolicy: 'no-referrer', // no-referrer, *no-referrer-when-downgrade, origin, origin-when-cross-origin, same-origin, strict-origin, strict-origin-when-cross-origin, unsafe-url
        ...options // Extiende/reescribe con cualquier opción adicional que pases
    };

    try {
        const response = await fetch(url, defaultOptions);
        if (!response.ok) {
            throw new Error(`Error ${response.status}`);
        }
        return await response.json();
    } catch (error) {
        console.error('Error:', error);
        throw error;
    }
}
export { fetchApi };
