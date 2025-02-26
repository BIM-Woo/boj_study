import sys
from collections import defaultdict, deque

class FileSystem:
    def __init__(self):
        self.folders = defaultdict(lambda: {"files": set(), "subfolders": set()})  # 폴더 구조 저장
        self.file_counts = defaultdict(int)  # 파일 개수 저장 (중복 포함)
        self.cache = {}  # 쿼리 결과 캐싱

    def add_entry(self, parent, name, is_folder):
        """폴더 또는 파일을 추가하는 함수"""
        if is_folder:
            self.folders[parent]["subfolders"].add(name)
            self.folders[name]  # 빈 폴더도 초기화
        else:
            self.folders[parent]["files"].add(name)
            self.file_counts[name] += 1

    def move(self, src, dst):
        """폴더를 이동하는 함수"""
        if src not in self.folders or dst not in self.folders:
            return
        
        # 이동할 폴더의 파일과 서브폴더 가져오기
        src_files = self.folders[src]["files"]
        src_subfolders = self.folders[src]["subfolders"]

        # 대상 폴더에 데이터 병합
        dst_files = self.folders[dst]["files"]
        dst_subfolders = self.folders[dst]["subfolders"]

        # 같은 파일이 있을 경우 덮어쓰기 (파일 개수는 그대로 유지)
        for file in src_files:
            dst_files.add(file)

        # 하위 폴더 병합
        dst_subfolders.update(src_subfolders)

        # 상위 폴더에서 이동한 폴더 제거
        for parent in self.folders:
            if src in self.folders[parent]["subfolders"]:
                self.folders[parent]["subfolders"].remove(src)
                break

        # 원본 폴더 삭제
        del self.folders[src]

        # 캐시 초기화 (폴더 이동 후 기존 정보 무효화)
        self.cache.clear()

    def count_files(self, folder):
        """특정 폴더 내 파일 개수와 종류를 계산하는 함수"""
        if folder in self.cache:
            return self.cache[folder]

        if folder not in self.folders:
            return (0, 0)

        unique_files = set()
        total_files = 0
        queue = deque([folder])

        while queue:
            current = queue.popleft()
            unique_files.update(self.folders[current]["files"])
            total_files += sum(self.file_counts[file] for file in self.folders[current]["files"])
            queue.extend(self.folders[current]["subfolders"])

        self.cache[folder] = (len(unique_files), total_files)
        return self.cache[folder]

def main():
    input = sys.stdin.read
    data = input().splitlines()

    fs = FileSystem()

    print("=== DEBUG: 입력 데이터 확인 ===")
    print(data)

    # 폴더 및 파일 개수 입력
    N, M = map(int, data[0].split())

    # 폴더 및 파일 정보 입력
    for i in range(1, N + M + 1):
        P, F, C = data[i].split()
        fs.add_entry(P, F, int(C))

    print("=== DEBUG: 폴더 초기 구조 확인 ===")
    for folder, contents in fs.folders.items():
        print(f"{folder}: {contents}")

    # 이동 횟수 입력
    K = int(data[N + M + 1])

    # 폴더 이동 처리
    index = N + M + 2
    for _ in range(K):
        A, B = data[index].split()
        fs.move(A, B)
        index += 1

    print("=== DEBUG: 폴더 이동 후 구조 확인 ===")
    for folder, contents in fs.folders.items():
        print(f"{folder}: {contents}")

    # 쿼리 개수 입력
    Q = int(data[index])
    index += 1

    # 쿼리 처리
    results = []
    queried_folders = []
    for _ in range(Q):
        folder = data[index]
        queried_folders.append(folder)
        results.append(" ".join(map(str, fs.count_files(folder))))
        index += 1

    print("=== DEBUG: 쿼리 처리 확인 ===")
    for folder in queried_folders:
        print(f"쿼리: {folder} -> {fs.count_files(folder)}")

    print("\n".join(results))

if __name__ == "__main__":
    main()
