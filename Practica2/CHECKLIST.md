# 🎯 Práctica 2: Ontologías - Guía Rápida

**Fecha límite:** 29 Octubre 2025, 23:59  
**Username WebProtégé:** __________ (¡Anótalo aquí!)

---

## 📋 CHECKLIST RÁPIDO

### PARTE 1: WebProtégé (Días 1-4)

- [ ] **Preparación:**
  - [ ] Leer publicación OFFF: https://bmcmedinformdecismak.biomedcentral.com/articles/10.1186/s12911-021-01636-1
  - [ ] Descargar offf.owl: https://github.com/UTHealth-Ontology/OFFF/
  - [ ] ⚠️ **ELIMINAR línea** `Import(<http://www.w3.org/2004/02/skos/core>)` del archivo
  - [ ] Crear cuenta en https://webprotege.stanford.edu/
  - [ ] Importar offf.owl como nuevo proyecto

- [ ] **Tarea 1: Añadir 10 Alérgenos**
  - [ ] Seleccionar 10 de `allergens_list.md`
  - [ ] Crear subclases en `Allergens`
  - [ ] 📸 Captura: Jerarquía + username visible

- [ ] **Tarea 2: Clase "Allergy"**
  - [ ] Crear subclase en `Health_Outcomes`
  - [ ] Añadir 10 relaciones `causedBy` (una por alérgeno)
  - [ ] 📸 Captura: Clase + relaciones + Entity Graph + username

- [ ] **Tarea 3: Clase "Inflammation"**
  - [ ] Crear subclase en `Health_Outcomes`
  - [ ] Añadir 4 relaciones causales con:
    - Heart_Disease
    - Hypertension
    - Obesity
    - Type_II_Diabetes
  - [ ] 📸 Captura: Clase + relaciones + Entity Graph + username

- [ ] **Tarea 4: Individuo "My fish sandwich"**
  - [ ] Crear instancia de `Fish_Sandwich`
  - [ ] Añadir data properties:
    - `containsGluten`: true
    - `hasAllergen`: "Peanut Oil"
  - [ ] 📸 Captura: Individuo + propiedades + username

- [ ] **Exportar ontología:** Guardar en `ontology/offf_modified.owl`

---

### PARTE 2: SPARQL (Día 5)

- [ ] **Query 1:** Artistas que empiezan con "Mado"
  - [ ] Ejecutar en https://dbpedia.org/sparql/
  - [ ] Usar código de `sparql_queries/query1_artists.sparql`
  - [ ] 📸 Captura de resultados
  - [ ] Copiar resultados a tabla

- [ ] **Query 2:** Personas altura 1.8-2.3m nacidas >1980
  - [ ] Ejecutar en https://dbpedia.org/snorql/
  - [ ] Usar código de `sparql_queries/query2_persons_height.sparql`
  - [ ] 📸 Captura de resultados
  - [ ] Copiar resultados a tabla

- [ ] **Query 3:** Personas altura/peso y clubes
  - [ ] Ejecutar en https://dbpedia.org/snorql/
  - [ ] Usar código de `sparql_queries/query3_persons_clubs.sparql`
  - [ ] 📸 Captura de resultados
  - [ ] Copiar resultados a tabla

---

### PARTE 3: Informe (Días 6-7)

- [ ] **Completar `informe_practica2.md`:**
  - [ ] Portada (nombres, grupo, fecha)
  - [ ] Sección 2.1: Lista y justificación de 10 alérgenos
  - [ ] Sección 2.2: Explicación + capturas de Allergens
  - [ ] Sección 2.3: Explicación + capturas de Allergy
  - [ ] Sección 2.4: Explicación + capturas de Inflammation
  - [ ] Sección 2.5: Explicación + capturas de "My fish sandwich"
  - [ ] Sección 3.1: Query 1 (código + tabla + captura + explicación)
  - [ ] Sección 3.2: Query 2 (código + tabla + captura + explicación)
  - [ ] Sección 3.3: Query 3 (código + tabla + captura + explicación)
  - [ ] Conclusiones
  - [ ] Referencias

- [ ] **Convertir a PDF**
- [ ] **Verificar que username aparece en TODAS las capturas**

---

### PARTE 4: Entrega (Día 8)

- [ ] Informe PDF completo
- [ ] Archivo ontología modificado (.owl)
- [ ] Entregar antes de las 23:59 del 29 de Octubre

---

## 📁 Archivos en tu proyecto:

```
Practica2/
├── CHECKLIST.md                    ← Este archivo (úsalo como guía)
├── allergens_list.md               ← Lista de alérgenos sugeridos
├── informe_practica2.md            ← Plantilla del informe (complétala)
├── sparql_queries/                 ← Queries listas para copiar
│   ├── query1_artists.sparql
│   ├── query2_persons_height.sparql
│   └── query3_persons_clubs.sparql
├── screenshots/                    ← Guarda aquí tus capturas
└── ontology/                       ← Guarda aquí offf.owl y offf_modified.owl
```

---

## ⚠️ RECORDATORIOS CRÍTICOS:

1. **USERNAME VISIBLE** en todas las capturas de WebProtégé
2. **ELIMINAR línea Import** antes de importar offf.owl
3. **Trabajo ORIGINAL** - no copiar de otros grupos
4. **Fecha límite:** 29 Octubre 2025, 23:59

---

## 🆘 Ayuda rápida:

- **Tutorial WebProtégé detallado:** Consulta con tu profesor o busca en YouTube "WebProtégé tutorial"
- **Queries SPARQL no funcionan:** Ajusta filtros (años, alturas, propiedades)
- **No encuentras una clase:** Usa la búsqueda en WebProtégé
- **Dudas técnicas:** Consulta la publicación OFFF o pregunta al profesor

---

**¡Éxito con tu práctica!** 🚀
