import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta

# ---------------------------------------------------------
# CONFIGURACIÓN DE PÁGINA
# ---------------------------------------------------------
st.set_page_config(
    page_title="Prodeman BI & Data Engineering Showcase | Luciano",
    page_icon="🥜",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Estilo personalizado CSS
st.markdown("""
    <style>
    .main-title {
        color: #1E3A8A;
        font-size: 2.2rem;
        font-weight: 700;
        margin-bottom: 0px;
    }
    .sub-title {
        color: #475569;
        font-size: 1.1rem;
        margin-bottom: 20px;
    }
    .metric-card {
        background-color: #F8FAFC;
        border-left: 5px solid #2563EB;
        padding: 15px;
        border-radius: 8px;
        box-shadow: 0 1px 3px rgba(0,0,0,0.1);
    }
    .status-ok {
        color: #16A34A;
        font-weight: bold;
    }
    .status-warn {
        color: #CA8A04;
        font-weight: bold;
    }
    </style>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# NAVEGACIÓN Y SIDEBAR
# ---------------------------------------------------------
st.sidebar.image("https://img.icons8.com/color/96/peanut.png", width=70)
st.sidebar.title("Prodeman Data Hub")
st.sidebar.caption("Propuesta Técnica & Demo de BI | Área de Sistemas e Innovación")

menu = st.sidebar.radio(
    "Seleccione una sección:",
    [
        "🎯 Propuesta & Perfil Profesional",
        "📊 Dashboard Operativo (Agroindustria)",
        "⚙️ Pipeline ETL & Control de Calidad",
        "📑 Gobernanza y Documentación"
    ]
)

st.sidebar.markdown("---")
st.sidebar.info("""
**Candidato:** Luciano  
**Título:** Licenciado en Sistemas  
**Stack Clave:** SQL Server, Python, Power BI, DAX, Pandas, ETL, Agile.  
""")

# ---------------------------------------------------------
# SECCIÓN 1: PROPUESTA Y PERFIL PROFESIONAL
# ---------------------------------------------------------
if menu == "🎯 Propuesta & Perfil Profesional":
    st.markdown('<p class="main-title">Propuesta de Postulación — Área de Sistemas, Mejora e Innovación</p>', unsafe_allow_html=True)
    st.markdown('<p class="sub-title">Candidato: Lic. en Sistemas | Integración, Transformación y Visualización de Datos para Prodeman</p>', unsafe_allow_html=True)
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.subheader("📌 ¿Por qué encajo en el perfil solicitado?")
        st.markdown("""
        Como **Licenciado en Sistemas** con sólida trayectoria en la construcción de soluciones analíticas y docencia universitaria en Data Science, cuento con la combinación exacta de competencias técnicas y mentalidad de servicio que Prodeman requiere:

        * **Solidez Técnica en Datos:** Experiencia práctica diseñando e implementando flujos **ETL**, modelos de datos estables (**SQL Server, MySQL**) y tableros de alto impacto en **Power BI (DAX)** y **Python (Pandas, Streamlit, Matplotlib, Seaborn)**.
        * **Orientación al Negocio:** Habilidad demostrada para dialogar con usuarios clave, traducir necesidades operativas/comerciales en modelos analíticos reutilizables y entregar respuestas concretas.
        * **Atención al Detalle & Calidad:** Rigor en la validación de inconsistencias, deduplicación y reglas de negocio para asegurar datos confiables antes de su consumo.
        * **Cultura de Documentación:** Hábito sistemático de documentar diccionarios de datos, linaje de transformación y manuales de dashboards para garantizar la sostenibilidad de la infraestructura.
        """)
    
    with col2:
        st.subheader("🛠️ Matriz de Requisitos vs. Perfil")
        data_req = {
            "Requisito Prodeman": ["SQL Server / MySQL", "Python & Pandas", "Power BI & DAX", "ETL & Automatización", "Excel Avanzado", "Metodologías Ágiles"],
            "Nivel de Dominio": ["Avanzado", "Avanzado", "Avanzado", "Avanzado", "Avanzado", "Scrum / Kanban"]
        }
        df_req = pd.DataFrame(data_req)
        st.dataframe(df_req, hide_index=True, use_container_width=True)

    st.markdown("---")
    st.subheader("🚀 Propuesta de Valor para Prodeman")
    
    col_a, col_b, col_c = st.columns(3)
    with col_a:
        st.markdown("""
        <div class="metric-card">
            <h4>1. Unificación de Fuentes</h4>
            <p>Conectar balanzas de acopio, sistemas ERP, líneas de proceso y exportación en un Data Repository centralizado.</p>
        </div>
        """, unsafe_allow_html=True)
    with col_b:
        st.markdown("""
        <div class="metric-card">
            <h4>2. Data Quality & Auditoría</h4>
            <p>Monitoreo automatizado de procesos ETL para alertar desvíos o fallas antes de que lleguen a los tableros gerenciales.</p>
        </div>
        """, unsafe_allow_html=True)
    with col_c:
        st.markdown("""
        <div class="metric-card">
            <h4>3. Cultura Data-Driven</h4>
            <p>Capacitación y acompañamiento a usuarios de negocio para maximizar la adopción de Power BI y reportes autoservicio.</p>
        </div>
        """, unsafe_allow_html=True)

# ---------------------------------------------------------
# SECCIÓN 2: DASHBOARD OPERATIVO AGROINDUSTRIAL
# ---------------------------------------------------------
elif menu == "📊 Dashboard Operativo (Agroindustria)":
    st.markdown('<p class="main-title">Tablero Operativo de Control — Prodeman BI Demo</p>', unsafe_allow_html=True)
    st.markdown('<p class="sub-title">Visión integral de recepción de maní, procesamiento industrial, exportaciones y generación de energía biomasa.</p>', unsafe_allow_html=True)
    
    # Filtros
    col_f1, col_f2 = st.columns(2)
    with col_f1:
        planta = st.selectbox("Seleccionar Planta / Sede:", ["General Cabrera (Planta Principal)", "Centro de Acopio Norte", "Centro de Acopio Sur"])
    with col_f2:
        periodo = st.select_slider("Rango de Tiempo:", options=["Últimos 7 días", "Último Mes", "Último Trimestre", "Campaña Actual"])
    
    st.markdown("---")
    
    # KPIs Superiores
    kpi1, kpi2, kpi3, kpi4 = st.columns(4)
    kpi1.metric("Ingreso Maní (Tn)", "14,850 Tn", "+8.2% vs semana previa")
    kpi2.metric("Rendimiento Blanqueado", "88.4%", "+1.1% ef. proceso")
    kpi3.metric("Energía Biomasa (MWh)", "3,420 MWh", "Cáscara procesada: 94%")
    kpi4.metric("Exportaciones Programadas", "420 Containers", "Destinos: UE, Asia, EE.UU.")
    
    st.markdown("###")
    
    # Gráficos
    col_g1, col_g2 = st.columns(2)
    
    # Datos simulados de recepción
    np.random.seed(42)
    fechas = pd.date_range(end=datetime.today(), periods=15)
    df_recepcion = pd.DataFrame({
        "Fecha": fechas,
        "Maní Confitería (Tn)": np.random.randint(400, 900, size=15),
        "Maní Industria (Tn)": np.random.randint(150, 400, size=15),
        "Humedad Promedio (%)": np.round(np.random.uniform(7.5, 10.2, size=15), 1)
    })
    
    with col_g1:
        st.subheader("🌾 Ingreso Diario de Materia Prima por Tipo")
        fig1 = px.bar(
            df_recepcion, x="Fecha", y=["Maní Confitería (Tn)", "Maní Industria (Tn)"],
            title="Volumen Recibido (Toneladas)",
            barmode="stack",
            color_discrete_sequence=["#1E3A8A", "#D97706"]
        )
        fig1.update_layout(legend_title="Variedad", margin=dict(l=20, r=20, t=40, b=20))
        st.plotly_chart(fig1, use_container_width=True)
        
    with col_g2:
        st.subheader("⚡ Producción Energética (Biomasa) vs. Consumo")
        df_energia = pd.DataFrame({
            "Día": [f"Día {i}" for i in range(1, 11)],
            "Energía Generada (MWh)": np.random.randint(280, 350, size=10),
            "Consumo Planta (MWh)": np.random.randint(220, 290, size=10)
        })
        fig2 = px.line(
            df_energia, x="Día", y=["Energía Generada (MWh)", "Consumo Planta (MWh)"],
            markers=True,
            color_discrete_sequence=["#16A34A", "#DC2626"],
            title="Generación con Cáscara de Maní vs Consumo Térmico/Eléctrico"
        )
        fig2.update_layout(margin=dict(l=20, r=20, t=40, b=20))
        st.plotly_chart(fig2, use_container_width=True)

# ---------------------------------------------------------
# SECCIÓN 3: PIPELINE ETL & DATA QUALITY
# ---------------------------------------------------------
elif menu == "⚙️ Pipeline ETL & Control de Calidad":
    st.markdown('<p class="main-title">Monitoreo del Pipeline ETL & Calidad de Datos</p>', unsafe_allow_html=True)
    st.markdown('<p class="sub-title">Demostración de extracción de fuentes heterogéneas, transformaciones con Pandas/SQL y validación automática de inconsistencias.</p>', unsafe_allow_html=True)
    
    st.subheader("🔄 Estado de Ejecución de Flujos ETL")
    
    etl_data = {
        "Flujo ETL": ["Ingesta_Balanzas_Acopio", "Transformacion_Humedad_Calidad", "Sync_SQLServer_PowerBI", "Exportaciones_ERP_MySQL", "Telemetria_Biomasa"],
        "Origen": ["MySQL Balanzas", "CSV / IoT Sensores", "SQL Server DW", "ERP SAP/Oracle"],
        "Destino": ["Data Mart Acopio", "Data Mart Calidad", "Dataset Power BI", "Data Mart Logística", "Data Mart Energía"],
        "Frecuencia": ["Cada 15 min", "Cada 1 hora", "Diario (06:00 hs)", "Cada 30 min", "Tiempo Real"],
        "Última Ejecución": ["Hace 5 min", "Hace 20 min", "Hoy 06:00 hs", "Hace 12 min", "Activo"],
        "Estado": ["OK", "OK", "OK", "OK", "OK"]
    }
    df_etl = pd.DataFrame(etl_data)
    st.dataframe(df_etl, hide_index=True, use_container_width=True)
    
    st.markdown("---")
    st.subheader("🧪 Simulador de Limpieza e Ingesta de Datos (Pandas & SQL Logic)")
    
    st.write("Carga o simulación de datos crudos con anomalías (registros nulos, fuera de rango o duplicados):")
    
    if st.button("Ejecutar Pipeline de Limpieza"):
        # Generar datos sucios
        raw_data = pd.DataFrame({
            "ID_Lote": [101, 102, 103, 104, 105, 105, 107],
            "Productor": ["Agro del Sur", "Estancia El Maní", None, "Campos Cabrera", "Agro del Sur", "Agro del Sur", "Cooperativa X"],
            "Humedad_%": [8.5, 14.2, 9.1, -2.0, 8.8, 8.8, 25.0],  # Anomalías: -2.0 y 25.0
            "Kilos_Netos": [28500, 31000, 27400, 29000, 28000, 28000, 30500]
        })
        
        c1, c2 = st.columns(2)
        with c1:
            st.caption("❌ Datos Crudos (con errores/duplicados):")
            st.dataframe(raw_data, use_container_width=True)
            
        with c2:
            st.caption("✅ Datos Transformados y Validados (Post-ETL):")
            # Proceso de limpieza
            clean_data = raw_data.drop_duplicates(subset=["ID_Lote"]).copy()
            clean_data["Productor"] = clean_data["Productor"].fillna("Desconocido / A Clasificar")
            # Regla de calidad: Humedad entre 5% y 18%
            clean_data = clean_data[(clean_data["Humedad_%"] >= 5.0) & (clean_data["Humedad_%"] <= 18.0)]
            st.dataframe(clean_data, use_container_width=True)
            
        st.success("✅ Proceso completado: 1 duplicado eliminado, 1 valor nulo imputado y 2 registros fuera de rango corregidos/filtrados.")

# ---------------------------------------------------------
# SECCIÓN 4: GOBERNANZA Y DOCUMENTACIÓN
# ---------------------------------------------------------
elif menu == "📑 Gobernanza y Documentación":
    st.markdown('<p class="main-title">Estrategia de Documentación & Gobernanza</p>', unsafe_allow_html=True)
    st.markdown('<p class="sub-title">Estándares para asegurar trazabilidad, orden y mantenibilidad de la infraestructura de datos en Prodeman.</p>', unsafe_allow_html=True)
    
    st.subheader("📘 Modelo de Diccionario de Datos (Muestra Data Warehouse)")
    
    dict_data = {
        "Tabla DW": ["dim_producto", "dim_producto", "fact_recepcion", "fact_recepcion", "fact_exportacion"],
        "Campo": ["id_producto", "nombre_producto", "id_recepcion", "porcentaje_humedad", "flete_contenedor_id"],
        "Tipo de Dato": ["INT (PK)", "VARCHAR(100)", "BIGINT (PK)", "DECIMAL(4,2)", "VARCHAR(50)"],
        "Regla de Negocio / Descripción": [
            "Identificador único del tipo de maní (Confitería, Blanqueado, Aceite).",
            "Descripción comercial de la materia prima o subproducto.",
            "Clave primaria correlativa por pesada de camión en balanza.",
            "Medición de humedad al ingreso. Rango válido: 6.00% a 15.00%.",
            "Código de seguimiento del contenedor asignado para exportación."
        ]
    }
    st.table(pd.DataFrame(dict_data))
    
    st.markdown("---")
    st.subheader("📌 Buenas Prácticas Aportadas al Rol")
    st.markdown("""
    1. **Sistemas de Control de Versiones:** Repositorios Git estructurados para scripts ETL en Python y esquemas SQL.
    2. **Documentación de Dashboards:** Fichas técnicas por tablero en Power BI indicando: *Usuario Sponsor, Frecuencia de Actualización, Linaje de Datos y Glosario de Métricas DAX*.
    3. **Alertas de Calidad:** Notificaciones vía Email/Teams cuando un job ETL falla o presenta inconsistencias graves en el volumen de datos ingresado.
    """)
