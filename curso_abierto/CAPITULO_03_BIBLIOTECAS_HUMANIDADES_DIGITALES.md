# Capítulo 3 — Bibliotecas de investigación y Humanidades Digitales

**Extensión transdisciplinar de Física Computacional · Jara Juana Bermejo Vega · UGR · edición V1**

## 3.1. Una biblioteca también es infraestructura computacional

Una biblioteca de investigación no es solo un proveedor de documentos: puede aportar descripción bibliográfica, identificadores persistentes, gestión de derechos, preservación de colecciones, normalización de datos y apoyo metodológico a investigaciones digitales. En Humanidades Digitales, la fuente documental y las decisiones de transcripción, clasificación, limpieza y consulta forman parte del argumento científico.

Morales-del-Castillo, Tamayo Ramírez y Peis Redondo (2020) estudian la relación entre bibliotecas de investigación y Humanidades Digitales en España mediante revisión y encuesta a bibliotecas académicas. Su análisis concluye que la colaboración existe frecuentemente, pero suele quedar diluida entre servicios generales; la figura del bibliotecario integrado (*embedded librarian*) puede mejorar el apoyo a datos e investigación.

**Referencia:** Morales-del-Castillo, J. M.; Tamayo Ramírez, R. M.; Peis Redondo, E. (2020). *Bibliotecas de investigación y Humanidades Digitales en España: una relación en construcción*. Revista de Humanidades Digitales, 5, 86–112. DOI: https://doi.org/10.5944/RHD.VOL.5.2020.27653. [Acceso del editor](https://revistas.uned.es/index.php/RHD/article/view/27653).

## 3.2. Entornos UGR y límites de acceso

Recursos institucionales: [Biblioteca Universitaria](https://biblioteca.ugr.es/), [Biblioguías UGR](https://bibliotecaugr.libguides.com/), [Digital Research in the Arts and Humanities](https://bibliotecaugr.libguides.com/digital_research), [Digibug](https://digibug.ugr.es/) y [Portal de Producción Científica](https://produccioncientifica.ugr.es/). La biblioguía de Digital Research describe una colección de eBooks de Taylor & Francis con **acceso restringido a miembros de la UGR**. Poder consultar un título mediante acreditación institucional no concede permiso para copiarlo, indexarlo públicamente o entrenar modelos con su contenido.

Separa tres clases: (A) metadatos bibliográficos disponibles conforme a sus condiciones, (B) obras abiertas con permisos explícitos y (C) obras restringidas que se pueden enlazar pero **no republicar**. Un repositorio abierto debe poder funcionar sin autenticarse en servicios restringidos.

## 3.3. Esquema de un documento investigable

```yaml
KRONE_DIGITAL_SOURCE_V1:
  title: Bibliotecas de investigación y Humanidades Digitales en España
  creators: [Morales-del-Castillo, Tamayo_Ramirez, Peis_Redondo]
  year: 2020
  identifier: doi:10.5944/RHD.VOL.5.2020.27653
  record_source: UGR_produccion_cientifica_y_editor
  access: OPEN_ACCESS_EDITOR_RECORD
  full_text_license: VERIFY_AT_EDITOR_BEFORE_COPY_OR_TDM
  extraction_method: MANUAL_METADATA_ONLY
  checksum: NOT_COMPUTED
  provenance: LINKED_EXTERNAL_SOURCE
  sensitive_data: false
```

Los campos expresan **qué sabemos y cómo lo sabemos**, no supuestas condiciones jurídicas no verificadas. Un DOI identifica una obra; **no es una licencia**. Un hash identifica unos bytes; no certifica que la transcripción sea fiel ni que su distribución esté autorizada.

## 3.4. Investigación digital como experimento reproducible

Una práctica responsable con un corpus realiza: selección explícita de fuentes → lectura de metadatos → limpieza documentada → análisis (palabras, coocurrencias, grafos, clasificación) → estimación de sesgos y cobertura → visualización reproducible → interpretación humanística. La etapa de interpretación no se puede sustituir por un clasificador.

**Actividad original:** a partir de los metadatos públicos de diez publicaciones seleccionadas, forma un grafo de relaciones documento–autor–palabra clave, respetando variantes de autoría y coincidencias de nombre. Compara los grados del grafo antes y después de la normalización. Explica qué decisiones de limpieza podrían producir asociaciones falsas. No descargues automáticamente PDFs ni el texto de eBooks restringidos.

## 3.5. Bibliotecario integrado, colaboración y responsabilidades

Un proyecto genuinamente interdisciplinar distingue la autoridad científica de la persona investigadora, el conocimiento documental de bibliotecas, la responsabilidad de instituciones editoras y los derechos de las personas autoras. Puede acordar glosarios, formatos de exportación, taxonomías, control de versiones, procedimientos FAIR cuando sean aplicables y calendarios de preservación. **FAIR no equivale a abierto sin condiciones**.

## 3.6. HyperJarra, recuperación y modelos locales

Un índice HyperJarra registra nodos tipados de documentos y sus procedencias. LlamaIndex puede actuar como una **proyección adaptadora** de ingestión/búsqueda; Ollama o llama.cpp como posibles ejecutores de modelos locales; un modelo de la familia Llama es otra identidad distinta. El curso no requiere dichos componentes para funcionar: la búsqueda léxica e índices JSON legibles bastan para el recorrido inicial.

**Regla de privacidad:** metadatos públicos correctamente autorizados pueden indexarse; datos personales de estudiantes, correos privados, invitaciones editoriales confidenciales, manuscritos bajo revisión y libros restringidos **no** deben introducirse en un índice docente público ni en un RAG externo. Las sugerencias de un LLM permanecen como hipótesis; no prueban autoría, hechos ni permisos.

## Cierre

En computación científica el testigo es un observable físico calculado y contrastado; en Humanidades Digitales es un resultado analítico respaldado por fuentes, decisiones editoriales y contexto interpretativo. En ambos casos, **método + procedencia + límites + interpretación** es el núcleo de la reproducibilidad.
