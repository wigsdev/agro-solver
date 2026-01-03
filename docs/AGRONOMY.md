# Documentación Agronómica 🌽

## Fórmulas de Densidad de Siembra

Este módulo calcula la población estimada de plantas por hectárea basándose en la disposición geométrica de la siembra.

### 1. Sistema Marco Real / Cuadro / Rectángulo
Es el sistema más común. Las plantas se alinean en filas y columnas formando ángulos de 90°.

$$
Población = \frac{10,000}{D_s \times D_p}
$$

Donde:
*   $D_s$: Distancia entre surcos/hileras (metros).
*   $D_p$: Distancia entre plantas (metros).

### 2. Sistema Tresbolillo (Triangular)
Las plantas de una hilera se siembran en el punto medio de las plantas de la hilera adyacente, formando triángulos equiláteros. Esto maximiza el uso del espacio y la luz.

**Eficiencia Geométrica**: $\sin(60°) \approx 0.866$

$$
Población = \frac{10,000}{D_s \times D_p \times 0.866025}
$$

Este sistema permite aproximadamente un **15.47% más de plantas** por unidad de área comparado con el sistema cuadrado, manteniendo la misma distancia entre plantas vecinas.
