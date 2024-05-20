import asyncio

from gtts import gTTS


proxies = {"http": "http://192.168.18.66:3128", "https": "http://192.168.18.66:3128"}
text_block = """
El impacto de la tecnología en la educación ha sido un tema de gran relevancia en las últimas décadas. Con el avance de la digitalización, los métodos de enseñanza y aprendizaje han experimentado transformaciones significativas que han llevado a debates sobre sus beneficios y desafíos.

En primer lugar, uno de los principales beneficios de la tecnología en la educación es la accesibilidad. Las plataformas en línea permiten que estudiantes de todo el mundo accedan a recursos educativos sin importar su ubicación geográfica. Por ejemplo, los cursos en línea masivos y abiertos (MOOC, por sus siglas en inglés) ofrecen oportunidades educativas a personas que de otra manera no tendrían acceso a educación de calidad. Además, herramientas como las videoconferencias permiten que profesores y estudiantes interactúen en tiempo real, superando barreras físicas y facilitando la educación a distancia.

Otro aspecto positivo es la personalización del aprendizaje. Las tecnologías educativas permiten a los estudiantes avanzar a su propio ritmo y de acuerdo a sus necesidades específicas. Por ejemplo, plataformas como Khan Academy utilizan algoritmos para adaptar el contenido según el progreso del estudiante, ofreciendo ejercicios y lecciones personalizadas. Esto es especialmente beneficioso para estudiantes con diferentes estilos y ritmos de aprendizaje, ya que pueden enfocarse en áreas donde necesitan más práctica y avanzar más rápido en temas que ya dominan.

Además, la tecnología fomenta el desarrollo de habilidades digitales, que son esenciales en el mundo laboral contemporáneo. Desde la alfabetización digital básica hasta habilidades más avanzadas como la programación y el análisis de datos, las herramientas tecnológicas preparan a los estudiantes para un mercado laboral cada vez más digitalizado. El uso de aplicaciones y software en el aula no solo facilita el aprendizaje de contenidos tradicionales, sino que también enseña a los estudiantes a utilizar herramientas tecnológicas que serán cruciales en su vida profesional.

Sin embargo, la integración de la tecnología en la educación también presenta desafíos significativos. Uno de los más evidentes es la brecha digital. No todos los estudiantes tienen acceso a dispositivos electrónicos y a una conexión a internet de calidad, lo que puede aumentar las desigualdades educativas. En muchos países, la infraestructura tecnológica aún es insuficiente, y esto limita las posibilidades de aprovechar las ventajas de la educación digital. Para abordar este problema, es crucial que los gobiernos y las instituciones educativas inviertan en infraestructura y en programas que garanticen el acceso equitativo a la tecnología.

Otro desafío es la capacitación de los docentes. La tecnología por sí sola no mejora la educación; es fundamental que los profesores estén bien capacitados para utilizarla de manera efectiva. Esto incluye no solo el uso de dispositivos y software, sino también la integración de estas herramientas en sus metodologías de enseñanza. Los programas de formación continua para docentes son esenciales para que puedan aprovechar al máximo las herramientas tecnológicas y adaptarse a los cambios en el entorno educativo.

Además, existe el riesgo de una dependencia excesiva de la tecnología, que puede afectar la calidad del aprendizaje. Por ejemplo, el uso indiscriminado de dispositivos puede distraer a los estudiantes y reducir la interacción cara a cara, que es crucial para el desarrollo de habilidades sociales y emocionales. Es importante encontrar un equilibrio entre el uso de la tecnología y los métodos tradicionales de enseñanza para asegurar una educación integral.

Finalmente, la privacidad y la seguridad de los datos son preocupaciones crecientes en la educación digital. La recopilación de datos sobre el rendimiento y el comportamiento de los estudiantes puede ser útil para personalizar el aprendizaje, pero también plantea riesgos de privacidad. Es fundamental establecer políticas claras y estrictas sobre el uso y la protección de los datos para garantizar que la información de los estudiantes esté segura.

En conclusión, la tecnología tiene el potencial de transformar la educación de manera significativa, ofreciendo numerosas ventajas como la accesibilidad, la personalización del aprendizaje y el desarrollo de habilidades digitales. Sin embargo, también es importante abordar los desafíos relacionados con la brecha digital, la capacitación de los docentes, el uso equilibrado de la tecnología y la protección de la privacidad. Solo así se podrá aprovechar plenamente el potencial de la tecnología para mejorar la educación y preparar a los estudiantes para el futuro.
"""

text_block = "Hola a todos, está es una prueba de transformación de texto a voz. Esta es la segunda parte del audio, tienes un texto más extenso para la segunda prueba."


tts = gTTS(text_block, lang="es", proxy="http://192.168.18.66:3128", timeout=60)
asyncio.run(tts.save("audio.mp3"))
