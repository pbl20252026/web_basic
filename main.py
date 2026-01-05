# TASK TODO CRUD BASIC
# C: create R: read U: update D: delete


# 1. Tạo một mảng để lưu các todo
todos = []


# 2. Tạo hàm để đọc toàn bộ các todo đó (Ân)
def read(todos):
    print("------Danh sách công việc------")
    for i in range(len(todos)):
        print(f"{i+1}: {todos[i]}")



# 3. Tạo hàm để thêm một todo mới vào mảng trên (Huy)
def create(task):
    todos.append(task)
    print(f"Đã thêm công việc: '{task}' vào danh sách.")

# 4. Tạo hàm để xóa một todo dựa trên chỉ số của nó trong mảng (Quyền)


# 5. Tạo hàm để cập nhật một todo dựa trên chỉ số của nó trong mảng (Nhân)


# 6. Tạo hàm xóa toàn bộ các todo trong mảng (Bùi)
def clear_todos():
    todos.clear()
    print("Đã xóa toàn bộ công việc trong danh sách.")


# 7. Xóa toàn bộ các todo trong mảng
def clear_todos():
    todos.clear()
