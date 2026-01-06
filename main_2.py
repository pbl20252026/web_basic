# TASK TODO CRUD BASIC
# C: create R: read U: update D: delete


# 1. Tạo một mảng để lưu các todo
todos = []


# 2. Tạo hàm để đọc toàn bộ các todo đó (Ân)
def read_todo(todos):
    for i in range(len(todos)):
        print(f"{i+1}: {todos[i]}")

# 3. Tạo hàm để thêm một todo mới vào mảng trên (Huy)


def them_todo(todos, id, title):
    todo = {
        "id": id,
        "title": title,
        "done": False
    }
    todos.append(todo)


# 4. Tạo hàm để xóa một todo dựa trên chỉ số của nó trong mảng (Quyền)
def delete_todo(index):
    index = int(input("Nhập chỉ số của todo cần xóa: "))-1
    if 0 <= index < len(todos):
        todos.pop(index)
    else:
        print("Index không hợp lệ")


# 5. Tạo hàm để cập nhật một todo dựa trên chỉ số của nó trong mảng (Nhân)
def update_todo(index, task):
    if 0 <= index < len(todos):
        todos[index] = task
    else:
        print("Index không hợp lệ")

# 6. Tạo hàm xóa toàn bộ các todo trong mảng (Bùi)


def xoa_todos():
    todos.clear()
    print('Toàn bộ todo đã được xóa trong mảng')

# 7. Xóa toàn bộ các todo trong mảng


def clear_todos():
    todos.clear()
