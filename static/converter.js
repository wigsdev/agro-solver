document.addEventListener('DOMContentLoaded', () => {
    // --- Data & Factors ---
    const factors = {
        area: {
            // Base unit: Square Meter (m²)
            'm2': 1,
            'ha': 10000,
            'acre': 4046.86,
            'mz': 7000,       // Manzana (Standard Approx)
            'tarea': 628.86   // Tarea (Dominicana/Centroamérica)
        },
        weight: {
            // Base unit: Kilogram (kg)
            'kg': 1,
            'lb': 0.453592,
            'qq': 45.36,      // Quintal (Standard)
            'ton': 1000
        }
    };

    // --- DOM Elements ---
    const tabButtons = document.querySelectorAll('.tab-btn');
    const inputAmount = document.getElementById('input-amount');
    const outputAmount = document.getElementById('output-amount');
    const selectFrom = document.getElementById('select-from');
    const selectTo = document.getElementById('select-to');

    let currentCategory = 'area'; // 'area' or 'weight'

    // --- Functions ---

    function populateSelects(category) {
        // Clear options
        selectFrom.innerHTML = '';
        selectTo.innerHTML = '';

        const units = Object.keys(factors[category]);
        const labels = {
            area: {
                'm2': 'Metros Cuadrados (m²)',
                'ha': 'Hectáreas (Ha)',
                'acre': 'Acres',
                'mz': 'Manzanas (Mz)',
                'tarea': 'Tareas'
            },
            weight: {
                'kg': 'Kilogramos (Kg)',
                'lb': 'Libras (Lb)',
                'qq': 'Quintales (qq)',
                'ton': 'Toneladas (t)'
            }
        };

        units.forEach(unit => {
            const optionFrom = new Option(labels[category][unit], unit);
            const optionTo = new Option(labels[category][unit], unit);
            selectFrom.add(optionFrom);
            selectTo.add(optionTo);
        });

        // Set defaults
        if (category === 'area') {
            selectFrom.value = 'ha';
            selectTo.value = 'acre';
        } else {
            selectFrom.value = 'kg';
            selectTo.value = 'lb';
        }

        convert();
    }

    function convert() {
        const val = parseFloat(inputAmount.value);
        if (isNaN(val)) {
            outputAmount.value = '';
            return;
        }

        const fromUnit = selectFrom.value;
        const toUnit = selectTo.value;
        const categoryFactors = factors[currentCategory];

        // 1. Convert to Base Unit
        const baseValue = val * categoryFactors[fromUnit];

        // 2. Convert to Target Unit
        const targetValue = baseValue / categoryFactors[toUnit];

        // Format Result (max 4 decimals, remove trailing zeros)
        outputAmount.value = parseFloat(targetValue.toFixed(4));
    }

    // --- Event Listeners ---

    // Tabs
    tabButtons.forEach(btn => {
        btn.addEventListener('click', () => {
            // UI Toggle
            tabButtons.forEach(b => b.classList.remove('active'));
            btn.classList.add('active');

            // Logic Switch
            currentCategory = btn.dataset.category;
            populateSelects(currentCategory);
        });
    });

    // Inputs
    inputAmount.addEventListener('input', convert);
    selectFrom.addEventListener('change', convert);
    selectTo.addEventListener('change', convert);

    // Init
    populateSelects('area');
});
