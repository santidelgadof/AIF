# Fundamentos de Inteligencia Artificial
## Práctica 2: Ontologías
### Master en Inteligencia Artificial 2025-26

---

**Autores:**
- Santiago Delgado Ferreiro
- David Carballo Rodríguez

**Grupo de Prácticas:** [Número de grupo]

**Fecha:** [DD/MM/2025]

---

## Índice

1. [Introducción](#introducción)
2. [Edición de Ontología OFFF](#edición-de-ontología-offf)
   - 2.1. [Selección de Alérgenos](#21-selección-de-alérgenos)
   - 2.2. [Creación de Subclases de Allergens](#22-creación-de-subclases-de-allergens)
   - 2.3. [Clase Allergy en Health_Outcomes](#23-clase-allergy-en-health_outcomes)
   - 2.4. [Clase Inflammation en Health_Outcomes](#24-clase-inflammation-en-health_outcomes)
   - 2.5. [Individuo "My fish sandwich"](#25-individuo-my-fish-sandwich)
3. [Consultas SPARQL](#consultas-sparql)
   - 3.1. [Query 1: Artistas en DBpedia](#31-query-1-artistas-en-dbpedia)
   - 3.2. [Query 2: Personas por Altura](#32-query-2-personas-por-altura)
   - 3.3. [Query 3: Personas por Altura/Peso y Clubes](#33-query-3-personas-por-alturapeso-y-clubes)
4. [Conclusiones](#conclusiones)
5. [Referencias](#referencias)

---

## 1. Introducción

[Breve introducción sobre ontologías, su importancia en IA y los objetivos de esta práctica]

---

## 2. Edición de Ontología OFFF

### 2.1. Selección de Alérgenos

Para esta práctica se han seleccionado los siguientes 10 alérgenos de la lista de Wikipedia (https://en.wikipedia.org/wiki/List_of_allergens):

1. **Peanut** (Cacahuete) - [Justificación]
2. **Tree Nuts** (Frutos secos) - [Justificación]
3. **Milk** (Leche) - [Justificación]
4. **Egg** (Huevo) - [Justificación]
5. **Fish** (Pescado) - [Justificación]
6. **Shellfish** (Mariscos) - [Justificación]
7. **Soy** (Soja) - [Justificación]
8. **Wheat** (Trigo) - [Justificación]
9. **Sesame** (Sésamo) - [Justificación]
10. **Celery** (Apio) - [Justificación]

**Criterios de selección:** [Explicar por qué se seleccionaron estos alérgenos]

---

### 2.2. Creación de Subclases de Allergens

**Descripción de la modificación:**

[Explicar el proceso de creación de las 10 subclases bajo la clase Allergens en WebProtégé]

**Capturas de pantalla:**

![Jerarquía de Allergens](screenshots/allergens_hierarchy.png)
*Figura 1: Jerarquía de clases mostrando las nuevas subclases de Allergens*

![Descripción de clases](screenshots/allergens_description.png)
*Figura 2: Descripción de las clases de alérgenos creadas*

**IMPORTANTE:** Verificar que el username de WebProtégé sea visible en todas las capturas.

**Explicación técnica:**
- [Descripción del proceso]
- [Propiedades añadidas]
- [Relaciones establecidas]

---

### 2.3. Clase Allergy en Health_Outcomes

**Descripción de la modificación:**

[Explicar cómo se creó la clase Allergy como subclase de Health_Outcomes]

**Relación "is caused by":**

Se ha establecido que la clase Allergy es causada por los siguientes alérgenos:
- [Lista de alérgenos y cómo se estableció la relación]

**Capturas de pantalla:**

![Clase Allergy](screenshots/allergy_class.png)
*Figura 3: Creación de la clase Allergy en Health_Outcomes*

![Relaciones Allergy](screenshots/allergy_causedby.png)
*Figura 4: Relaciones "is caused by" de Allergy con los alérgenos*

![Entity Graph Allergy](screenshots/allergy_entity_graph.png)
*Figura 5: Grafo de entidades mostrando las relaciones de Allergy*

**Explicación técnica:**
- [Proceso de creación]
- [Tipo de propiedad utilizada]
- [Lógica de la relación]

---

### 2.4. Clase Inflammation en Health_Outcomes

**Descripción de la modificación:**

[Explicar cómo se creó la clase Inflammation como subclase de Health_Outcomes]

**Relación "causes":**

Se ha establecido que Inflammation causa las siguientes condiciones:
1. Heart disease
2. Hypertension
3. Obesity
4. Type II diabetes

**Capturas de pantalla:**

![Clase Inflammation](screenshots/inflammation_class.png)
*Figura 6: Creación de la clase Inflammation en Health_Outcomes*

![Relaciones Inflammation](screenshots/inflammation_causes.png)
*Figura 7: Relaciones de causalidad de Inflammation*

![Entity Graph Inflammation](screenshots/inflammation_entity_graph.png)
*Figura 8: Grafo de entidades mostrando las relaciones de Inflammation*

**Explicación técnica:**
- [Proceso de creación]
- [Propiedad "causes" utilizada]
- [Lógica de las relaciones causales]

---

### 2.5. Individuo "My fish sandwich"

**Descripción de la modificación:**

[Explicar cómo se creó la instancia "My fish sandwich" de la clase Fish Sandwich]

**Data Properties:**
1. **Contains gluten:** [Valor asignado]
2. **Has allergens:** Peanut Oil

**Capturas de pantalla:**

![Individuo My fish sandwich](screenshots/my_fish_sandwich_individual.png)
*Figura 9: Creación del individuo "My fish sandwich"*

![Data Properties](screenshots/my_fish_sandwich_properties.png)
*Figura 10: Data properties del individuo "My fish sandwich"*

**Explicación técnica:**
- [Proceso de creación de la instancia]
- [Cómo se asignaron las data properties]
- [Relación con la clase Fish Sandwich]

---

## 3. Consultas SPARQL

### 3.1. Query 1: Artistas en DBpedia

**Objetivo:** Obtener 10 nombres de artistas que empiezan con "Mado" usando DBpedia.

**Endpoint:** https://dbpedia.org/sparql/ (http://dbpedia.org)

**Consulta SPARQL:**

```sparql
PREFIX dbo: <http://dbpedia.org/ontology/>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

SELECT DISTINCT ?artist ?name
WHERE {
  ?artist a dbo:Artist .
  ?artist rdfs:label ?name .
  FILTER (lang(?name) = 'en')
  FILTER (STRSTARTS(?name, "Mado"))
}
LIMIT 10
```

**Explicación de la lógica:**

1. **PREFIX declarations:** Se definen los prefijos para simplificar la consulta
   - `dbo:` para la ontología de DBpedia
   - `rdfs:` para el vocabulario RDF Schema

2. **SELECT DISTINCT:** Selecciona resultados únicos para evitar duplicados

3. **?artist a dbo:Artist:** Filtra solo entidades que son de tipo Artist

4. **?artist rdfs:label ?name:** Obtiene la etiqueta (nombre) del artista

5. **FILTER (lang(?name) = 'en'):** Filtra solo nombres en inglés

6. **FILTER (STRSTARTS(?name, "Mado")):** Filtra nombres que empiezan con "Mado"

7. **LIMIT 10:** Limita los resultados a 10 artistas

**Resultados:**

![Resultados Query 1](screenshots/sparql_query1_results.png)
*Figura 11: Resultados de la consulta SPARQL para artistas*

| Artist URI | Name |
|------------|------|
| [URI 1]    | [Nombre 1] |
| [URI 2]    | [Nombre 2] |
| ...        | ... |

[Incluir tabla completa con los 10 resultados]

**Análisis de resultados:**
[Comentar los resultados obtenidos]

---

### 3.2. Query 2: Personas por Altura

**Objetivo:** Obtener las primeras 10 personas con altura entre 1.8 y 2.3 metros, nacidas después de 1980, ordenadas por fecha de nacimiento.

**Endpoint:** https://dbpedia.org/snorql/

**Consulta SPARQL:**

```sparql
PREFIX dbo: <http://dbpedia.org/ontology/>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

SELECT DISTINCT ?person ?name ?height ?birthDate
WHERE {
  ?person a dbo:Person .
  ?person rdfs:label ?name .
  ?person dbo:height ?height .
  ?person dbo:birthDate ?birthDate .
  
  FILTER (lang(?name) = 'en')
  FILTER (?height >= 1.8 && ?height <= 2.3)
  FILTER (YEAR(?birthDate) > 1980)
}
ORDER BY ?birthDate
LIMIT 10
```

**Explicación de la lógica:**

1. **Selección de variables:** Se seleccionan persona, nombre, altura y fecha de nacimiento

2. **?person a dbo:Person:** Filtra solo entidades de tipo Person

3. **dbo:height y dbo:birthDate:** Obtiene las propiedades de altura y fecha de nacimiento

4. **FILTER (?height >= 1.8 && ?height <= 2.3):** Filtra alturas en el rango especificado (en metros)

5. **FILTER (YEAR(?birthDate) > 1980):** Filtra personas nacidas después del año 1980

6. **ORDER BY ?birthDate:** Ordena los resultados por fecha de nacimiento en orden ascendente

7. **LIMIT 10:** Limita los resultados a 10 personas

**Resultados:**

![Resultados Query 2](screenshots/sparql_query2_results.png)
*Figura 12: Resultados de la consulta SPARQL para personas por altura*

| Person URI | Name | Height (m) | Birth Date |
|------------|------|------------|------------|
| [URI 1]    | [Nombre 1] | [Altura 1] | [Fecha 1] |
| [URI 2]    | [Nombre 2] | [Altura 2] | [Fecha 2] |
| ...        | ...  | ...        | ...        |

[Incluir tabla completa con los 10 resultados ordenados por fecha]

**Análisis de resultados:**
[Comentar los resultados obtenidos y el orden cronológico]

---

### 3.3. Query 3: Personas por Altura/Peso y Clubes

**Objetivo:** Obtener personas con altura ≥2.10m O peso ≥95kg, mostrando el número de clubes asociados, agrupadas por persona, ordenadas por número de clubes ascendente, limitado a 7 resultados.

**Endpoint:** https://dbpedia.org/snorql/

**Consulta SPARQL:**

```sparql
PREFIX dbo: <http://dbpedia.org/ontology/>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

SELECT ?person ?name (COUNT(?club) as ?numberOfClubs)
WHERE {
  ?person a dbo:Person .
  ?person rdfs:label ?name .
  OPTIONAL { ?person dbo:team ?club . }
  
  {
    { ?person dbo:height ?height . FILTER (?height >= 2.10) }
    UNION
    { ?person dbo:weight ?weight . FILTER (?weight >= 95000) }
  }
  
  FILTER (lang(?name) = 'en')
}
GROUP BY ?person ?name
ORDER BY ASC(?numberOfClubs)
LIMIT 7
```

**Explicación de la lógica:**

1. **COUNT(?club) as ?numberOfClubs:** Cuenta el número de clubes asociados a cada persona

2. **OPTIONAL { ?person dbo:team ?club }:** Obtiene los clubes de forma opcional (algunas personas pueden no tener clubes)

3. **UNION entre altura y peso:** Permite seleccionar personas que cumplan CUALQUIERA de las dos condiciones:
   - Altura >= 2.10 metros
   - Peso >= 95000 gramos (95 kg, ya que DBpedia usa gramos)

4. **GROUP BY ?person ?name:** Agrupa los resultados por persona para contar sus clubes

5. **ORDER BY ASC(?numberOfClubs):** Ordena por número de clubes en orden ascendente

6. **LIMIT 7:** Limita los resultados a las primeras 7 personas

**Resultados:**

![Resultados Query 3](screenshots/sparql_query3_results.png)
*Figura 13: Resultados de la consulta SPARQL para personas por altura/peso*

| Person URI | Name | Number of Clubs |
|------------|------|-----------------|
| [URI 1]    | [Nombre 1] | [Num 1] |
| [URI 2]    | [Nombre 2] | [Num 2] |
| ...        | ...  | ...             |

[Incluir tabla completa con los 7 resultados ordenados por número de clubes]

**Análisis de resultados:**
[Comentar los resultados, relación entre altura/peso y número de clubes, etc.]

---

## 4. Conclusiones

[Resumir los aprendizajes de la práctica]

- **Sobre ontologías:** [Qué se aprendió sobre estructura, clases, propiedades, instancias]
- **Sobre WebProtégé:** [Experiencia con la herramienta]
- **Sobre SPARQL:** [Qué se aprendió sobre consultas, filtros, agregaciones]
- **Dificultades encontradas:** [Problemas y cómo se resolvieron]
- **Aplicaciones prácticas:** [Cómo se pueden aplicar estos conocimientos]

---

## 5. Referencias

1. Wikipedia - List of Allergens: https://en.wikipedia.org/wiki/List_of_allergens
2. WebProtégé: https://webprotege.stanford.edu/
3. DBpedia SPARQL Endpoint: https://dbpedia.org/sparql/
4. DBpedia Snorql: https://dbpedia.org/snorql/
5. SPARQL 1.1 Query Language: https://www.w3.org/TR/sparql11-query/
6. Ontology Food Framework: [Referencia a OFFF]

---

## Anexos

### Anexo A: Archivo de Ontología Modificado

[Incluir referencia al archivo .owl entregado]

### Anexo B: Capturas de Pantalla Adicionales

[Si es necesario, incluir capturas adicionales]

---

**Nota:** Todas las capturas de pantalla incluyen el username de WebProtégé para validar la autoría del trabajo.
