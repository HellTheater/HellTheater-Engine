#!/bin/bash

# -----------------------------------------------------------------------------
# MANIFIESTO DE EJECUCIÓN PARA "HELL theater"
# -----------------------------------------------------------------------------
# Este guion impone una disciplina de hierro. Falla al primer signo de debilidad.
# 'set -e' aborta el script si cualquier comando falla.
# 'set -o pipefail' asegura que un fallo en un pipeline (ej: cmd1 | cmd2) se detecte.
# -----------------------------------------------------------------------------
set -e
set -o pipefail

# -----------------------------------------------------------------------------
# PRELUDIO: LA PUESTA EN ESCENA
# Prepara el entorno de forma determinista y limpia. 'npm ci' es superior a
# 'install' para CI/CD porque usa el package-lock.json para una instalación
# exacta y reproducible. Es el equivalente a construir el escenario siempre
# con los mismos planos.
# -----------------------------------------------------------------------------
echo "==> PRELUDIO: Construyendo un escenario idéntico..."
npm ci

# -----------------------------------------------------------------------------
# ACTO I: LA PURGA ESTILÍSTICA (LINTING)
# Antes de juzgar la lógica, juzgamos la forma. El código debe adherirse a un
# estándar estético y estructural. El linting no es sobre preferencia, es
# sobre disciplina colectiva y la eliminación de errores triviales.
# -----------------------------------------------------------------------------
echo "==> ACTO I: Imponiendo la disciplina estilística (Linting)..."
npm run lint

# -----------------------------------------------------------------------------
# ACTO II: LA PRUEBA DE FUEGO (TESTING)
# El corazón del ritual. Aquí, las promesas del código se enfrentan a la
# realidad. Se ejecutan pruebas unitarias, de integración y cualquier otra
# validación. Incluimos '--coverage' para medir qué porcentaje del código
# se atrevió a pasar por el fuego. Una cobertura baja es una sombra de duda.
# -----------------------------------------------------------------------------
echo "==> ACTO II: Sometiendo el código a la prueba de fuego (Tests)..."
npm test -- --coverage

# -----------------------------------------------------------------------------
# ACTO III: EL ENSAMBLAJE FINAL (BUILD)
# Si el código sobrevive a las pruebas, se transforma. De un conjunto de
# archivos de desarrollo, se compila y optimiza en su forma final, lista para
# la producción. Cualquier error aquí significa un defecto en la transmutación.
# -----------------------------------------------------------------------------
echo "==> ACTO III: Forjando el artefacto de producción (Build)..."
npm run build

# -----------------------------------------------------------------------------
# (OPCIONAL) ACTO IV: EL VEREDICTO DE SEGURIDAD (AUDIT)
# El código no existe en el vacío. Depende de otros. Este acto examina la
# cadena de suministro, buscando vulnerabilidades conocidas en las dependencias.
# Es un acto de desconfianza necesaria en un mundo imperfecto.
# -----------------------------------------------------------------------------
echo "==> ACTO IV: Auditando la cadena de suministro en busca de traiciones (Security)..."
npm audit --production

# -----------------------------------------------------------------------------
# FINALE: LA OBRA HA SIDO VALIDADA
# Si el script llega a este punto sin ser abortado, el commit es digno.
# Ha pasado por cada filtro y ha demostrado su valía.
# -----------------------------------------------------------------------------
echo "******************************************************"
echo "==> FINALE: 'HELL theater' ha superado el manifiesto."
echo "******************************************************"