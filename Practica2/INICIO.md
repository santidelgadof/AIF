# 🎯 Guía Rápida - Práctica 2 Ontologías

## Links importantes:

### Lectura obligatoria:
- **Publicación OFFF:** https://bmcmedinformdecismak.biomedcentral.com/articles/10.1186/s12911-021-01636-1

### Descargas:
- **Ontología OFFF:** https://github.com/UTHealth-Ontology/OFFF/ (descargar `offf.owl`)

### Herramientas:
- **WebProtégé:** https://webprotege.stanford.edu/
- **DBpedia SPARQL:** https://dbpedia.org/sparql/
- **DBpedia Snorql:** https://dbpedia.org/snorql/

---

## ⚠️ Paso crítico ANTES de importar:

Abre `offf.owl` con editor de texto y **ELIMINA esta línea:**
```
Import(<http://www.w3.org/2004/02/skos/core>)
```

---

## 📋 Resumen de tareas:

1. **WebProtégé:** Editar ontología OFFF
   - 10 subclases de Allergens
   - Clase Allergy con relaciones causedBy
   - Clase Inflammation con relaciones causales
   - Individuo "My fish sandwich" con 2 data properties

2. **SPARQL:** Ejecutar 3 consultas en DBpedia
   - Query 1: Artistas "Mado*"
   - Query 2: Personas por altura
   - Query 3: Personas por altura/peso y clubes

3. **Informe:** Completar plantilla con explicaciones y capturas
   - Portada + explicaciones + capturas + queries + conclusiones
   - Convertir a PDF

4. **Entregar:** PDF + ontología modificada (.owl)

---

**Fecha límite:** 29 Octubre 2025, 23:59

**⚠️ IMPORTANTE:** Tu username de WebProtégé debe aparecer en TODAS las capturas.
