/**
 * Agro-Solver Frontend Logic
 * Handles communication with the backend.
 */

document.addEventListener('DOMContentLoaded', () => {
    const statusDiv = document.getElementById('status-display');

    // Function to check API health
    const checkConnectivity = async () => {
        try {
            console.log(`Attempting connection to: ${CONFIG.API_URL}`);

            const response = await fetch(`${CONFIG.API_URL}/`);

            if (!response.ok) {
                throw new Error(`HTTP Error! Status: ${response.status}`);
            }

            const data = await response.json();

            // Success State
            statusDiv.textContent = data.message;
            statusDiv.className = 'status-success';
            console.log('Backend response:', data);

        } catch (error) {
            // Error State
            statusDiv.textContent = `Error de conexión: ${error.message}`;
            statusDiv.className = 'status-error';
            console.error('Connection failed:', error);
        }
    };

    // Execute check
    checkConnectivity();
});
