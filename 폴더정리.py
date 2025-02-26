from collections import defaultdict
import sys

class Folder:
    def __init__(self):
        self.files = defaultdict(int)  # 파일 이름별 개수 저장
        self.subfolders = {}  # 하위 폴더 저장

    def add_file(self, filename):
        self.files[filename] += 1

    def add_subfolder(self, name):
        if name not in self.subfolders:
            self.subfolders[name] = Folder()
        return self.subfolders[name]

    def count_files(self):
        unique_files = set(self.files.keys())
        total_files = sum(self.files.values())

        for subfolder in self.subfolders.values():
            sub_unique, sub_total = subfolder.count_files()
            unique_files.update(sub_unique)
            total_files += sub_total

        return len(unique_files), total_files  # 파일 종류 개수, 파일 총 개수 반환

# 트리 구조 생성
def build_directory(n, m, entries):
    root = Folder()
    folder_map = defaultdict(Folder)  # 폴더가 자동으로 생성되도록 변경
    folder_map['main'] = root

    for entry in entries:
        parent, name, file_flag = entry.split()

        if file_flag == "0":  # 파일이면
            folder_map[parent].add_file(name)
        else:  # 폴더이면
            folder_map[parent].add_subfolder(name)  # 부모 폴더가 자동 생성됨

    return root, folder_map

# 쿼리 처리
def process_queries(queries, folder_map):
    results = []
    for query in queries:
        folder_path = query.split('/')
        current = folder_map.get('main', None)

        for folder in folder_path[1:]:
            if current and folder in current.subfolders:
                current = current.subfolders[folder]
            else:
                current = None
                break

        if current:
            unique_count, total_count = current.count_files()
            results.append(f"{unique_count} {total_count}")
        else:
            results.append("0 0")

    return results

input = sys.stdin.read
data = input().splitlines()

# 첫 번째 줄: N (폴더 수), M (파일 수)
n, m = map(int, data[0].split())

# N + M 줄의 폴더/파일 정보
entries = data[1:n + m + 1]

# 다음 줄: Q (쿼리 개수)
q = int(data[n + m + 1])

# Q개의 경로 쿼리
queries = data[n + m + 2:n + m + 2 + q]

# 디렉토리 빌드 및 쿼리 처리
root, folder_map = build_directory(n, m, entries)
outputs = process_queries(queries, folder_map)

# ✅ 빠른 출력 처리
sys.stdout.write("\n".join(outputs) + "\n")

