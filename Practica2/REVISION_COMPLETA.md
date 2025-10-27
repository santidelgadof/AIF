# 📊 REVISIÓN COMPLETA - Práctica 2 Ontologías

**Fecha de revisión:** 27 de Octubre de 2025  
**Fecha límite:** 29 de Octubre de 2025, 23:59  
**Días restantes:** 2 días

---

## ✅ LO QUE ESTÁ COMPLETO

### 1. Estructura del Proyecto ✓
```
Practica2/
├── allergens_list.md          ✓
├── CHECKLIST.md               ✓
├── INICIO.md                  ✓
├── informe_practica2.md       ✓ (plantilla)
├── informe_practica2.tex      ✓ (NUEVO - documento LaTeX completo)
├── ontology/
│   └── offf.owl               ✓
├── screenshots/               ✓ (10 capturas)
│   ├── Allergens.png
│   ├── allergy.png
│   ├── inflammation_1.png
│   ├── inflammation_2.png
│   ├── inflammation_3.png
│   ├── inflammation_4.png
│   ├── My fish sandwich.png
│   ├── Query1.png
│   ├── Qiery2.png (typo en nombre)
│   └── Query3.png
└── sparql_queries/            ✓
    ├── query1_artists.sparql
    ├── query2_persons_height.sparql
    └── query3_persons_clubs.sparql
```

### 2. Trabajo en WebProtégé ✓
- [x] Cuenta creada (username: santi_david)
- [x] Ontología OFFF importada
- [x] 10 alérgenos añadidos como subclases de Allergens
- [x] Clase Allergy creada en Health_Outcomes
- [x] Clase Inflammation creada en Health_Outcomes
- [x] Individuo "My fish sandwich" creado
- [x] Capturas de pantalla tomadas (username visible)

### 3. Queries SPARQL ✓
- [x] Query 1 ejecutada (artistas "Mado*")
- [x] Query 2 ejecutada (personas por altura)
- [x] Query 3 ejecutada (personas altura/peso + clubes)
- [x] Capturas de resultados tomadas

### 4. Documento LaTeX ✓
- [x] Documento completo creado: `informe_practica2.tex`
- [x] Estructura profesional con todos los paquetes necesarios
- [x] Portada con datos de autores
- [x] Índice automático
- [x] Todas las secciones estructuradas
- [x] Código SPARQL formateado con syntax highlighting
- [x] Referencias incluidas
- [x] Anexos con lista de archivos

---

## ❌ LO QUE FALTA COMPLETAR

### 🔴 CRÍTICO (Obligatorio para entregar)

#### 1. **Exportar Ontología Modificada** ⚠️ URGENTE
- [ ] En WebProtégé: Download/Export → OWL/XML
- [ ] Guardar como: `ontology/offf_modified.owl`
- [ ] Verificar que contiene todas tus modificaciones
- **Sin este archivo, la práctica está INCOMPLETA**

#### 2. **Completar Resultados SPARQL en LaTeX** ⚠️ IMPORTANTE
El archivo `.tex` tiene varios `TODO` que debes completar:

**En Query 1 (línea ~485):**
```latex
% TODO: Completar con los resultados reales de la ejecución
\begin{table}[H]
    ...
    [Completar con datos reales] & Madonna \\
    [Completar con datos reales] & [Nombre 2] \\
    ...
```
**Acción:** Transcribir los 10 artistas de tu captura `Query1.png`

**En Query 2 (línea ~559):**
```latex
% TODO: Completar con datos reales
\begin{table}[H]
    ...
    [URI 1] & [Nombre 1] & [Altura 1] & [Fecha 1] \\
    ...
```
**Acción:** Transcribir las 10 personas de tu captura `Qiery2.png`

**En Query 3 (línea ~679):**
```latex
% TODO: Completar con datos reales
\begin{table}[H]
    ...
    [URI 1] & [Nombre 1] & [N1] \\
    ...
```
**Acción:** Transcribir las 7 personas de tu captura `Query3.png`

**Análisis de resultados (3 secciones):**
```latex
% TODO: Completar con análisis real
```
**Acción:** Escribir 2-3 párrafos analizando cada resultado

#### 3. **Datos Faltantes en LaTeX**
- [ ] Línea 73: `\textbf{Grupo de Prácticas:} [Completar número de grupo]`
- [ ] Línea 76: Logo universidad (opcional, puede comentarse si no tienes)

---

### 🟡 RECOMENDADO (Mejora la calidad)

#### 4. **Mejorar Análisis y Conclusiones**
Las secciones de análisis tienen placeholders que podrías expandir:

- Query 1 análisis (línea ~532): Añadir comentarios sobre los artistas encontrados
- Query 2 análisis (línea ~592): Comentar sobre la distribución de alturas/fechas
- Query 3 análisis (línea ~712): Analizar relación altura/peso vs. número de clubes

---

## 📝 PASOS PARA COMPLETAR (Orden sugerido)

### HOY (27 Oct) - 2 horas

#### Paso 1: Exportar Ontología (10 min) 🔴
1. Ir a WebProtégé
2. Abrir proyecto OFFF
3. File/Download → Export → OWL/XML
4. Guardar en `ontology/offf_modified.owl`
5. Verificar tamaño (debe ser mayor que offf.owl original)

#### Paso 2: Transcribir Resultados SPARQL (45 min) 🔴
1. Abrir `informe_practica2.tex` en editor
2. Buscar "TODO: Completar con datos reales"
3. Para cada query:
   - Abrir la captura correspondiente
   - Transcribir datos a la tabla LaTeX
   - Formato: `URI & Nombre & Datos \\`

**Ejemplo para Query 1:**
```latex
http://dbpedia.org/resource/Madonna & Madonna \\
http://dbpedia.org/resource/Mado_Robin & Mado Robin \\
```

#### Paso 3: Escribir Análisis (30 min) 🟡
Para cada query, escribir 2-3 párrafos respondiendo:
- ¿Qué patrones observas en los resultados?
- ¿Son los resultados esperados?
- ¿Qué demuestra técnicamente la query?

#### Paso 4: Completar Datos (5 min) 🔴
- Número de grupo
- Comentar línea del logo si no lo tienes:
  ```latex
  % \includegraphics[width=0.3\textwidth]{logo_universidad.png}\\
  ```

#### Paso 5: Compilar LaTeX (10 min)
1. Instalar LaTeX si no lo tienes:
   - Windows: MiKTeX o TeX Live
   - Online: Overleaf.com
2. Compilar: `pdflatex informe_practica2.tex` (2 veces)
3. Verificar que se genera `informe_practica2.pdf`
4. Revisar que las imágenes aparecen correctamente

---

### MAÑANA (28 Oct) - 1 hora

#### Paso 6: Revisión Final
- [ ] Leer el PDF completo
- [ ] Verificar que todas las imágenes se ven
- [ ] Revisar ortografía
- [ ] Comprobar que las tablas están completas
- [ ] Verificar que username aparece en capturas
- [ ] Comprobar que tienes `offf_modified.owl`

#### Paso 7: Preparar Entrega
1. Crear carpeta: `Practica2_Delgado_Carballo`
2. Incluir:
   - `informe_practica2.pdf`
   - `ontology/offf_modified.owl`
3. Comprimir en ZIP (si es necesario)
4. Subir a plataforma ANTES de las 23:59 del 29 Oct

---

## 🛠️ CÓMO COMPILAR EL DOCUMENTO LATEX

### Opción 1: Overleaf (Recomendado - Online, fácil)
1. Ir a: https://overleaf.com
2. New Project → Upload Project
3. Subir `informe_practica2.tex` y carpeta `screenshots/`
4. Click en "Recompile"
5. Descargar PDF

### Opción 2: LaTeX Local (Windows)
```powershell
# Instalar MiKTeX (solo primera vez)
# Descargar de: https://miktex.org/download

# Compilar documento (ejecutar 2 veces para índice)
cd "C:\Users\Usuario\Documents\AUniversidad\Master\AIF\Labs\AIF\Practica2"
pdflatex informe_practica2.tex
pdflatex informe_practica2.tex

# Resultado: informe_practica2.pdf
```

### Opción 3: Visual Studio Code + LaTeX Workshop
1. Instalar extensión: LaTeX Workshop
2. Abrir `informe_practica2.tex`
3. Ctrl+Alt+B para compilar
4. Ctrl+Alt+V para ver PDF

---

## 📋 CHECKLIST FINAL PRE-ENTREGA

### Archivos
- [ ] `informe_practica2.pdf` (generado y completo)
- [ ] `ontology/offf_modified.owl` (exportado de WebProtégé)
- [ ] Tamaño total razonable (< 20 MB)

### Contenido del PDF
- [ ] Portada con nombres, grupo, fecha
- [ ] Índice generado automáticamente
- [ ] Todas las secciones completas (sin [Completar] o TODO)
- [ ] 10 figuras de screenshots visibles
- [ ] Username "santi_david" visible en capturas
- [ ] 3 tablas SPARQL con datos reales
- [ ] Código SPARQL formateado correctamente
- [ ] Referencias completas
- [ ] Sin errores ortográficos

### Verificaciones Técnicas
- [ ] Ontología modificada contiene las 12 clases nuevas
- [ ] Ontología modificada contiene el individuo "My fish sandwich"
- [ ] PDF no tiene errores de compilación
- [ ] Todas las imágenes se cargan correctamente
- [ ] Hipervínculos funcionan

---

## ⚠️ ADVERTENCIAS IMPORTANTES

1. **Ontología modificada es OBLIGATORIA**
   - Sin este archivo, falta un entregable crítico
   - Verifica que tiene tus modificaciones antes de entregar

2. **Tablas SPARQL deben tener datos reales**
   - No dejes placeholders [Completar] o [URI 1]
   - Transcribe desde tus capturas

3. **Fecha límite es ESTRICTA**
   - 29 Octubre 2025, 23:59
   - Sube con tiempo (no esperes al último minuto)

4. **Username debe ser visible**
   - En todas las capturas de WebProtégé
   - Para validar autoría del trabajo

---

## 📊 RESUMEN EJECUTIVO

**Estado actual:** 85% completo

**Falta:**
1. 🔴 Exportar `offf_modified.owl` (5 min)
2. 🔴 Completar 3 tablas de resultados en LaTeX (30 min)
3. 🔴 Completar datos: grupo (1 min)
4. 🟡 Escribir análisis de queries (30 min)
5. 🟡 Revisar y compilar PDF (15 min)

**Tiempo estimado total:** 1.5 horas

**¡Estás muy cerca de terminar!** 🚀

---

## 🎯 SIGUIENTE ACCIÓN INMEDIATA

**Ahora mismo, haz esto:**

1. Abre WebProtégé
2. Export ontología → Guarda como `offf_modified.owl`
3. Abre `informe_practica2.tex`
4. Busca primer "TODO"
5. Transcribe datos de tus capturas

**¡Ánimo! Ya casi lo tienes todo hecho!** 💪
