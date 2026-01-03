/**
 * Lógica Frontend de Agro-Solver
 * Maneja la comunicación con el backend.
 */

document.addEventListener('DOMContentLoaded', () => {
    // Execute check
    // Connectivity check removed for UI clean up
    console.log('App initialized');

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
