# Guía Paso a Paso - Práctica 2: Ontologías

## 📋 Checklist General

- [ ] Registrarse en WebProtégé
- [ ] Acceder a la ontología OFFF
- [ ] Completar ediciones de ontología
- [ ] Ejecutar consultas SPARQL
- [ ] Tomar todas las capturas de pantalla
- [ ] Redactar informe
- [ ] Exportar archivo de ontología
- [ ] Revisar que el username sea visible en capturas
- [ ] Entregar antes del 29 de Octubre 2025

---

## 🔧 Parte 1: Edición de Ontología OFFF

### Paso 1: Acceso a WebProtégé

1. **Ir a:** https://webprotege.stanford.edu/
2. **Crear cuenta** o iniciar sesión
3. **Anotar tu username** (debe aparecer en todas las capturas)
4. **Buscar o abrir** la ontología OFFF (Food Ontology Framework)
   - Si no está disponible, consultar con el profesor cómo acceder

### Paso 2: Seleccionar 10 Alérgenos

1. **Visitar:** https://en.wikipedia.org/wiki/List_of_allergens
2. **Seleccionar 10 alérgenos** de la lista (ver sugerencias en `allergens_list.md`)
3. **Anotar los nombres** en inglés tal como aparecen en Wikipedia

**Alérgenos sugeridos:**
- Peanut
- Tree Nuts
- Milk
- Egg
- Fish
- Shellfish
- Soy
- Wheat
- Sesame
- Celery

### Paso 3: Crear Subclases de Allergens

1. **En WebProtégé:**
   - Navegar al panel de clases (Classes)
   - Buscar la clase "Allergens"
   - Hacer clic derecho → "Create subclass"
   
2. **Para cada uno de los 10 alérgenos:**
   - Crear una nueva subclase
   - Nombrarla según el alérgeno (ej: "Peanut", "Milk", etc.)
   - Agregar descripción si es necesario
   
3. **Tomar capturas de pantalla:**
   - [ ] Jerarquía de clases mostrando las 10 subclases
   - [ ] Vista de descripción de algunas clases
   - [ ] Entity graph (si está disponible)
   - ⚠️ **IMPORTANTE:** Username debe ser visible

### Paso 4: Crear Clase "Allergy" en Health_Outcomes

1. **Navegar a la clase "Health_Outcomes"**
2. **Crear subclase "Allergy":**
   - Clic derecho en "Health_Outcomes" → "Create subclass"
   - Nombrar: "Allergy"
   - Agregar descripción

3. **Definir relación "is caused by":**
   - Ir a la pestaña de propiedades (Properties)
   - Buscar o crear la propiedad "is caused by" o "causedBy"
   - Establecer que "Allergy" es causada por los 10 alérgenos creados
   
   **Opciones para definir la relación:**
   - Usar restricciones (Restrictions)
   - Establecer axiomas de clase
   - Formato típico: `Allergy SubClassOf causedBy some Peanut`

4. **Tomar capturas de pantalla:**
   - [ ] Creación de la clase Allergy
   - [ ] Relaciones definidas (causedBy)
   - [ ] Entity graph mostrando las relaciones
   - ⚠️ **Username visible**

### Paso 5: Crear Clase "Inflammation" en Health_Outcomes

1. **Navegar a la clase "Health_Outcomes"**
2. **Crear subclase "Inflammation":**
   - Clic derecho en "Health_Outcomes" → "Create subclass"
   - Nombrar: "Inflammation"

3. **Definir relación "causes":**
   - Buscar las clases existentes:
     - Heart disease
     - Hypertension
     - Obesity
     - Type II diabetes
   
   - Establecer que estas condiciones son causadas por Inflammation
   - Usar la propiedad "causes" o "causedBy" (inversa)
   - Formato típico: `HeartDisease SubClassOf causedBy some Inflammation`

4. **Tomar capturas de pantalla:**
   - [ ] Creación de la clase Inflammation
   - [ ] Relaciones con las 4 condiciones
   - [ ] Entity graph
   - ⚠️ **Username visible**

### Paso 6: Crear Individuo "My fish sandwich"

1. **Buscar la clase "Fish Sandwich"**
2. **Crear una nueva instancia (individual):**
   - Clic derecho en "Fish Sandwich" → "Create instance"
   - Nombrar: "My fish sandwich"

3. **Agregar Data Properties:**
   
   **Propiedad 1: Contains gluten**
   - Buscar o crear data property "containsGluten" o similar
   - Establecer valor: true o "yes"
   
   **Propiedad 2: Has allergens**
   - Buscar o crear data property "hasAllergen" o similar
   - Establecer valor: "Peanut Oil"
   
   **Nota:** Si las data properties no existen, puede que necesites crearlas primero:
   - Ir a Data Properties
   - Create new data property
   - Definir dominio (Fish Sandwich) y rango (boolean/string)

4. **Tomar capturas de pantalla:**
   - [ ] Creación del individuo
   - [ ] Data properties asignadas
   - [ ] Vista completa del individuo
   - ⚠️ **Username visible**

### ✅ Checklist Edición Ontología

- [ ] 10 subclases de Allergens creadas
- [ ] Clase Allergy creada en Health_Outcomes
- [ ] Relaciones causedBy para Allergy definidas
- [ ] Clase Inflammation creada en Health_Outcomes
- [ ] Relaciones causales para Inflammation definidas
- [ ] Individuo "My fish sandwich" creado
- [ ] Data properties del individuo asignadas
- [ ] Todas las capturas tomadas con username visible
- [ ] Exportar archivo de ontología (.owl o .zip)

---

## 🔍 Parte 2: Consultas SPARQL

### Query 1: Artistas que empiezan con "Mado"

**Endpoint:** https://dbpedia.org/sparql/

**Pasos:**
1. Ir a https://dbpedia.org/sparql/
2. Copiar la consulta de `sparql_queries/query1_artists.sparql`
3. Pegar en el editor (sin los comentarios #)
4. Hacer clic en "Run Query"
5. Revisar resultados

**Consulta:**
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

**Tareas:**
- [ ] Ejecutar query
- [ ] Capturar resultados (screenshot)
- [ ] Copiar resultados en tabla
- [ ] Explicar lógica en el informe

---

### Query 2: Personas por Altura

**Endpoint:** https://dbpedia.org/snorql/

**Pasos:**
1. Ir a https://dbpedia.org/snorql/
2. Copiar la consulta de `sparql_queries/query2_persons_height.sparql`
3. Pegar en el editor
4. Ejecutar
5. Si no hay resultados, ajustar filtros (ver notas en el archivo)

**Consulta:**
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

**Posibles ajustes si no hay resultados:**
- Probar con `dbp:height` en lugar de `dbo:height`
- Ajustar rango de altura
- Cambiar año de nacimiento

**Tareas:**
- [ ] Ejecutar query
- [ ] Capturar resultados
- [ ] Verificar orden por fecha
- [ ] Explicar lógica en el informe

---

### Query 3: Personas por Altura/Peso y Clubes

**Endpoint:** https://dbpedia.org/snorql/

**Pasos:**
1. Ir a https://dbpedia.org/snorql/
2. Copiar la consulta de `sparql_queries/query3_persons_clubs.sparql`
3. Pegar en el editor
4. Ejecutar
5. Verificar agrupación y orden

**Consulta:**
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

**Nota importante:**
- Peso en DBpedia suele estar en gramos (95000g = 95kg)
- Altura en metros (2.10 = 2.10m)

**Tareas:**
- [ ] Ejecutar query
- [ ] Capturar resultados
- [ ] Verificar agrupación por persona
- [ ] Verificar orden ascendente por clubes
- [ ] Explicar uso de UNION, GROUP BY, COUNT

---

## 📄 Parte 3: Redacción del Informe

### Estructura del Informe

Usar la plantilla en `informe_practica2.md` como base.

**Secciones obligatorias:**

1. **Portada**
   - Título completo
   - Nombres de autores
   - Grupo de prácticas
   - Fecha

2. **Edición de Ontología**
   - Para cada modificación:
     - Descripción del cambio
     - Capturas de pantalla (con username)
     - Explicación técnica
     - Justificación

3. **Consultas SPARQL**
   - Para cada query:
     - Código SPARQL
     - Resultados (tabla + screenshot)
     - Explicación línea por línea
     - Análisis de resultados

4. **Conclusiones**
   - Aprendizajes
   - Dificultades
   - Aplicaciones prácticas

### Checklist Informe

- [ ] Portada completa
- [ ] Índice
- [ ] Introducción
- [ ] Explicación de 10 alérgenos seleccionados
- [ ] Explicación de subclases de Allergens + capturas
- [ ] Explicación de clase Allergy + capturas
- [ ] Explicación de clase Inflammation + capturas
- [ ] Explicación de individuo "My fish sandwich" + capturas
- [ ] Query 1: código + resultados + explicación
- [ ] Query 2: código + resultados + explicación
- [ ] Query 3: código + resultados + explicación
- [ ] Conclusiones
- [ ] Referencias
- [ ] Todas las capturas muestran username
- [ ] Formato profesional
- [ ] Sin errores ortográficos

---

## 📦 Entrega Final

### Archivos a entregar:

1. **Informe en PDF**
   - Convertir `informe_practica2.md` a Word/PDF
   - Incluir todas las capturas
   - Verificar formato

2. **Archivo de Ontología**
   - Exportar desde WebProtégé
   - Formato .owl o .zip
   - Verificar que contenga todas las modificaciones

### Checklist Pre-Entrega

- [ ] Informe completo en PDF
- [ ] Archivo de ontología exportado
- [ ] Todas las capturas incluidas
- [ ] Username visible en todas las capturas
- [ ] Nombres de autores y grupo correctos
- [ ] Fecha correcta
- [ ] Referencias incluidas
- [ ] Sin plagio (trabajo original)
- [ ] Revisión ortográfica completa
- [ ] Tamaño de archivos adecuado

### Fecha límite: **29 de Octubre de 2025, 23:59**

---

## 💡 Consejos y Tips

### Para WebProtégé:

1. **Guarda frecuentemente** - WebProtégé guarda automáticamente pero verifica
2. **Exporta regularmente** - Descarga backups de tu ontología
3. **Toma capturas progresivas** - No esperes al final
4. **Verifica tu username** - Debe estar visible en cada captura
5. **Usa descripciones claras** - Ayuda en el informe

### Para SPARQL:

1. **Prueba queries simples primero** - Luego añade complejidad
2. **Usa LIMIT bajo al probar** - Evita sobrecargar el servidor
3. **Lee mensajes de error** - Dan pistas sobre qué ajustar
4. **Explora los datos** - Usa queries exploratorias primero
5. **Documenta cada ajuste** - Útil para el informe

### Para el Informe:

1. **Empieza temprano** - No dejes para el último día
2. **Sigue la plantilla** - Asegura que no falte nada
3. **Sé específico** - Explica cada paso técnico
4. **Usa imágenes claras** - Capturas legibles y completas
5. **Revisa antes de entregar** - Ortografía y coherencia

### Recursos Útiles:

- **SPARQL Tutorial:** https://www.w3.org/TR/sparql11-query/
- **DBpedia Documentation:** https://wiki.dbpedia.org/
- **WebProtégé User Guide:** https://protegewiki.stanford.edu/wiki/WebProtege
- **Ontology Best Practices:** https://www.w3.org/TR/owl2-primer/

---

## ⚠️ Advertencias Importantes

1. **NO COPIAR** de otros grupos - Calificación de 0
2. **VERIFICAR USERNAME** - Debe estar en todas las capturas
3. **EXPORTAR ONTOLOGÍA** - No olvides incluir el archivo
4. **DEADLINE ESTRICTO** - 29 Oct 2025, 23:59
5. **TRABAJO EN GRUPO** - Máximo 3 personas

---

## 📞 Si Tienes Problemas

- **No puedes acceder a OFFF:** Consulta con el profesor
- **WebProtégé no funciona:** Intenta en otro navegador
- **Queries SPARQL sin resultados:** Ajusta filtros y propiedades
- **Dudas técnicas:** Consulta documentación o pregunta al profesor

---

**¡Buena suerte con la práctica!** 🚀
