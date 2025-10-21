# Práctica 2: Ontologías - AIF 2025/26

## Descripción
Práctica de Fundamentos de Inteligencia Artificial sobre edición de ontologías y consultas SPARQL.

## Estructura del Proyecto

```
Practica2/
├── README.md                          # Este archivo
├── informe_practica2.md              # Plantilla para el informe
├── ontology/                          # Archivos de ontología modificados
├── screenshots/                       # Capturas de pantalla de WebProtégé
├── sparql_queries/                    # Consultas SPARQL
│   ├── query1_artists.sparql         # Query 1: Artistas DBpedia
│   ├── query2_persons_height.sparql  # Query 2: Personas por altura
│   └── query3_persons_clubs.sparql   # Query 3: Personas por altura/peso y clubes
└── allergens_list.md                 # Lista de 10 alérgenos seleccionados
```

## Tareas

### 3.2.1. Edición de Ontología OFFF

**WebProtégé:** https://webprotege.stanford.edu/

1. ✅ Seleccionar 10 alérgenos de: https://en.wikipedia.org/wiki/List_of_allergens
2. ✅ Crear subclases de Allergens en la ontología OFFF
3. ✅ Crear clase "Allergy" en Health_Outcomes
4. ✅ Definir relaciones: Allergy is caused by allergens
5. ✅ Crear clase "Inflammation" en Health_Outcomes
6. ✅ Definir relaciones: heart disease, hypertension, obesity, type II diabetes caused by Inflammation
7. ✅ Crear individuo "My fish sandwich" (Fish Sandwich class)
   - Data property: contains gluten
   - Data property: has allergens as Peanut Oil

**IMPORTANTE:** Todas las capturas deben mostrar tu username de WebProtégé

### 3.2.2. Consultas SPARQL

#### Query 1: Artistas en DBpedia
- **Endpoint:** https://dbpedia.org/sparql/
- **Objetivo:** 10 artistas cuyos nombres empiezan con "Mado"

#### Query 2: Personas por altura
- **Endpoint:** https://dbpedia.org/snorql/
- **Objetivo:** 10 personas con altura entre 1.8-2.3m, nacidas después de 1980
- **Ordenar por:** Fecha de nacimiento

#### Query 3: Personas por altura/peso y clubes
- **Endpoint:** https://dbpedia.org/snorql/
- **Objetivo:** Personas con altura ≥2.10m O peso ≥95kg
- **Mostrar:** Número de clubes asociados
- **Agrupar por:** Persona
- **Ordenar por:** Número de clubes (ascendente)
- **Límite:** Top 7 resultados

## Entregables

1. **Informe PDF/Word** con:
   - Portada (título, autores, grupo, fecha)
   - Explicaciones de modificaciones ontología
   - Capturas de pantalla (con username visible)
   - Queries SPARQL con resultados y explicaciones

2. **Archivo de ontología modificado** (.owl o formato WebProtégé)

## Fecha de Entrega
**29 de Octubre de 2025, 23:59**

## Notas Importantes
- Trabajo en grupos de máximo 3 personas
- La copia total o parcial resultará en calificación de 0
- Posible defensa presencial si hay dudas
