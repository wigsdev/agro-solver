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

    // Calculator Logic
    const form = document.getElementById('density-form');
    const resultDiv = document.getElementById('result-display');
    const densityValue = document.getElementById('density-value');
    const densityContext = document.getElementById('density-context');
    const calcBtn = document.getElementById('calc-btn');

    form.addEventListener('submit', async (e) => {
        e.preventDefault();

        // UI Loading State
        calcBtn.disabled = true;
        calcBtn.textContent = "Calculando...";
        resultDiv.style.display = 'none';

        const payload = {
            row_distance: parseFloat(document.getElementById('row_distance').value),
            plant_distance: parseFloat(document.getElementById('plant_distance').value),
            system: document.getElementById('system').value
        };

        try {
            const response = await fetch(`${CONFIG.API_URL}/api/density`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(payload)
            });

            if (!response.ok) {
                const err = await response.json();
                throw new Error(err.detail || 'Error en cálculo');
            }

            const data = await response.json();

            // UI Success State
            resultDiv.style.display = 'block';
            densityValue.textContent = `${data.plants_per_hectare.toLocaleString()} plantas/ha`;
            densityContext.textContent = `Sistema: ${data.system_used === 'triangular' ? 'Tresbolillo' : 'Cuadro'}`;
            densityValue.style.color = '#28a745';

        } catch (error) {
            // UI Error State
            resultDiv.style.display = 'block';
            densityValue.textContent = "Error";
            densityContext.textContent = error.message;
            densityValue.style.color = '#dc3545';
        } finally {
            calcBtn.disabled = false;
            calcBtn.textContent = "Calcular";
        }
    });
});
