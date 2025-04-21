
---

### 📑 Reporte HTML de resultados

<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Reporte de Pruebas Automatizadas con Selenium</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 40px;
            background-color: #f4f4f4;
        }
        h1, h2 {
            color: #2c3e50;
        }
        ul {
            list-style: none;
            padding-left: 0;
        }
        li {
            background: #ecf0f1;
            margin: 10px 0;
            padding: 10px;
            border-left: 6px solid #27ae60;
        }
        .fallido {
            border-left-color: #c0392b;
        }
        .explicacion {
            background-color: #fff;
            padding: 15px;
            border-left: 5px solid #3498db;
            margin-top: 30px;
        }
    </style>
</head>
<body>

    <h1>📋 Reporte de Pruebas Automatizadas</h1>

    <h2>✅ Resultados</h2>
    <ul>
        <li>Registro de usuario: <strong>Éxito</strong></li>
        <li>Carga de archivo: <strong>Éxito</strong></li>
        <li>Descarga de archivo: <strong>Éxito</strong></li>
        <li>Alerta de confirmación: <strong>Éxito</strong></li>
        <li>Alerta de prompt: <strong>Éxito</strong></li>
    </ul>

    <div class="explicacion">
        <h2>⚙️ Modo Headless y Manejo de Descargas</h2>

        <p>Las pruebas fueron ejecutadas en <strong>modo headless</strong>, lo que significa que el navegador Google Chrome se ejecutó en segundo plano sin interfaz gráfica. Esto se logra mediante la configuración de Selenium con el siguiente argumento:</p>
        <pre><code>options.add_argument("--headless")</code></pre>

        <p>Además, para permitir la <strong>descarga automática de archivos</strong> en este modo (que normalmente está restringida), se configuraron las preferencias del navegador usando:</p>
        <pre><code>
options.add_experimental_option("prefs", {
    "download.default_directory": "C:/downloads",
    "download.prompt_for_download": False,
    "directory_upgrade": True,
    "safebrowsing.enabled": True
})
        </code></pre>

        <p>Esto permite que los archivos descargados durante las pruebas se guarden directamente en <strong>C:/downloads</strong> sin mostrar ningún cuadro de diálogo.</p>

        <p>Esta configuración es esencial para asegurar que las pruebas puedan ejecutarse correctamente en entornos automatizados como CI/CD o servidores remotos sin interfaz gráfica.</p>
    </div>

</body>
</html>
