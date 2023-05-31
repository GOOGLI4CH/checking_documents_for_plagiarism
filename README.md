<h1>Проверка .docx файлов на плагиат / Checking .docx files for plagiarism</h1>
<p>Этот репозиторий состоит из скрипта Python, который обнаруживает плагиат в файлах .docx с помощью алгоритма Левенштейна и поиска схожих участков в файле.</p>
<p>This repository consists of a Python script that detects plagiarism in .docx files using the Levenshtein algorithm and finds similar areas in the file.</p>

<h3>Начало работы / Getting Started</h3>
<p>Для начала работы с исходным кодом выполните клонирование репозитория командой: <br><code>git clone https://github.com/GOOGLI4CH/checking_documents_for_plagiarism.git </code></p>
<p>To start working with the source code, clone the repository with the command: <br><code>git clone https://github.com/GOOGLI4CH/checking_documents_for_plagiarism.git </code></p>

<h3>Требования / Requirements</h3>
<p>Выполните следующую команду для установки необходимых модулей: <code>pip install -r requirements.txt</code></p>
<p>Run the following command to install the required modules: <code>pip install -r requirements.txt</code></p>

<h3>Описание работы программы / Description of the program</h3>
<p>Файлы, подлежащие проверке следует поместить в выбранную папку. После запуска скрипта все файлы считываются, и каждый файл проходит сравнение с остальными файлами,
находящимися в выбранной папке. Такой путь проходят все файлы, тем самым обеспечивается полное сравнение содержимого всех файлов друг с другом.</p>
<p>The files to be scanned should be placed in the selected folder. After running the script, all files are read, and each file is compared with the rest of the files,
located in the selected folder. All files go through this path, thereby ensuring a complete comparison of the contents of all files with each other.</p>

<h3>Алгоритмы / Algorithms</h3>
<p>Для проверки используется алгоритм Левенштейна и алгоритм поиска схожих участков содержимого файлов.<br>
Расстояние Левенштейна (Алгоритм Левенштейна) - это минимальное число односимвольных преобразований (удаления, вставки или замены), необходимых, чтобы превратить одну последовательность в другую.
Чем больше расстояние, тем более различны строки.<br>
Алгоритм поиска наибольшей общей подпоследовательности (поиск схожих участков) - вычисляет сходство между последовательностями и возвращает значение "отношения сходства",
которое указывает на степень сходства между последовательностями.</p>
<p>For verification, the Levenshtein algorithm and the algorithm for searching for similar sections of file content are used.<br>
The Levenshtein Distance (Levenshtein Algorithm) is the minimum number of single-character transformations (deletions, insertions, or substitutions) required to turn one sequence into another.
The greater the distance, the more distinct the lines.<br>
Algorithm for finding the largest common subsequence (searching for similar sections) - calculates the similarity between sequences and returns the value of the "similarity ratio",
which indicates the degree of similarity between sequences.</p>