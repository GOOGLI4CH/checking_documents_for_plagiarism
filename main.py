import os
from difflib import SequenceMatcher

import Levenshtein
import docx


def get_files_from_folder(folder_path):
    files = []
    for root, directories, filenames in os.walk(folder_path):
        for filename in filenames:
            files.append(os.path.join(root, filename))
    return files


def read_docx(file_path):
    try:
        doc = docx.Document(file_path)
        text = ' '.join([paragraph.text for paragraph in doc.paragraphs])
        return text
    except:
        print(f"Не удалось открыть {os.path.basename(file_path)}")
        pass


def write_results(results, output_file):
    with open(output_file, 'w', encoding='utf-8') as file:
        for result in results:
            file.write(result + '\n')


def calculate_similarity_matcher(text1, text2):
    if text1 is None or text2 is None:
        return 0

    matcher = SequenceMatcher(None, text1, text2)
    return matcher.ratio()


def calculate_similarity_levenshtein(text1, text2):
    if text1 is None or text2 is None:
        return 0

    distance = Levenshtein.distance(text1, text2)
    max_length = max(len(text1), len(text2))
    similarity = (max_length - distance) / max_length
    return similarity


def check_plagiarism(file_paths, limit_percent):
    num_files = len(file_paths)
    results = []
    results_plagiarism = []
    limit = limit_percent / 100

    for i in range(num_files):
        for j in range(i + 1, num_files):
            text1 = read_docx(file_paths[i])
            text2 = read_docx(file_paths[j])

            similarity_matcher = calculate_similarity_matcher(text1, text2)
            similarity_levenshtein = calculate_similarity_levenshtein(text1, text2)

            result = f"Файлы {os.path.basename(file_paths[i])} и {os.path.basename(file_paths[j])} схожи на:" \
                     f" matcher({(similarity_matcher * 100):.2f}%) levenshtein({(similarity_levenshtein * 100):.2f}%)"

            if similarity_matcher > limit or similarity_levenshtein > limit:
                results_plagiarism.append(result)
            results.append(result)

    return results, results_plagiarism


def main():
    # Название файла с общим результатом
    output_file = 'result.txt'
    # Название файла с результатом, учитывая предел
    output_plagiarism_file = 'plagiarism_result.txt'
    # Название папки, в которой находятся файлы для проверки
    folder_path = 'data'
    # Процент совпадения (файлы, схожесть которых >= limit, помещаются в отдельный файл)
    limit = 70

    file_paths = get_files_from_folder(folder_path)
    results, results_plagiarism = check_plagiarism(file_paths, limit)
    write_results(results, output_file)
    write_results(results_plagiarism, output_plagiarism_file)


if __name__ == '__main__':
    main()
